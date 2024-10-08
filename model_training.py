import os
from google.cloud import aiplatform

# Initialize Vertex AI
aiplatform.init(project="your-gcp-project-id", location="us-central1")

def deploy_model():
    # Deploy a pre-trained model (e.g., GPT/BERT) on Vertex AI
    model = aiplatform.Model.upload(
        display_name="customer-support-model",
        artifact_uri="gs://your-bucket-name/model/",
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-5:latest"
    )

    # Endpoint creation for serving the model
    endpoint = model.deploy(machine_type="n1-standard-4")
    print(f"Model deployed at endpoint: {endpoint.resource_name}")

if __name__ == "__main__":
    deploy_model()
