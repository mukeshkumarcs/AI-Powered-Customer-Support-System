# AI-Powered Customer Support System

This project demonstrates an AI-powered customer support system utilizing Google Vertex AI and large language models (LLMs) to automate customer interactions.

### Key Features:
- **LLM Integration**: Leverages a pre-trained BERT/GPT model for customer queries.
- **GCP Services**: Deployed on Google Cloud using Vertex AI and Cloud Run for scalability.
- **AutoML Optimization**: Used AutoML to train the model and ensure high performance.

### How to Run:
1. Clone the repository: `git clone https://github.com/your-github-username/ai-customer-support-system.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the app locally: `python main.py`
4. Deploy to GCP:
   - Use `model_training.py` to deploy the AI model on Google Vertex AI.
   - Use the provided `Dockerfile` to containerize the app and deploy to Google Cloud Run.
