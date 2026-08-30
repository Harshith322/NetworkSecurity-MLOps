# Network Security Threat Detection & MLOps Pipeline

An end-to-end machine learning pipeline for detecting network security threats using supervised classification, automated data processing, model evaluation, and containerized deployment.

## Overview

```text
Raw Network Data
       |
       v
Data Ingestion
       |
       v
Data Validation
       |
       v
Data Transformation
       |
       v
Model Training
       |
       v
Model Evaluation
       |
       v
Trained Model
       |
       v
Prediction Application
```

## Features

- Automated data ingestion and validation
- Feature transformation and preprocessing
- Multiple classification models
- Hyperparameter evaluation
- F1 Score, Precision, and Recall evaluation
- MLflow experiment tracking
- Serialized model artifacts for inference
- FastAPI prediction application
- Docker containerization
- GitHub Actions CI/CD
- Cloud deployment support

## Machine Learning Pipeline

### Data Ingestion
Loads the network security dataset and prepares it for processing.

### Data Validation
Validates input data against the expected schema.

### Data Transformation
Transforms features into a format suitable for machine learning and saves the preprocessing object for inference.

### Model Training

The pipeline evaluates:

- Random Forest
- Decision Tree
- Gradient Boosting
- Logistic Regression
- AdaBoost

The best-performing model is selected based on the evaluation results.

### Model Evaluation

Models are evaluated using:

- Precision
- Recall
- F1 Score

MLflow can be used to track metrics and model artifacts.

## Project Structure

```text
NetworkSecurity-MLOps/
|
├── .github/
│   └── workflows/
├── data_schema/
│   └── schema.yaml
├── Network_Data/
│   └── phishingData.csv
├── networksecurity/
│   ├── cloud/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
├── final_model/
├── prediction_output/
├── templates/
│   └── table.html
├── app.py
├── main.py
├── push_data.py
├── requirements.txt
└── README.md
```

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Machine Learning | Scikit-learn |
| API | FastAPI |
| Experiment Tracking | MLflow |
| Database | MongoDB |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | AWS |
| Data Processing | NumPy / Pandas |

## Running Locally

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd NetworkSecurity-MLOps
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file:

```env
MONGO_DB_URL=<YOUR_MONGODB_CONNECTION_STRING>

MLFLOW_TRACKING_URI=<YOUR_MLFLOW_TRACKING_URI>
MLFLOW_TRACKING_USERNAME=<YOUR_MLFLOW_USERNAME>
MLFLOW_TRACKING_PASSWORD=<YOUR_MLFLOW_PASSWORD>
```

Never commit `.env` or credentials to the repository.

### 5. Run the training pipeline

```bash
python main.py
```

### 6. Start the application

```bash
python app.py
```

## Docker

Build the image:

```bash
docker build -t network-security .
```

Run the container:

```bash
docker run -p 8000:8000 network-security
```

## CI/CD

The project includes a GitHub Actions workflow for automating build and deployment steps.

```text
Git Push
   |
   v
Run Tests
   |
   v
Build Docker Image
   |
   v
Push Image to Container Registry
   |
   v
Deploy Application
```

Cloud credentials should be stored as GitHub Actions Secrets rather than committed to the repository.

## MLflow

When configured, MLflow tracks model experiments, metrics, and model artifacts.

Tracked metrics include:

- F1 Score
- Precision
- Recall

MLflow configuration is provided through environment variables and is not stored in source code.

## Security

Credentials and environment-specific configuration should never be committed to Git.

The repository ignores local and generated files such as:

```text
.env
venv/
__pycache__/
logs/
Artifacts/
```

## Disclaimer

This project is intended for learning and demonstration of an end-to-end machine learning and MLOps workflow for network security classification. It should not be treated as a production-grade security detection system without additional validation, monitoring, and security hardening.
