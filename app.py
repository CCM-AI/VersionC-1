import streamlit as st
import pandas as pd

# Sample risk calculation functions (to be implemented according to your guidelines)
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    if smoker and systolic_bp > 140:
        return "High"
    return "Moderate"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c):
    if fasting_glucose > 126 or hba1c > 6.5:
        return "High"
    return "Moderate"

def calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year):
    if smoking_years > 20 and exacerbations_last_year > 2:
        return "High"
    return "Moderate"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count):
    if frequency_of_symptoms > 4 or nighttime_symptoms > 2:
        return "High"
    return "Moderate"

# AI Assistant Function
def ai_assistant_response(condition, risk):
    responses = []

    if condition == "Cardiovascular":
        if risk == "High":
            responses.append(
                "### Cardiovascular Risk Management\n"
                "- **Management**: Make heart-healthy lifestyle changes such as a balanced diet, regular exercise, and possibly medication.\n"
                "- **Goals**: Target a blood pressure below 130/80 mmHg and LDL cholesterol below 100 mg/dL within 6 months.\n"
                "- **Avoid**: Smoking and high sodium foods.\n"
                "- **Monitoring**: Check blood pressure and cholesterol every 3 months.\n"
                "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)\n"
            )
        else:
            responses.append(
                "### Cardiovascular Risk Management\n"
                "- **Management**: Encourage healthy lifestyle choices.\n"
                "- **Goals**: Maintain blood pressure under 140/90 mmHg.\n"
                "- **Monitoring**: Annual check-ups.\n"
            )

    elif condition == "Diabetes":
        if risk == "High":
            responses.append(
                "### Diabetes Risk Management\n"
                "- **Management**: Follow a structured diabetes plan with dietary changes, regular monitoring, and possibly medication.\n"
                "- **Goals**: Aim for an HbA1c level below 7% within 3 months.\n"
                "- **Avoid**: Sugary foods and a sedentary lifestyle.\n"
                "- **Monitoring**: Follow-up every 3 months.\n"
                "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)\n"
            )
        else:
            responses.append(
                "### Diabetes Risk Management\n"
                "- **Management**: Continue healthy habits and monitor regularly.\n"
                "- **Goals**: Aim for an HbA1c below 8% annually.\n"
                "- **Monitoring**: Regular glucose checks.\n"
            )

    elif condition == "COPD":
        if risk == "High":
            responses.append(
                "### COPD Risk Management\n"
                "- **Management**: Start smoking cessation and pulmonary rehabilitation.\n"
                "- **Goals**: Improve FEV1 by at least 5% in 6 months.\n"
                "- **Avoid**: Smoking and air pollutants.\n"
                "- **Monitoring**: Follow-ups every 1-3 months.\n"
                "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)\n"
            )
        else:
            responses.append(
                "### COPD Risk Management\n"
                "- **Management**: Encourage smoking cessation and bronchodilator use.\n"
                "- **Goals**: Maintain FEV1 above 70%.\n"
                "- **Monitoring**: Biannual lung function tests.\n"
            )

    elif condition == "Asthma":
        if risk == "High":
            responses.append(
                "### Asthma Risk Management\n"
                "- **Management**: Ensure proper medication use and adherence.\n"
                "- **Goals**: Control symptoms to less than 2 days/week and no nighttime awakenings.\n"
                "- **Avoid**: Allergens and tobacco smoke.\n"
                "- **Monitoring**: Check control every 1-3 months.\n"
                "- **Resources**: [AAFA Guidelines](https://www.aafa.org)\n"
            )
        else:
            responses.append(
                "### Asthma Risk Management\n"
                "- **Management**: Reinforce adherence to your asthma plan.\n"
                "- **Goals**: Maintain less than 2 uses of rescue inhaler/week.\n"
                "- **Monitoring**: Every 3-6 months check-up.\n"
            )

    return "\n\n".join(responses)

