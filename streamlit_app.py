import streamlit as st
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

st.set_page_config(page_title="Physiotherapy Assessment Platform", layout="wide")

st.title("🏥 Physiotherapy Clinical Assessment System")

# -------------------------
# DEMOGRAPHIC DATA
# -------------------------

st.header("Patient Demographics")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Patient Name")
    age = st.number_input("Age", 0, 120)

with col2:
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    phone = st.text_input("Phone Number")

with col3:
    occupation = st.text_input("Occupation")
    visit_date = st.date_input("Visit Date")

# -------------------------
# MEDICAL HISTORY
# -------------------------

st.header("Medical History")

conditions = [
"Diabetes",
"Hypertension",
"Thyroid Disorder",
"Cardiac Disease",
"Asthma",
"Arthritis",
"Osteoporosis",
"Previous Surgery",
"Neurological Disorder"
]

history = st.multiselect("Select Existing Conditions", conditions)

other_history = st.text_area("Other Medical History")

# -------------------------
# PAIN SCALE
# -------------------------

st.header("Pain Assessment")

pain_score = st.slider("Pain Level (VAS Scale)", 0, 10)

pain_area = st.multiselect(
"Area of Pain",
[
"Neck","Shoulder","Upper Back","Lower Back",
"Hip","Knee","Ankle","Foot","Elbow","Wrist"
]
)

# -------------------------
# MMT
# -------------------------

st.header("Manual Muscle Testing (MMT)")

mmt_scale = ["0","1","2","3","4","5"]

mmt_shoulder = st.selectbox("Shoulder Strength", mmt_scale)
mmt_elbow = st.selectbox("Elbow Strength", mmt_scale)
mmt_hip = st.selectbox("Hip Strength", mmt_scale)
mmt_knee = st.selectbox("Knee Strength", mmt_scale)

# -------------------------
# RANGE OF MOTION
# -------------------------

st.header("Range of Motion (Degrees)")

col1, col2 = st.columns(2)

with col1:
    shoulder_rom = st.number_input("Shoulder ROM")
    elbow_rom = st.number_input("Elbow ROM")

with col2:
    hip_rom = st.number_input("Hip ROM")
    knee_rom = st.number_input("Knee ROM")

# -------------------------
# EDEMA
# -------------------------

st.header("Inflammation / Edema")

edema_grade = st.selectbox(
"Edema Grade",
["None","1+ Mild","2+ Moderate","3+ Deep","4+ Severe"]
)

# -------------------------
# CLINICAL EXAMINATION
# -------------------------

st.header("Clinical Examination")

observation = st.text_area("On Observation")

palpation = st.text_area("On Palpation")

examination = st.text_area("On Examination")

# -------------------------
# SPECIAL TESTS
# -------------------------

st.header("Special Tests")

special_tests = st.text_area("Document Special Tests")

# -------------------------
# DIAGNOSIS
# -------------------------

st.header("Clinical Diagnosis")

diagnosis = st.text_area("Diagnosis")

# -------------------------
# REHAB PROTOCOL
# -------------------------

st.header("Rehabilitation Plan")

rehab = st.text_area("Rehabilitation Protocol")

# -------------------------
# REPORT GENERATION
# -------------------------

def create_pdf():

    styles = getSampleStyleSheet()
    
    file = tempfile.NamedTemporaryFile(delete=False)
    
    doc = SimpleDocTemplate(file.name)
    
    story = []
    
    story.append(Paragraph("Physiotherapy Assessment Report", styles['Title']))
    story.append(Spacer(1,20))
    
    story.append(Paragraph(f"Patient Name: {name}", styles['Normal']))
    story.append(Paragraph(f"Age: {age}", styles['Normal']))
    story.append(Paragraph(f"Gender: {gender}", styles['Normal']))
    story.append(Paragraph(f"Phone: {phone}", styles['Normal']))
    
    story.append(Spacer(1,20))
    
    story.append(Paragraph("Medical History:", styles['Heading2']))
    story.append(Paragraph(", ".join(history), styles['Normal']))
    story.append(Paragraph(other_history, styles['Normal']))
    
    story.append(Spacer(1,20))
    
    story.append(Paragraph("Pain Assessment:", styles['Heading2']))
    story.append(Paragraph(f"Pain Score: {pain_score}", styles['Normal']))
    story.append(Paragraph(f"Pain Area: {', '.join(pain_area)}", styles['Normal']))
    
    story.append(Spacer(1,20))
    
    story.append(Paragraph("MMT Results:", styles['Heading2']))
    story.append(Paragraph(f"Shoulder: {mmt_shoulder}", styles['Normal']))
    story.append(Paragraph(f"Elbow: {mmt_elbow}", styles['Normal']))
    story.append(Paragraph(f"Hip: {mmt_hip}", styles['Normal']))
    story.append(Paragraph(f"Knee: {mmt_knee}", styles['Normal']))
    
    story.append(Spacer(1,20))
    
    story.append(Paragraph("ROM:", styles['Heading2']))
    story.append(Paragraph(f"Shoulder: {shoulder_rom}", styles['Normal']))
    story.append(Paragraph(f"Elbow: {elbow_rom}", styles['Normal']))
    story.append(Paragraph(f"Hip: {hip_rom}", styles['Normal']))
    story.append(Paragraph(f"Knee: {knee_rom}", styles['Normal']))
    
    story.append(Spacer(1,20))
    
    story.append(Paragraph("Observation:", styles['Heading2']))
    story.append(Paragraph(observation, styles['Normal']))
    
    story.append(Paragraph("Palpation:", styles['Heading2']))
    story.append(Paragraph(palpation, styles['Normal']))
    
    story.append(Paragraph("Examination:", styles['Heading2']))
    story.append(Paragraph(examination, styles['Normal']))
    
    story.append(Paragraph("Special Tests:", styles['Heading2']))
    story.append(Paragraph(special_tests, styles['Normal']))
    
    story.append(Paragraph("Diagnosis:", styles['Heading2']))
    story.append(Paragraph(diagnosis, styles['Normal']))
    
    story.append(Paragraph("Rehabilitation Protocol:", styles['Heading2']))
    story.append(Paragraph(rehab, styles['Normal']))
    
    doc.build(story)
    
    return file.name


if st.button("Generate Report"):

    pdf = create_pdf()

    with open(pdf, "rb") as f:
        st.download_button(
            label="Download Report",
            data=f,
            file_name="physiotherapy_report.pdf",
            mime="application/pdf"
        )
