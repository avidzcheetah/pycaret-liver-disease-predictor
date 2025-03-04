# Liver Disease Prediction Using PyCaret

This project demonstrates how to predict liver disease using the PyCaret machine learning library. Developed as part of the Udemy course **"Machine Learning Projects for Healthcare,"** the project uses clinical data to build, tune, and evaluate models that can help identify patients at risk of chronic liver disease.

---

## Overview

### Objective
Predict liver disease in patients based on clinical and biochemical parameters using PyCaret. The model helps reduce the burden on doctors by automating the prediction process.

### Background
Chronic liver disease (CLD) is the progressive deterioration of liver functions over more than six months. It results from factors such as alcohol abuse, toxins, infections, and genetic/metabolic disorders. It is only when over 75% of liver tissue is affected that the organ’s functionality starts to decline noticeably.

---

## Dataset

### Description
The dataset consists of 554 records:
- 416 records of liver patients
- 167 records of non-liver patients

### Features
- **Age** (patients above 89 are recorded as 90)
- **Gender**
- **Total Bilirubin**
- **Direct Bilirubin**
- **Alkaline Phosphotase**
- **Alamine Aminotransferase**
- **Aspartate Aminotransferase**
- **Total Proteins**
- **Albumin**
- **Albumin and Globulin Ratio**

**Target**: A class label indicating the presence (liver patient) or absence (non-liver patient) of liver disease.

---

## Project Workflow

### Data Preparation
- Importing and reading the dataset using Pandas.
- Preprocessing includes handling missing values (imputed using the mean for numeric features and constant for categorical features), encoding categorical variables, and splitting the data into training and testing sets via PyCaret’s `setup` function.

### Model Development with PyCaret
- Initializing the environment using PyCaret’s classification module.
- Training multiple models using the `create_model` function (a Logistic Regression model is used as an example).
- Tuning hyperparameters using the `tune_model` function.
- Comparing models with evaluation metrics such as **Accuracy, AUC, Recall, Precision, F1,** and **Kappa**.

### Model Prediction
- Using the best-performing model to predict liver disease on the test set.

---

## Installation & Setup

### Prerequisites
- Python 3.x
- Pandas
- PyCaret

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/liver-disease-prediction.git
cd liver-disease-prediction
```

Create a `requirements.txt` file (if not provided) with:
```text
pandas
pycaret
```

Then run:
```bash
pip install -r requirements.txt
```

---

## How to Run

### Launch the Notebook or Script

For Jupyter Notebook:
```bash
jupyter notebook liver_disease_prediction.ipynb
```

For Python script:
```bash
python liver_disease_prediction.py
```

---

## Project Code Example

```python
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from pycaret.classification import setup, create_model, tune_model, compare_models, predict_model

# Load the dataset
dataset = pd.read_csv("indian_liver_patient.csv")
print(dataset.head())

# Set up the PyCaret environment
exp = setup(data=dataset, target='Dataset', session_id=123, fold=10, silent=True)

# Create a Logistic Regression model
lr = create_model('lr')
tuned_lr = tune_model(lr)

# Compare models
best_model = compare_models()

# Predict on the test set
predictions = predict_model(best_model)
print(predictions)
```

---

## Project Structure

| File/Folder                                               | Description                                                                                           |
|------------------------------------------------|---------------------------------------------------------------------------------------------------|
| README.md                                                | Project overview and instructions                                                           |
| PyCaret_Liver_Disease_prediction.ipynb   | Jupyter Notebook covering data visualization, preprocessing, model training, etc. |
| Model+Deployment.ipynb                         | Jupyter Notebook for model deployment steps                                       |
| app.py                                                    | Python script for running the deployment using Streamlit        |
| classifier.pkl                                              | Saved trained model file                                                                        |
| indian_liver_patient.csv                              | Dataset file containing clinical records for liver disease prediction                    |
| Problem+Statement+-+Liver+Disease+prediction+by+using+Pycaret+-+ML+Project.pdf | Project problem statement and description document                |
| Chronic+Liver+Disease+-+Information.pdf  | Additional reference document related to chronic liver disease                    |

---

## Results

The project evaluates several models based on key metrics. The results indicate that the model comparison, built using PyCaret, helps select the best performing classifier (e.g., Extra Trees Classifier, Logistic Regression, among others) to effectively predict liver disease.

---

## Future Work

- Expand the dataset with more diverse features.
- Integrate additional data preprocessing steps.
- Experiment with ensemble methods and deep learning models.
- Optimize the deployment for real-time prediction in a healthcare environment.

---

## Acknowledgements

This project is part of the Udemy course **“Machine Learning Projects for Healthcare.”** Clinical insights on chronic liver disease and its symptoms were incorporated to provide a comprehensive understanding of the condition, emphasizing the importance of early prediction.

---

This README provides you with detailed instructions and a clear overview of the project for easy setup and reproducibility. Happy coding!
