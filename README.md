# Bioactivity Prediction of Chemical Compounds Against Cyclooxygenase-2(COX-2) Using Machine Learning with Python

## Overview
This project focuses on predicting the bioactivity of chemical compounds against Cyclooxygenase-2 (COX-2), an enzyme implicated in inflammation and various diseases. The goal is to develop a machine learning model that can accurately classify compounds as active or inactive COX-2 inhibitors, streamlining the early stages of drug discovery. The project leverages cheminformatics tools, Python-based machine learning, and a user-friendly web interface for predictions.



## Problem Statement
Traditional drug discovery methods for COX-2 inhibitors are time-consuming, costly, and often yield compounds with undesirable side effects. This project addresses these challenges by:
- Reducing reliance on wet-lab experiments through computational predictions.
- Providing a user-friendly tool for researchers without extensive coding experience.
- Identifying potential COX-2 inhibitors with fewer side effects using machine learning.



## Methodology
The project follows a structured pipeline from data collection to model deployment:

### 1. Data Collection and Preprocessing
- **Data Source**: Curated bioactivity data for COX-2 (Target ID: CHEMBL230) was extracted from the ChEMBL database.
- **Preprocessing**:
  - Removed rows with missing values.
  - Binarized activity labels: Compounds with IC50 < 10,000 nM were labeled as "active," others as "inactive."
  - Retained essential columns: `molecule_chembl_id`, `SMILES`, `standard_value (IC50)`, and `bioactivity_class`.

### 2. Molecular Descriptor Calculation
- **Tools**: RDKit was used to compute six key molecular descriptors:
  - Molecular Weight (`MolWt`)
  - LogP (lipophilicity)
  - Hydrogen Bond Donors (`HDonors`)
  - Hydrogen Bond Acceptors (`HAcceptors`)
  - Topological Polar Surface Area (`TPSA`)
  - Number of Rotatable Bonds (`NumRotatableBonds`).
- **Quality Control**: Rows with invalid or missing descriptors were identified and excluded.

### 3. Machine Learning Model Training
- **Algorithm**: XGBoost (Extreme Gradient Boosting) was selected for its robustness in handling imbalanced datasets and non-linear relationships.
- **Data Splitting**: The dataset was split into 80% training and 20% testing sets, with stratification to maintain class distribution.
- **Class Imbalance Handling**: SMOTE-Tomek resampling was applied to balance the training data.
- **Feature Scaling**: StandardScaler was used to normalize input features.
- **Model Evaluation**: Performance was assessed using accuracy, ROC-AUC, precision, recall, and F1-score. A confusion matrix and feature importance analysis were also generated.

### 4. Web Application Deployment
- **Tool**: Streamlit was used to create an interactive web app.
- **Features**:
  - Input interface for SMILES strings.
  - Real-time descriptor calculation and bioactivity prediction.
  - Visualization of molecular structures and prediction confidence scores.

![web app-](https://github.com/AkhilT044/ML_Bioactivity_Pediction_CYCLOGENASE-2/blob/main/WebApp.png)


## Results and Validation
- The trained XGBoost model achieved high accuracy in classifying COX-2 inhibitors.
- Validation was performed using known natural COX-2 inhibitors (e.g., Senkyunolide I, Cryptotanshinone, Roburic acid), and the model correctly predicted their activity.
- Key insights from feature importance analysis highlighted molecular descriptors critical for COX-2 inhibition.



## Key Features
- **Data-Driven Approach**: Utilized experimentally validated bioactivity data from ChEMBL.
- **Interpretability**: Feature importance analysis provides insights into molecular properties influencing bioactivity.
- **User-Friendly Interface**: The Streamlit app enables researchers to make predictions without coding expertise.
- **Scalability**: The methodology can be adapted for other drug targets.



## Future Work
- **Expand Descriptors**: Incorporate 3D molecular descriptors and docking scores for enhanced accuracy.
- **Advanced Models**: Explore deep learning techniques like graph neural networks for improved predictions.
- **Experimental Validation**: Collaborate with labs to test top predicted compounds in vitro.
- **Multi-Target Predictions**: Extend the model to predict activity against multiple biological targets.



## How to Use
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AkhilT044/ML_Bioactivity_Pediction_CYCLOGENASE-2.git
   cd ML_Bioactivity_Pediction_CYCLOGENASE-2
   ```

2. **Set Up the Environment**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

4. **Input SMILES Strings**: Use the web interface to input SMILES strings of compounds and view predictions.


