import streamlit as st
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.set_page_config(page_title="Physiotherapy Assessment Platform", layout="wide")

st.title("Physiotherapy Clinical Assessment System")

tabs = st.tabs([
"Demographics",
"Chief Complaint",
"History",
"Observation",
"Examination",
"ROM",
"MMT",
"Sensory",
"Neurological",
"Diagnosis & Report"
])

# ------------------------------------------------
# DEMOGRAPHICS
# ------------------------------------------------

with tabs[0]:

    st.header("Demographic Data")

    col1,col2,col3 = st.columns(3)

    with col1:
        name = st.text_input("Name")
        age = st.number_input("Age",0,120)

    with col2:
        gender = st.selectbox("Gender",["Male","Female","Other"])
        occupation = st.text_input("Occupation")

    with col3:
        dominance = st.selectbox("Dominant Hand",["Right","Left"])
        address = st.text_area("Address")


# ------------------------------------------------
# CHIEF COMPLAINT
# ------------------------------------------------

with tabs[1]:

    st.header("Chief Complaint – Functional Difficulty")

    difficulty = st.multiselect(
    "Difficulty in",
    [
    "Walking",
    "ADL",
    "Sitting",
    "Standing",
    "Overhead Activities",
    "Working"
    ]
    )

    chief_notes = st.text_area("Additional Complaint Description")


# ------------------------------------------------
# HISTORY
# ------------------------------------------------

with tabs[2]:

    st.header("History")

    present_history = st.text_area("Present History")

    past_history = st.text_area("Past History")

    family_history = st.text_area("Family History")

    st.subheader("Medical History")

    medical_conditions = st.multiselect(
    "Select Conditions",
    [
    "Cancer","Diabetes","Hypoglycemia","Hypertension",
    "Heart Diseases","Angina","Shortness of Breath",
    "Stroke","Kidney Disease","UTI","Allergies",
    "Asthma","Liver Disease","Polio","Chronic Bronchitis",
    "Pneumonia","Emphysema","Migraine","Anemia",
    "Ulcer","Arthritis"
    ]
    )

    drug_history = st.text_area("Drug History")

    surgical_history = st.text_area("Surgical History")

    st.subheader("Pain Assessment")

    pain_score = st.slider("Pain (VAS Scale)",0,10)

    pain_area = st.multiselect(
    "Pain Location",
    ["Neck","Shoulder","Back","Hip","Knee","Ankle","Foot","Elbow","Wrist"]
    )


# ------------------------------------------------
# OBSERVATION
# ------------------------------------------------

with tabs[3]:

    st.header("Observation")

    body_built = st.selectbox("Body Built",["Ectomorph","Mesomorph","Endomorph"])

    swelling_grade = st.selectbox("Swelling Grade",["None","1+","2+","3+","4+"])

    swelling_area = st.text_input("Swelling Area")

    edema_grade = st.selectbox("Edema Grade",["None","1+","2+","3+","4+"])

    edema_area = st.text_input("Edema Area")

    scar_area = st.text_input("Scar Area")

    ambulation = st.radio("Mode of Ambulation",["Independent","Dependent"])

    appliances = st.radio("External Appliances",["Present","Not Present"])

    gait = st.text_input("Gait Pattern")

    involuntary = st.text_input("Involuntary Movement")

    posture = st.text_input("Posture")


# ------------------------------------------------
# EXAMINATION
# ------------------------------------------------

with tabs[4]:

    st.header("Vitals")

    col1,col2,col3 = st.columns(3)

    with col1:
        HR = st.number_input("Heart Rate")

    with col2:
        RR = st.number_input("Respiratory Rate")

    with col3:
        weight = st.number_input("Weight")

    muscle_tone = st.selectbox(
    "Muscle Tone (MAS)",
    ["0","1","1+","2","3","4"]
    )


# ------------------------------------------------
# ROM
# ------------------------------------------------

with tabs[5]:

    st.header("Range of Motion (Degrees)")

    joints = [
    "Shoulder Flexion","Shoulder Extension","Shoulder Abduction","Shoulder Adduction","Shoulder IR","Shoulder ER",
    "Elbow Flexion","Elbow Extension",
    "Wrist Flexion","Wrist Extension","Wrist UD","Wrist RD",
    "Hip Flexion","Hip Extension","Hip Abduction","Hip Adduction","Hip IR","Hip ER",
    "Knee Flexion","Knee Extension",
    "Ankle Plantarflexion","Ankle Dorsiflexion"
    ]

    rom_data = {}

    for j in joints:
        rom_data[j] = st.number_input(j,0,200)

# ------------------------------------------------
# MMT
# ------------------------------------------------

with tabs[6]:

    st.header("Manual Muscle Testing")

    grades = ["0","1","2","3","4","5"]

    mmt_data = {}

    for j in joints:
        mmt_data[j] = st.selectbox(f"{j} Strength",grades)

# ------------------------------------------------
# SENSORY
# ------------------------------------------------

with tabs[7]:

    st.header("Sensory Examination")

    superficial = st.multiselect(
    "Superficial Sensation",
    ["Light Touch","Pressure","Temperature","Pain"]
    )

    deep = st.multiselect(
    "Deep Sensation",
    ["Kinesthesia","Proprioception"]
    )

    cortical = st.multiselect(
    "Cortical Sensation",
    ["2 Point Discrimination","Tactile Localization","Stereognosis"]
    )


# ------------------------------------------------
# NEUROLOGICAL
# ------------------------------------------------

with tabs[8]:

    st.header("Neurological Examination")

    dtr = st.multiselect(
    "Deep Tendon Reflex",
    ["Biceps","Triceps","Knee","Ankle"]
    )

    cranial = st.text_area("Cranial Nerve Examination")

    coordination = st.text_area("Coordination")

    balance = st.text_area("Balance")

    mmse = st.number_input("MMSE Score",0,30)

    dgi = st.number_input("Dynamic Gait Index",0,24)

    investigation = st.text_area("Investigations")


# ------------------------------------------------
# DIAGNOSIS & REPORT
# ------------------------------------------------

with tabs[9]:

    st.header("Diagnosis")

    diagnosis = st.text_area("Clinical Diagnosis")

    styles = getSampleStyleSheet()

    def generate_pdf():

        file = tempfile.NamedTemporaryFile(delete=False)

        doc = SimpleDocTemplate(file.name)

        story = []

        story.append(Paragraph("Physiotherapy Assessment Report",styles['Title']))
        story.append(Spacer(1,20))

        story.append(Paragraph(f"Name: {name}",styles['Normal']))
        story.append(Paragraph(f"Age: {age}",styles['Normal']))
        story.append(Paragraph(f"Gender: {gender}",styles['Normal']))
        story.append(Paragraph(f"Occupation: {occupation}",styles['Normal']))

        story.append(Spacer(1,20))

        story.append(Paragraph("Chief Complaint",styles['Heading2']))
        story.append(Paragraph(str(difficulty),styles['Normal']))

        story.append(Paragraph("Diagnosis",styles['Heading2']))
        story.append(Paragraph(diagnosis,styles['Normal']))

        doc.build(story)

        return file.name

    if st.button("Generate Report"):

        pdf = generate_pdf()

        with open(pdf,"rb") as f:
            st.download_button(
            "Download PDF Report",
            f,
            file_name="physio_assessment_report.pdf"
            )
