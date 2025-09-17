*🛍️ Products Recommender ChatBot*
A conversational AI chatbot that helps users discover products based on their preferences. Built with Python and Flask, and deployed via Vercel, this project integrates monitoring tools like Prometheus and Grafana for performance insights.

📦 Features
🧠 Intelligent product recommendations via chat

🌐 Flask-based backend with Gunicorn for production

📦 Docker support for containerized deployment

📊 Monitoring with Prometheus and Grafana

🧩 Modular codebase for easy extension

🧰 Tech Stack
Technology	Role
Python	Backend logic
Flask	Web framework
HTML/CSS	Frontend templates
Docker	Containerization
Prometheus	Metrics collection
Grafana	Visualization and monitoring
📁 Project Structure
Code
├── app.py                  # Main Flask app
├── data/                   # Product data files
├── product/                # Recommendation logic
├── templates/              # HTML templates
├── static/                 # CSS and JS assets
├── utils/                  # Utility functions
├── grafana/, prometheus/   # Monitoring setup
├── Dockerfile              # Docker configuration
├── flask-deployment.yaml   # Deployment config
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
⚙️ Installation & Local Setup
bash
# Clone the repo
git clone https://github.com/suryareddy127/Products-recommender-ChatBot.git
cd Products-recommender-ChatBot

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
🐳 Docker Deployment
bash
# Build the Docker image
docker build -t recommender-chatbot .

# Run the container
docker run -p 5000:5000 recommender-chatbot

🌐 Vercel Deployment
Push your code to GitHub.
Go to vercel.com, import the repo.
Set up environment variables if needed.
Deploy and monitor via Vercel dashboard.

📡 Monitoring Setup

Prometheus: Configure scraping targets in prometheus.yml.

Grafana: Import dashboards and connect to Prometheus data source.

📚 API Overview
Endpoint	Method	Description
/	GET	Home --> page
/recommend	POST --> Accepts user input, returns product suggestions
Example request:

json
POST /recommend
{
  "query": "I need a budget smartphone"
}
