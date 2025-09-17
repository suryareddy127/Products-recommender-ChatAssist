# 🛍️ Products Recommender ChatBot

An intelligent chatbot that helps users discover products through natural conversation. Built with Python and Flask, this project integrates monitoring tools like Prometheus and Grafana, and is designed for scalable deployment on Google Cloud Platform (GCP).


## ✨ Features

💬 Conversational product recommendations

🧠 Uses review data to answer questions

🐍 Built with Python and LangChain

⚙️ Flask & app backend for production

🐳 Docker support for containerized deployment

📈 Monitoring via Prometheus and Grafana

🧩 Modular codebase for easy customization


## 🧰 Tech Stack

🐍 Python-->Backend logic

🔥Flask -->Web framework

🎨 HTML/CSS -->Frontend templates

🐳 Docker -->Containerization

📊 Prometheus -->Metrics collection

📈 Grafana -->Visualization and monitoring

🚀 GCP (Cloud Run) -->Scalable cloud deployment


## 🧠 How It Works

**Data Conversion:** Product reviews from a CSV file are converted into searchable documents.

**Embeddings:** Text is transformed into vectors using HuggingFace models.

**Storage:** Vectors are stored in AstraDB for fast retrieval.

**RAG Pipeline:** LangChain connects the database with a Groq-powered chatbot that answers questions using relevant reviews.

**Session Memory:** Each user session keeps track of chat history for better context.
