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
                "- **Risk Factors for Cardiovascular Disease**: [Watch Video](https://www.youtube.com/watch?v=SRioi_6Yh18)\n"
                "- **Maintain Healthy Weight**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=_ZtgTotfAfQ)\n"
                "- **Physical Activity**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=IF8IEj8Rzvg)\n"
                "- **Diet**: [Watch Video](https://www.youtube.com/watch?v=c5Cgmwi-oRI)\n"
                "- **Hypertension**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=NG17qcXYxYQ)\n"
                "- **Smoking Cessation**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=24eovpnitPk)\n"
                "- **Cholesterol Management**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=G3AIYdJdfDk)\n"
                "- **Managing Stress**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=QODuDQwsJ80)\n"
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
                "- **Keep Your Diabetes Under Control**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=qG3OyONVbEQ)\n"
                "- **Physical Activity**: [Watch Video](https://www.youtube.com/watch?feature=shared&v=IF8IEj8Rzvg)\n"
                "- **Diet**: [Watch Video](https://www.youtube.com/watch?v=c5Cgmwi-oRI)\n"
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
                "- **Keep Your Asthma Controlled**: [Watch Video](https://www.youtube.com/shorts/SqG13EtRIAo)\n"
                "- **Check Inhaler Use Technique**: [Watch Video](https://www.youtube.com/watch?v=2dVnDkpymYk)\n"
            )
        else:
            responses.append(
                "### Asthma Risk Management\n"
                "- **Management**: Reinforce adherence to your asthma plan.\n"
                "- **Goals**: Maintain less than 2 uses of rescue inhaler/week.\n"
                "- **Monitoring**: Every 3-6 months check-up.\n"
            )

    return "\n\n".join(responses)

# Rest of the code is the same, with `ai_assistant_response` invoked in each condition section to display risk management steps.

# Educational Resources Section
st.write("---")
st.header("Educational Resources")
st.write("Here are some trusted resources for chronic disease management:")
st.write("- [American Diabetes Association (ADA)](https://www.diabetes.org)")
st.write("- [American Heart Association (AHA)](https://www.heart.org)")
st.write("- [Global Initiative for Chronic Obstructive Lung Disease (GOLD)](https://goldcopd.org)")
st.write("- [Asthma and Allergy Foundation of America (AAFA)](https://www.aafa.org)")
st.write("---")
st.write("### Video Resources")
st.write("- [Keep Your Asthma Controlled](https://www.youtube.com/shorts/SqG13EtRIAo)")
st.write("- [Check Inhaler Use Technique](https://www.youtube.com/watch?v=2dVnDkpymYk)")
st.write("- [Risk Factors for Cardiovascular Disease](https://www.youtube.com/watch?v=SRioi_6Yh18)")
st.write("- [Keep Your Diabetes Under Control](https://www.youtube.com/watch?feature=shared&v=qG3OyONVbEQ)")
st.write("- [Physical Activity](https://www.youtube.com/watch?feature=shared&v=IF8IEj8Rzvg)")
st.write("- [Diet](https://www.youtube.com/watch?v=c5Cgmwi-oRI)")
st.write("- [Hypertension](https://www.youtube.com/watch?feature=shared&v=NG17qcXYxYQ)")
st.write("- [Smoking](https://www.youtube.com/watch?feature=shared&v=24eovpnitPk)")
st.write("- [High Cholesterol](https://www.youtube.com/watch?feature=shared&v=G3AIYdJdfDk)")
st.write("- [Stress Management](https://www.youtube.com/watch?feature=shared&v=QODuDQwsJ80)")
st.write("- [Maintain Healthy Weight](https://www.youtube.com/watch?feature=shared&v=_ZtgTotfAfQ)")

# Feedback Section
st.write("---")
st.header("Feedback and Support")
st.write("We value your feedback! Please let us know how we can improve this application or if you need further assistance.")
feedback = st.text_area("Your feedback here")

if st.button("Submit Feedback"):
    st.write("Thank you for your feedback!")
