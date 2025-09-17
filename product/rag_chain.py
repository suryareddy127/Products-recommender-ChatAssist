from langchain_groq import ChatGroq
from langchain.chains import create_history_aware_retriever,create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from product.config import config

class RAGChain:
    def __init__(self,vector_store):
        self.vector_store=vector_store
        self.model = ChatGroq(model=config.RAG_MODEL,temperature=0.5)
        self.history_store = {}
        
    def _get_history(self,session_id:str) -> BaseChatMessageHistory:
        if session_id not in self.history_store:
            self.history_store[session_id] = ChatMessageHistory()
        return self.history_store[session_id]
    
    def build_chain(self):
        retriever = self.vector_store.as_retriever(search_kwargs={"k":3})
        
        context_prompt = ChatPromptTemplate.from_messages([
            ("system","You are a product review analysis assistant. Use the following pieces of context to answer the users question. If you don't know the answer, just say that you don't know,"),
            MessagesPlaceholder(variable_name="history"),
            ("user","{input}")
        ])
        
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system","""You're a Product review analysis chatbot answering product-related queries using reviews and titles.
                          Stick to context. Be concise and helpful.\n\nCONTEXT:\n{context}\n\nQUESTION: {input}"""),
            MessagesPlaceholder(variable_name="history"),
            ("user","{input}")
        ])
          
        history_aware_retriever = create_history_aware_retriever(
            self.model , retriever,context_prompt
        )
        question_answering_chain = create_stuff_documents_chain(
            self.model,qa_prompt
        )
        rag_chain =create_retrieval_chain(
            history_aware_retriever,question_answering_chain
        )
        
        return RunnableWithMessageHistory(
            rag_chain, 
            self._get_history,
            input_messages_key="input",
            history_messages_key="history",
            output_messages_key="answer"
        )
        