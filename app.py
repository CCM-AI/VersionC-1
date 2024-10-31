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
                "Goal": ["> 80%", "< 2/year"],
                "Time Frame": ["6 months", "Ongoing"],
                "Monitoring": ["Monthly", "Every 3 months"],
                "Notes": [
                    "- Stop smoking and avoid triggers.\n"
                    "- Participate in pulmonary rehabilitation.\n"
                ]
            }
        else:
            data = {
                "Target": ["FEV1"],
                "Goal": ["> 70%"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Biannual"],
                "Notes": [
                    "- Continue avoiding smoking and pollutants.\n"
                    "- Maintain a healthy diet to support lung health.\n"
                ]
            }

    elif condition == "Asthma":
        if risk == "High":
            data = {
                "Target": ["Symptom Control", "Medication Adherence"],
                "Goal": ["< 2 days/week", "100%"],
                "Time Frame": ["Ongoing", "Ongoing"],
                "Monitoring": ["Monthly", "Monthly"],
                "Notes": [
                    "- Use your rescue inhaler as prescribed.\n"
                    "- Identify and avoid asthma triggers.\n"
                ]
            }
        else:
            data = {
                "Target": ["Symptom Control"],
                "Goal": ["< 2 uses/week"],
                "Time Frame": ["Ongoing"],
                "Monitoring": ["Every 3-6 months"],
                "Notes": [
                    "- Keep your inhaler with you at all times.\n"
                    "- Practice breathing exercises daily.\n"
                ]
            }

    return pd.DataFrame(data)

# Video library data (simplified for demonstration)
video_library = [
    {"Title": "Understanding Cardiovascular Disease", "URL": "https://www.example.com/video1"},
    {"Title": "Managing Diabetes Effectively", "URL": "https://www.example.com/video2"},
    {"Title": "COPD Management Strategies", "URL": "https://www.example.com/video3"},
    {"Title": "Asthma Action Plan", "URL": "https://www.example.com/video4"},
]

# Streamlit UI
def main():
    st.title("Chronic Disease Risk Assessment Tool")

    # Create tabs for each functionality
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan"])

    # Cardiovascular Risk Assessment
    with tab1:
        st.header("Cardiovascular Risk Assessment")
        age = st.number_input("Age", min_value=18, max_value=120, value=50)
        systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)
        cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=150, max_value=300, value=200)
        smoker = st.checkbox("Smoker")

        if st.button("Calculate Cardiovascular Risk"):
            cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
            st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
            st.write(ai_assistant_response("Cardiovascular", cardio_risk))

    # Diabetes Risk Assessment
    with tab2:
        st.header("Diabetes Risk Assessment")
        bmi = st.number_input("BMI", min_value=10, max_value=60, value=25)
        family_history = st.checkbox("Family History of Diabetes")
        fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=60, max_value=300, value=100)
        hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=14.0, value=5.7)

        if st.button("Calculate Diabetes Risk"):
            diabetes_risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
            st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
            st.write(ai_assistant_response("Diabetes", diabetes_risk))

    # COPD Risk Assessment
    with tab3:
        st.header("COPD Risk Assessment")
        smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=100, value=10)
        fev1 = st.number_input("FEV1 (%)", min_value=0, max_value=100, value=80)
        exacerbations_last_year = st.number_input("Exacerbations Last Year", min_value=0, max_value=20, value=0)

        if st.button("Calculate COPD Risk"):
            copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
            st.write(f"**COPD Risk Level**: {copd_risk}")
            st.write(ai_assistant_response("COPD", copd_risk))

    # Asthma Risk Assessment
    with tab4:
        st.header("Asthma Risk Assessment")
        frequency_of_symptoms = st.number_input("Days with Symptoms per Week", min_value=0, max_value=7, value=2)
        nighttime_symptoms = st.number_input("Nighttime Symptoms per Month", min_value=0, max_value=30, value=1)
        inhaler_use = st.number_input("Rescue Inhaler Uses per Week", min_value=0, max_value=20, value=1)
        eosinophil_count = st.number_input("Eosinophil Count", min_value=0, max_value=1000, value=300)

        if st.button("Calculate Asthma Risk"):
            asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count)
            st.write(f"**Asthma Risk Level**: {asthma_risk}")
            st.write(ai_assistant_response("Asthma", asthma_risk))

    # Unified Care Plan Tab
    with tab5:
        st.header("Unified Care Plan")
        
        # Collecting results for care plan
        results = {
            "Cardiovascular": cardio_risk if 'cardio_risk' in locals() else "Not calculated",
            "Diabetes": diabetes_risk if 'diabetes_risk' in locals() else "Not calculated",
            "COPD": copd_risk if 'copd_risk' in locals() else "Not calculated",
            "Asthma": asthma_risk if 'asthma_risk' in locals() else "Not calculated"
        }

        care_plan = patient_friendly_care_plan(results)
        st.write(care_plan)

        # Displaying unified care plan table
        st.write("### Unified Care Plan Table")
        for condition, risk in results.items():
            care_plan_table = create_unified_care_plan_table(condition, risk)
            st.write(f"#### {condition} - Risk Level: {risk}")
            st.dataframe(care_plan_table)

        # Video Library Section
        st.write("### Video Library")
        st.write("Explore these resources to learn more about managing chronic diseases:")
        for video in video_library:
            st.markdown(f"- [{video['Title']}]({video['URL']})")

# Run the Streamlit app
if __name__ == "__main__":
    main()