# Function to create patient-friendly care plans
def patient_friendly_care_plan(results):
    care_plan = []

    for condition, risk in results.items():
        care_steps = f"### Care Plan for {condition} - Risk Level: {risk}\n"
        
        if risk == "High":
            care_steps += (
                "- **Step 1**: Schedule an appointment with your healthcare provider within the next week.\n"
                "- **Step 2**: Start a heart-healthy diet focusing on fruits, vegetables, and whole grains.\n"
                "- **Step 3**: Aim for at least 150 minutes of moderate exercise each week.\n"
                "- **Step 4**: Monitor your health indicators (like blood pressure) as advised.\n"
                "- **Step 5**: Join a support group for motivation and guidance.\n"
            )
        elif risk == "Moderate":
            care_steps += (
                "- **Step 1**: Schedule a follow-up appointment within the next month.\n"
                "- **Step 2**: Continue a balanced diet and stay active.\n"
                "- **Step 3**: Aim for at least 30 minutes of exercise most days.\n"
                "- **Step 4**: Keep track of your symptoms and report any changes.\n"
                "- **Step 5**: Educate yourself about your condition using reliable resources.\n"
            )
        
        care_plan.append(care_steps)

    return "\n\n".join(care_plan)

# Function to create a unified care plan table
def create_unified_care_plan_table(condition, risk):
    if condition == "Cardiovascular":
        if risk == "High":
            data = {
                "Target": ["Blood Pressure", "LDL Cholesterol", "Physical Activity"],
                "Goal": ["< 130/80 mmHg", "< 100 mg/dL", "150 minutes/week"],
                "Time Frame": ["6 months", "6 months", "Ongoing"],
                "Monitoring": ["Every 3 months", "Every 3 months", "Weekly check-ins"],
                "Notes": [
                    "- Eat more fruits and vegetables daily.\n"
                    "- Reduce salt and saturated fat intake.\n"
                    "- Schedule 30-minute walks, 5 days a week.\n",
                    "- Include healthy fats like avocado and nuts.\n"
                    "- Choose whole grains over refined ones.\n",
                    "- Track weekly activity using a journal or app.\n"
                ]
            }
        else:
            data = {
                "Target": ["Blood Pressure", "Physical Activity"],
                "Goal": ["< 140/90 mmHg", "30 minutes/day"],
                "Time Frame": ["Ongoing", "Ongoing"],
                "Monitoring": ["Annually", "Weekly check-ins"],
                "Notes": [
                    "- Maintain a balanced diet with whole foods.\n"
                    "- Limit processed foods and sugar intake.\n",
                    "- Incorporate light exercises like walking or cycling.\n"
                ]
            }

    elif condition == "Diabetes":
        if risk == "High":
            data = {
                "Target": ["HbA1c", "Fasting Glucose", "Physical Activity"],
                "Goal": ["< 7%", "< 126 mg/dL", "150 minutes/week"],
                "Time Frame": ["3 months", "3 months", "Ongoing"],
                "Monitoring": ["Every 3 months", "Every 3 months", "Weekly check-ins"],
                "Notes": [
                    "- Follow a diabetes meal plan focusing on low GI foods.\n"
                    "- Measure blood sugar before meals.\n",
                    "- Engage in regular moderate exercise like brisk walking.\n"
                ]
            }
        else:
            data = {
                "Target": ["HbA1c", "Physical Activity"],
                "Goal": ["< 8%", "30 minutes/day"],
                "Time Frame": ["Annual", "Ongoing"],
                "Monitoring": ["Annually", "Weekly check-ins"],
                "Notes": [
                    "- Continue healthy eating habits, including whole grains.\n"
                    "- Stay active with activities you enjoy, like dancing.\n"
                ]
            }

    elif condition == "COPD":
        if risk == "High":
            data = {
                "Target": ["FEV1", "Exacerbations"],
                "Goal": ["> 70%", "< 2 per year"],
                "Time Frame": ["Ongoing", "Ongoing"],
                "Monitoring": ["Every 1-3 months", "Every visit"],
                "Notes": [
                    "- Avoid smoking and secondhand smoke.\n"
                    "- Use inhalers as prescribed and track usage.\n"
                ]
            }
        else:
            data = {
                "Target": ["FEV1"],
                "Goal": ["> 60%"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Biannually"],
                "Notes": [
                    "- Continue avoiding triggers that worsen symptoms.\n"
                    "- Perform breathing exercises regularly.\n"
                ]
            }

    elif condition == "Asthma":
        if risk == "High":
            data = {
                "Target": ["Symptom Control", "Inhaler Technique"],
                "Goal": ["< 2 days/week", "100% adherence"],
                "Time Frame": ["Ongoing", "Ongoing"],
                "Monitoring": ["Every 1-3 months", "At each visit"],
                "Notes": [
                    "- Review and practice inhaler technique regularly.\n"
                    "- Avoid known allergens and triggers.\n"
                ]
            }
        else:
            data = {
                "Target": ["Symptom Control"],
                "Goal": ["< 2 uses/week"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Every 3-6 months"],
                "Notes": [
                    "- Ensure you have an asthma action plan.\n"
                    "- Engage in regular physical activity with precautions.\n"
                ]
            }

    return pd.DataFrame(data)

# Streamlit Application Layout
st.title("Chronic Disease Risk Assessment and Care Plan")

# Risk Assessment Inputs
st.sidebar.header("Input Patient Information")

age = st.sidebar.number_input("Age", min_value=1, max_value=120)
systolic_bp = st.sidebar.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=250)
smoker = st.sidebar.selectbox("Smoker?", ("Yes", "No"))
cholesterol = st.sidebar.number_input("Cholesterol Level (mg/dL)", min_value=100, max_value=400)

bmi = st.sidebar.number_input("BMI", min_value=10, max_value=60)
family_history = st.sidebar.selectbox("Family History of Diabetes?", ("Yes", "No"))
fasting_glucose = st.sidebar.number_input("Fasting Glucose (mg/dL)", min_value=60, max_value=300)
hba1c = st.sidebar.number_input("HbA1c (%)", min_value=4, max_value=15)

smoking_years = st.sidebar.number_input("Years of Smoking", min_value=0, max_value=100)
fev1 = st.sidebar.number_input("FEV1 (%)", min_value=0, max_value=100)
exacerbations_last_year = st.sidebar.number_input("Exacerbations Last Year", min_value=0, max_value=20)

frequency_of_symptoms = st.sidebar.number_input("Asthma Symptoms Frequency (per week)", min_value=0, max_value=20)
nighttime_symptoms = st.sidebar.number_input("Nighttime Symptoms (per month)", min_value=0, max_value=20)
inhaler_use = st.sidebar.number_input("Inhaler Use (per week)", min_value=0, max_value=20)
eosinophil_count = st.sidebar.number_input("Eosinophil Count", min_value=0, max_value=100)

if st.sidebar.button("Assess Risk"):
    # Calculate risks
    cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Yes", cholesterol)
    diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose, hba1c)
    copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
    asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)

    risks = {
        "Cardiovascular": cardio_risk,
        "Diabetes": diabetes_risk,
        "COPD": copd_risk,
        "Asthma": asthma_risk
    }

    # Display results
    st.subheader("Risk Assessment Results")
    for condition, risk in risks.items():
        st.write(f"{condition}: {risk}")

    # AI Assistant Care Recommendations
    st.subheader("AI Assistant Recommendations")
    response = ai_assistant_response("Cardiovascular", cardio_risk)
    response += "\n\n" + ai_assistant_response("Diabetes", diabetes_risk)
    response += "\n\n" + ai_assistant_response("COPD", copd_risk)
    response += "\n\n" + ai_assistant_response("Asthma", asthma_risk)
    st.markdown(response)

    # Unified Care Plan
    st.subheader("Unified Care Plan")
    care_plan = patient_friendly_care_plan(risks)
    st.markdown(care_plan)

    # Unified Care Plan Table
    st.subheader("Unified Care Plan Table")
    for condition, risk in risks.items():
        st.write(f"**{condition} - Risk Level: {risk}**")
        care_plan_df = create_unified_care_plan_table(condition, risk)
        st.dataframe(care_plan_df)

    # Resources for Unified Care Plan
    st.subheader("Patient Education Resources")
    st.markdown(
        """
        - [Keep your asthma-controlled](https://www.youtube.com/shorts/SqG13EtRIAo)  
        - [Check inhalers use technique](https://www.youtube.com/watch?v=2dVnDkpymYk)  
        - [Risk factors for cardiovascular disease](https://www.youtube.com/watch?v=SRioi_6Yh18)  
        - [Keep your diabetes under control](https://www.youtube.com/watch?feature=shared&v=qG3OyONVbEQ)  
        - [Physical activity](https://www.youtube.com/watch?feature=shared&v=IF8IEj8Rzvg)  
        - [Diet](https://www.youtube.com/watch?v=c5Cgmwi-oRI)  
        - [Hypertension](https://www.youtube.com/watch?feature=shared&v=NG17qcXYxYQ)  
        - [Smoking](https://www.youtube.com/watch?feature=shared&v=24eovpnitPk)  
        - [High cholesterol](https://www.youtube.com/watch?feature=shared&v=G3AIYdJdfDk)  
        - [Stress](https://www.youtube.com/watch?feature=shared&v=QODuDQwsJ80)  
        - [Maintain healthy weight](https://www.youtube.com/watch?feature=shared&v=_ZtgTotfAfQ)  
        """
    )
