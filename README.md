# customer-churn-mlops-project

🗓️ Timeline to Hit the Deadline (Aug 30, 2025, 1:00 PM CT)
| Date               | Task                               |
| ------------------ | ---------------------------------- |
| **Aug 25–26**      | Dataset download, EDA, cleaning    |
| **Aug 26**         | Model training and evaluation      |
| **Aug 26-27**      | Flask app + Dockerization          |
| **Aug 29 AM**      | CI/CD pipeline + Heroku deployment |
| **Aug 29 PM**      | SageMaker + Kubernetes deployment  |
| **Aug 30 Morning** | Final demo prep, schedule Zoom     |


✅ Deliverables

 GitHub repo with clean code & organized folders
 
 README.md with project explanation
 
 .ipynb and .pkl files
 
 Flask app and Docker container
 
 CI/CD pipeline and live Heroku app
 
 SageMaker notebook or screenshot
 
 Kubernetes YAML files
 
 Scheduled Zoom demo


📁 Folder Structure (For GitHub Repository)

 customer-churn-mlops-project/
 
│

├── data/

│   └── Telco-Customer-Churn-prepared.csv             # Prepared dataset (add to .gitignore if too large)

│

├── notebooks/

│   └── ANA-680_FinalProject_EDA_8-30-2025.ipynb      # EDA, cleaning, feature engineering

│   └── ANA-680_FinalProject_Model_8-30-2025.ipynb    # Training, validation, metrics

│

├── models/

│   └── churn_model.pkl                     # Trained ML model

│   └── scaler.pkl 

│

├── app/

│   ├── app.py                              # Flask application

│   ├── templates/

│   │   └── index.html                      # HTML form for predictions

│   └── static/                             # (Optional) CSS, JS files

|   │   └── style.css                       # Style CSS for HTML form

│   ├── Dockerfile                          # Containerize Flask app

│

├── k8s/

│   ├── deployment.yaml                     # Kubernetes deployment config

│   └── service.yaml                        # Kubernetes service config

│

├── .github/

│   └── workflows/

│       └── ci-cd.yml                       # GitHub Actions workflow for CI/CD

│

├── sagemaker/

│   └── sagemaker_notebook.ipynb           # Container-based model deployment

│

├── requirements.txt                        # Python dependencies

├── heroku.yml                              # Heroku container deployment

├── README.md                               # Project overview

└── .gitignore                              # Ignore files/folders like __pycache__, *.pkl, etc.


# 📊 Customer Churn Prediction - MLOps Project

This project predicts customer churn in a subscription-based telecom business using a machine learning pipeline deployed through modern MLOps practices. The model is built, containerized, and deployed using tools such as Flask, Docker, GitHub Actions, Heroku, AWS SageMaker, and Kubernetes.

## 🚀 Objective

To build and deploy a predictive model that identifies customers likely to churn using historical data. This empowers the business to proactively engage at-risk customers and reduce churn.

---

## 📁 Project Structure

├── data/ # Raw dataset

├── notebooks/ # Jupyter notebooks for EDA and modeling

├── model/ # Saved model (.pkl)

├── app/ # Flask app for model inference

├── docker/ # Dockerfile and containerization

├── k8s/ # Kubernetes configuration files

├── .github/workflows/ # GitHub Actions CI/CD pipeline

├── sagemaker/ # Deployment in AWS SageMaker

├── requirements.txt # Python dependencies

├── heroku.yml # Heroku deployment config

├── README.md # Project overview and instructions

---

## 📌 Dataset

- **Name:** Telco Customer Churn Dataset
- **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Type:** Tabular, ~7,000 records
- **Target:** `Churn` (Yes/No)

---

## 🔧 Technologies Used

- **Data Processing:** `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Modeling:** `scikit-learn`, `xgboost`
- **Web Framework:** `Flask`
- **Containerization:** `Docker`, `Docker Hub`
- **CI/CD:** `GitHub Actions`, `Heroku`
- **Cloud ML Platform:** `AWS SageMaker Studio Lab`
- **Orchestration:** `Kubernetes`, `kubectl`, `minikube` (or EKS)

---

## 🔁 Workflow

1. **Data Exploration & Cleaning**
2. **Model Training & Evaluation**
3. **Save Model (.pkl)**
4. **Flask App for Local Deployment**
5. **Containerize with Docker**
6. **CI/CD Pipeline to Heroku using GitHub Actions**
7. **Redeploy using AWS SageMaker Studio Lab**
8. **Deploy with Kubernetes Cluster**
9. **Live Demonstration via Zoom**

---

## 🧪 CI/CD Pipeline

- CI/CD is handled using **GitHub Actions**
- On every push to `main`, the model is tested, containerized, and deployed to **Heroku**
- Configuration is available in `.github/workflows/ci-cd.yml`

---

## ☁️ Cloud & Container Tools

| Tool       | Use Case                        |
|------------|----------------------------------|
| Docker     | Containerizing Flask application |
| Docker Hub | Image hosting                    |
| Heroku     | App deployment (via CI/CD)       |
| SageMaker  | Model deployment in AWS          |
| Kubernetes | Scalable app deployment          |

---

## 🧠 Model Performance

> *To be updated after model training...*

- Accuracy: `--%`
- Precision: `--%`
- Recall: `--%`
- AUC: `--`

---

## 📞 Demo & Contact

A live demonstration will be scheduled with the instructor to walk through:

- Flask model inference
- Containerized deployment
- CI/CD pipeline
- AWS SageMaker & Kubernetes deployment

📅 **Deadline:** Saturday, August 30, 2025 – 1:00 PM CT  
📹 **Zoom Demo:** _To be scheduled_

---

## ✅ To-Do Checklist

- [x] Select dataset & define problem
- [ ] Perform EDA and data prep
- [ ] Train and evaluate model
- [ ] Build and test Flask app
- [ ] Containerize app using Docker
- [ ] Set up CI/CD and deploy on Heroku
- [ ] Redeploy via SageMaker
- [ ] Deploy with Kubernetes
- [ ] Final demo

---

## 👨‍💻 Author

- **Randall Crawford**
- [GitHub Profile](https://github.com/RCC0149/customer-churn-mlops-project)
- **Email:** rcc_0149@yahoo.com

