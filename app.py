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
                "Monitoring": ["Every 1-3 months", "Every 1-3 months"],
                "Notes": [
                    "- Join a pulmonary rehabilitation program.\n"
                    "- Follow a prescribed medication regimen.\n"
                ]
            }
        else:
            data = {
                "Target": ["FEV1"],
                "Goal": ["> 70%"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Biannually"],
                "Notes": [
                    "- Maintain an active lifestyle as tolerated.\n"
                    "- Avoid respiratory irritants.\n"
                ]
            }

    elif condition == "Asthma":
        if risk == "High":
            data = {
                "Target": ["Symptom Frequency", "PEF"],
                "Goal": ["< 2 times/week", "> 80% predicted"],
                "Time Frame": ["Ongoing", "Ongoing"],
                "Monitoring": ["Monthly", "Monthly"],
                "Notes": [
                    "- Ensure proper inhaler technique.\n"
                    "- Create an asthma action plan with your healthcare provider.\n"
                ]
            }
        else:
            data = {
                "Target": ["Symptom Frequency"],
                "Goal": ["< 1 time/week"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Monthly"],
                "Notes": [
                    "- Continue to monitor symptoms and medication use.\n"
                    "- Follow up as needed with your doctor.\n"
                ]
            }

    df = pd.DataFrame(data)
    return df

# Function to get numeric input with error handling
def get_numeric_input(label, min_value, max_value, value, key):
    try:
        return st.number_input(label, min_value=min_value, max_value=max_value, value=value, key=key)
    except ValueError as e:
        st.error(f"Invalid input for {label}: {e}")
        return None

# User Inputs
st.title("Chronic Disease Risk Assessment")
st.write("Assess your risk for chronic diseases.")

# Cardiovascular Risk Inputs
st.subheader("Cardiovascular Risk Assessment")
age = get_numeric_input("Age (years)", 18, 120, 50, key="cv_age")
systolic_bp = get_numeric_input("Systolic Blood Pressure (mmHg)", 80, 300, 120, key="cv_sbp")
smoker = st.selectbox("Are you a smoker?", ("No", "Yes"), key="cv_smoker") == "Yes"
cholesterol = get_numeric_input("Cholesterol (mg/dL)", 100, 400, 200, key="cv_chol")

# Calculate and display cardiovascular risk
if age and systolic_bp and cholesterol:
    cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
    st.write(f"Your cardiovascular risk is: **{cardio_risk}**")

# Diabetes Risk Inputs
st.subheader("Diabetes Risk Assessment")
bmi = get_numeric_input("BMI (kg/m²)", 10, 50, 25, key="diabetes_bmi")
family_history = st.selectbox("Family history of diabetes?", ("No", "Yes"), key="diabetes_family_history") == "Yes"
fasting_glucose = get_numeric_input("Fasting Glucose (mg/dL)", 50, 300, 100, key="diabetes_fasting_glucose")
hba1c = get_numeric_input("HbA1c (%)", 4.0, 14.0, 5.0, key="diabetes_hba1c")

# Calculate and display diabetes risk
if bmi and fasting_glucose and hba1c:
    diabetes_risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
    st.write(f"Your diabetes risk is: **{diabetes_risk}**")

# COPD Risk Inputs
st.subheader("COPD Risk Assessment")
smoking_years = get_numeric_input("Years of Smoking", 0, 100, 20, key="copd_smoking_years")
age_copd = get_numeric_input("Age (years)", 18, 120, 50, key="copd_age")
fev1 = get_numeric_input("FEV1 (L)", 0.1, 8.0, 3.0, key="copd_fev1")
exacerbations_last_year = get_numeric_input("Exacerbations Last Year", 0, 100, 1, key="copd_exacerbations")

# Calculate and display COPD risk
if smoking_years and age_copd and fev1 and exacerbations_last_year:
    copd_risk = calculate_copd_risk(smoking_years, age_copd, fev1, exacerbations_last_year)
    st.write(f"Your COPD risk is: **{copd_risk}**")

# Asthma Risk Inputs
st.subheader("Asthma Risk Assessment")
frequency_of_symptoms = get_numeric_input("Frequency of Symptoms (times/week)", 0, 20, 2, key="asthma_symptoms")
nighttime_symptoms = get_numeric_input("Nighttime Symptoms (times/month)", 0, 30, 1, key="asthma_nighttime")
inhaler_use = get_numeric_input("Inhaler Use (times/month)", 0, 50, 5, key="asthma_inhaler_use")
eosinophil_count = get_numeric_input("Eosinophil Count (cells/µL)", 0, 1000, 300, key="asthma_eosinophil")

# Calculate and display asthma risk
if frequency_of_symptoms and nighttime_symptoms and inhaler_use and eosinophil_count:
    asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)
    st.write(f"Your asthma risk is: **{asthma_risk}**")

# Collecting all results
results = {
    "Cardiovascular": cardio_risk if 'cardio_risk' in locals() else None,
    "Diabetes": diabetes_risk if 'diabetes_risk' in locals() else None,
    "COPD": copd_risk if 'copd_risk' in locals() else None,
    "Asthma": asthma_risk if 'asthma_risk' in locals() else None
}

# Display AI Assistant Response
st.subheader("AI Assistant Recommendations")
for condition, risk in results.items():
    if risk:
        response = ai_assistant_response(condition, risk)
        st.markdown(response)

# Display Patient-Friendly Care Plan
st.subheader("Patient-Friendly Care Plans")
care_plan = patient_friendly_care_plan(results)
st.markdown(care_plan)

# Create a Unified Care Plan Table
st.subheader("Unified Care Plan")
for condition, risk in results.items():
    if risk:
        care_plan_df = create_unified_care_plan_table(condition, risk)
        st.write(f"**{condition} - Risk Level: {risk}**")
        st.dataframe(care_plan_df)

