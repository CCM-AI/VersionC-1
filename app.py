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
                "Monitoring": ["Every 1-3 months", "Every month"],
                "Notes": [
                    "- Avoid exposure to smoke and air pollution.\n"
                    "- Participate in pulmonary rehabilitation programs.\n"
                ]
            }
        else:
            data = {
                "Target": ["FEV1"],
                "Goal": ["> 70%"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Biannual"],
                "Notes": [
                    "- Maintain an active lifestyle with regular exercise.\n"
                    "- Avoid known triggers like dust and strong odors.\n"
                ]
            }

    elif condition == "Asthma":
        if risk == "High":
            data = {
                "Target": ["Asthma Control", "Symptoms Frequency"],
                "Goal": ["Control day symptoms", "No nighttime symptoms"],
                "Time Frame": ["Ongoing", "Ongoing"],
                "Monitoring": ["Every 1-3 months", "Monthly"],
                "Notes": [
                    "- Ensure proper inhaler technique and adherence.\n"
                    "- Identify and avoid triggers.\n"
                ]
            }
        else:
            data = {
                "Target": ["Asthma Control"],
                "Goal": ["Controlled Symptoms"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Every 3-6 months"],
                "Notes": [
                    "- Keep rescue inhaler accessible.\n"
                    "- Stay proactive about managing asthma.\n"
                ]
            }

    df = pd.DataFrame(data)
    return df

# Sidebar for navigation
st.sidebar.title("Patient Care Plan Tool")
options = ["Home", "Risk Assessment", "Unified Care Plan"]
choice = st.sidebar.radio("Select an option", options)

# Home Page
if choice == "Home":
    st.title("Patient Care Plan Tool")
    st.write(
        "Welcome to the Patient Care Plan Tool. Use this application to assess health risks "
        "and generate personalized care plans. Navigate through the options on the left."
    )

# Risk Assessment Page
elif choice == "Risk Assessment":
    st.title("Risk Assessment")
    
    st.subheader("Cardiovascular Risk Assessment")
    age = st.number_input("Enter age (years):", min_value=1, max_value=120, value=30)
    systolic_bp = st.number_input("Enter systolic blood pressure (mmHg):", min_value=50, max_value=250, value=120)
    smoker = st.radio("Are you a smoker?", ("Yes", "No"))
    cholesterol = st.number_input("Enter LDL cholesterol level (mg/dL):", min_value=0, max_value=300, value=100)
    cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Yes", cholesterol)

    st.subheader("Diabetes Risk Assessment")
    bmi = st.number_input("Enter BMI:", min_value=10.0, max_value=50.0, value=25.0)
    family_history = st.radio("Family history of diabetes?", ("Yes", "No"))
    fasting_glucose = st.number_input("Enter fasting glucose (mg/dL):", min_value=0, max_value=300, value=100)
    hba1c = st.number_input("Enter HbA1c (%):", min_value=4.0, max_value=15.0, value=5.7)
    diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose, hba1c)

    st.subheader("COPD Risk Assessment")
    smoking_years = st.number_input("Enter years of smoking:", min_value=0, max_value=100, value=10)
    fev1 = st.number_input("Enter FEV1 (% predicted):", min_value=0.0, max_value=100.0, value=80.0)
    exacerbations_last_year = st.number_input("Enter number of exacerbations last year:", min_value=0, max_value=10, value=1)
    copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)

    st.subheader("Asthma Risk Assessment")
    frequency_of_symptoms = st.number_input("Days of symptoms in the past week:", min_value=0, max_value=7, value=1)
    nighttime_symptoms = st.number_input("Nighttime symptoms in the past month:", min_value=0, max_value=30, value=0)
    inhaler_use = st.number_input("Days of rescue inhaler use in the past week:", min_value=0, max_value=7, value=1)
    eosinophil_count = st.number_input("Eosinophil count (cells/uL):", min_value=0, max_value=1000, value=300)
    asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)

    # Store results in a dictionary
    results = {
        "Cardiovascular": cardio_risk,
        "Diabetes": diabetes_risk,
        "COPD": copd_risk,
        "Asthma": asthma_risk
    }

    # AI Assistant Response
    st.subheader("AI Assistant Recommendations")
    for condition, risk in results.items():
        response = ai_assistant_response(condition, risk)
        st.markdown(response)

    # Patient Friendly Care Plan
    st.subheader("Patient Friendly Care Plan")
    care_plan = patient_friendly_care_plan(results)
    st.markdown(care_plan)

# Unified Care Plan Page
elif choice == "Unified Care Plan":
    st.title("Unified Care Plan")
    
    st.subheader("Unified Care Plan Table")
    
    condition = st.selectbox("Select a condition:", ["Cardiovascular", "Diabetes", "COPD", "Asthma"])
    risk_level = st.selectbox("Select risk level:", ["High", "Moderate"])

    care_plan_df = create_unified_care_plan_table(condition, risk_level)
    st.dataframe(care_plan_df)

    st.subheader("Video Educational Resources")
    st.write("Here are some video resources for your condition:")
    if condition == "Cardiovascular":
        st.video("https://www.youtube.com/watch?v=9T28H7sO3C0")
        st.video("https://www.youtube.com/watch?v=W2x1rS9z4Wk")
    elif condition == "Diabetes":
        st.video("https://www.youtube.com/watch?v=PHfBtbYAYBo")
        st.video("https://www.youtube.com/watch?v=4PqH9lB2cIU")
    elif condition == "COPD":
        st.video("https://www.youtube.com/watch?v=ow48T6uM1rA")
        st.video("https://www.youtube.com/watch?v=L-Wu2Y_pW0s")
    elif condition == "Asthma":
        st.video("https://www.youtube.com/watch?v=DEyJXnM30MQ")
        st.video("https://www.youtube.com/watch?v=vQUqaZJtJw8")

