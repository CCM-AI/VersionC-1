# Streamlit UI Setup
st.title("Chronic Disease Risk Assessment Tool")

# Initialize session state
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Tabs for different conditions
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="cv_age")
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, key="systolic_bp")
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=150, max_value=300, value=200, key="cholesterol")
    smoker = st.checkbox("Smoker", key="smoker")

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk
        st.write(ai_assistant_response("Cardiovascular", cardio_risk))

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, key="bmi")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="diabetes_age")
    family_history = st.checkbox("Family History of Diabetes", key="family_history")
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=100, key="fasting_glucose")
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.5, key="hba1c")

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk
        st.write(ai_assistant_response("Diabetes", diabetes_risk))

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=50, value=10, key="smoking_years")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="copd_age")
    fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80, key="fev1")
    exacerbations_last_year = st.number_input("Exacerbations in Last Year", min_value=0, max_value=10, value=1, key="exacerbations")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk
        st.write(ai_assistant_response("COPD", copd_risk))

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Symptoms (0-7 days/week)", 0, 7, 2, key="frequency_of_symptoms")
    nighttime_symptoms = st.slider("Nighttime Symptoms (0-7 days/week)", 0, 7, 1, key="nighttime_symptoms")
    inhaler_use = st.slider("Inhaler Use (0-7 days/week)", 0, 7, 2, key="inhaler_use")
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80, key="fev1_asthma")
    eosinophil_count = st.number_input("Eosinophil Count (cells/μL)", min_value=0, max_value=1000, value=300, key="eosinophil_count")

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk
        st.write(ai_assistant_response("Asthma", asthma_risk))

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan")
    if st.session_state['results']:
        st.write("### Suggested Patient-Friendly Care Plan")
        patient_care_plan = patient_friendly_care_plan(st.session_state['results'])
        st.write(patient_care_plan)

        # Create a comprehensive table for the unified care plan
        st.write("### Care Plan Targets Table")
        for condition, risk in st.session_state['results'].items():
            st.write(f"#### Care Plan for {condition} - Risk Level: {risk}")
            care_plan_table = create_unified_care_plan_table(condition, risk)
            st.dataframe(care_plan_table)

# Educational Resources Section
st.write("---")
st.header("Educational Resources")
st.write("Here are some trusted resources for chronic disease management:")
st.write("- [American Diabetes Association (ADA)](https://www.diabetes.org)")
st.write("- [American Heart Association (AHA)](https://www.heart.org)")
st.write("- [Global Initiative for Chronic Obstructive Lung Disease (GOLD)](https://goldcopd.org)")
st.write("- [Asthma and Allergy Foundation of America (AAFA)](https://www.aafa.org)")

# Video Library Section
st.write("---")
st.header("Video Library")
st.write("Here are some helpful videos on chronic disease management:")
st.write("- [Check inhalers use technique](https://www.youtube.com/watch?v=2dVnDkpymYk)")
st.write("- [Risk factors for cardiovascular disease](https://www.youtube.com/watch?v=SRioi_6Yh18)")
st.write("- [Keep your diabetes under control](https://www.youtube.com/watch?feature=shared&v=qG3OyONVbEQ)")
st.write("- [Physical activity](https://www.youtube.com/watch?feature=shared&v=IF8IEj8Rzvg)")
st.write("- [Diet](https://www.youtube.com/watch?v=c5Cgmwi-oRI)")
st.write("- [Smoking](https://www.youtube.com/watch?feature=shared&v=24eovpnitPk)")
st.write("- [High cholesterol](https://www.youtube.com/watch?feature=shared&v=G3AIYdJdfDk)")
st.write("- [Stress](https://www.youtube.com/watch?feature=shared&v=QODuDQwsJ80)")
st.write("- [Maintain healthy weight](https://www.youtube.com/watch?feature=shared&v=_ZtgTotfAfQ)")

# Footer Section
st.write("---")
st.header("Feedback and Support")
st.write("We value your feedback! Please let us know how we can improve this application or if you need further assistance.")
feedback = st.text_area("Your Feedback:", height=100)
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
