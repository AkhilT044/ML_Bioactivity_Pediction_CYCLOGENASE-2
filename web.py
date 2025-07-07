import streamlit as st
import pandas as pd
import joblib
from rdkit import Chem
from rdkit.Chem import Descriptors, Draw
from PIL import Image
import io

# Set page config
st.set_page_config(
    page_title="COX-2 Inhibitor Predictor", page_icon="🧪", layout="centered"
)

# Logo image
logo = Image.open("Logo.png")
# Display logo
st.image(logo, use_container_width=True)


# Title and description
st.write("""
# Cyclooxygenase 2  Inhibitor Prediction

Predict bioactivity using molecular descriptors and machine learning.
***
""")


# Function to calculate descriptors
def calculate_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None
    return {
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "HDonors": Descriptors.NumHDonors(mol),
        "HAcceptors": Descriptors.NumHAcceptors(mol),
        "TPSA": Descriptors.TPSA(mol),
        "RotBonds": Descriptors.NumRotatableBonds(mol),
    }


# Load model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("xgb_model2.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None


model = load_model()

# User input
st.sidebar.header("User Input Features")
smiles_input = st.sidebar.text_input(
    "Enter SMILES string:",
)

if st.sidebar.button("Predict"):
    if not smiles_input:
        st.warning("Please enter a SMILES string")
    elif not model:
        st.error("Model not loaded properly")
    else:
        with st.spinner("Processing..."):
            try:
                # Calculate descriptors
                descriptors = calculate_descriptors(smiles_input)

                if not descriptors:
                    st.error("Invalid SMILES string. Please check your input.")
                else:
                    # Create DataFrame for prediction
                    input_data = pd.DataFrame([descriptors])

                    # Make prediction
                    prediction = model.predict(input_data)[0]
                    proba = model.predict_proba(input_data)[0]
                    class_name = "active" if prediction == 0 else "inactive"

                    # Display results
                    st.success("Prediction complete!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Molecular Descriptors")
                        st.write(f"- **Molecular Weight**: {descriptors['MolWt']:.2f}")
                        st.write(f"- **LogP**: {descriptors['LogP']:.2f}")
                        st.write(f"- **H-Bond Donors**: {descriptors['HDonors']}")
                        st.write(f"- **H-Bond Acceptors**: {descriptors['HAcceptors']}")
                        st.write(
                            f"- **Topological Polar Surface Area**: {descriptors['TPSA']:.2f}"
                        )
                        st.write(f"- **Rotatable Bonds**: {descriptors['RotBonds']}")

                    with col2:
                        st.subheader("Prediction Results")
                        if class_name == "active":
                            st.markdown("**Bioactivity Class**: ✅ Active")
                        else:
                            st.markdown("**Bioactivity Class**: ❌ Inactive")

                        st.write(f"**Probability**: {max(proba) * 100:.1f}%")
                        st.write("**Model**: XGBoost")

                    # Display molecule image
                    mol = Chem.MolFromSmiles(smiles_input)
                    if mol:
                        img = Draw.MolToImage(mol)
                        st.image(img, caption="Molecular Structure", width=300)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
