from utils.resume_parser import extract_text_from_pdf, extract_skills_from_resume
from utils.intent_handler import detect_user_intent, get_intent_message
from utils.role_guidance import get_role_specific_guidance


import streamlit as st
import pickle
import pandas as pd
import requests
from io import BytesIO

# ================= Role–Skill Requirements (NEW) =================
ROLE_SKILL_REQUIREMENTS = {
    "ML Engineer": ["Python", "Machine Learning", "Statistics", "Deep Learning", "NLP"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "NLP", "Statistics"],
    "Data Scientist": ["Python", "SQL", "Statistics", "Machine Learning"],
    "Data Analyst": ["SQL", "Excel", "Statistics", "Python"],
    "Business Analyst": ["Excel", "SQL", "Communication", "Statistics"],
    "Backend Developer": ["Python", "SQL", "Communication"]
}

# ================= Helper Function =================
def show_skill_status(skill_name, skill_level):
    if skill_level < 2:
        st.info(f"⬇️ {skill_name} needs improvement")
    elif skill_level == 2:
        st.info(f"ℹ️ {skill_name} at intermediate level")
    else:
        st.info(f"✔️ {skill_name} skill is strong")

# ================= Load Model =================
model = pickle.load(open("models/career_model.pkl", "rb"))
label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

# ================= Session State =================
if "predicted" not in st.session_state:
    st.session_state.predicted = False

# ================= Page Config =================
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Career Guidance System")
st.write("Select your skills and get career recommendations")

# ================= Resume Input (UNCHANGED) =================
with st.sidebar:
    st.header("📄 Resume Input")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    st.markdown("— OR —")
    resume_url = st.text_input("Paste Resume PDF URL")
    st.markdown("— OR —")
    resume_text_input = st.text_area("Paste Resume Text", height=200)

resume_skills = None

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_skills = extract_skills_from_resume(resume_text)
    st.sidebar.caption("✅ Resume processed (File Upload)")

elif resume_url:
    try:
        response = requests.get(resume_url)
        pdf_file = BytesIO(response.content)
        resume_text = extract_text_from_pdf(pdf_file)
        resume_skills = extract_skills_from_resume(resume_text)
        st.sidebar.caption("✅ Resume processed (URL)")
    except:
        st.sidebar.error("❌ Invalid resume URL")

elif resume_text_input:
    resume_skills = extract_skills_from_resume(resume_text_input)
    st.sidebar.caption("✅ Resume processed (Pasted Text)")

# ================= Manual Skills (UNCHANGED) =================
st.header("🔧 Select Your Skills")

level_map = {"None": 0, "Basic": 1, "Intermediate": 2, "Advanced": 3}

col1, col2 = st.columns(2)

with col1:
    python_level = st.selectbox("Python", level_map.keys())
    ml_level = st.selectbox("Machine Learning", level_map.keys())
    dl_level = st.selectbox("Deep Learning", level_map.keys())
    excel_level = st.selectbox("Excel", level_map.keys())

with col2:
    sql_level = st.selectbox("SQL", level_map.keys())
    nlp_level = st.selectbox("NLP", level_map.keys())
    stats_level = st.selectbox("Statistics", level_map.keys())
    communication_level = st.selectbox("Communication", level_map.keys())

    
    selected_levels = {
    "python": python_level,
    "sql": sql_level,
    "statistics": stats_level,
    "ml": ml_level,
    "dl": dl_level,
    "nlp": nlp_level
    }


# ================= Predict Button =================
st.markdown("---")
if st.button("🚀 Predict Career Path"):
    st.session_state.predicted = True

# ================= Results Section =================
if st.session_state.predicted:

    resume_skills = resume_skills or {}

    final_python = min(resume_skills.get("python", 0) + level_map[python_level], 3)
    final_sql = min(resume_skills.get("sql", 0) + level_map[sql_level], 3)
    final_stats = min(resume_skills.get("statistics", 0) + level_map[stats_level], 3)
    final_ml = min(resume_skills.get("ml", 0) + level_map[ml_level], 3)
    final_dl = min(resume_skills.get("dl", 0) + level_map[dl_level], 3)
    final_nlp = min(resume_skills.get("nlp", 0) + level_map[nlp_level], 3)
    final_excel = min(resume_skills.get("excel", 0) + level_map[excel_level], 3)
    final_comm = min(resume_skills.get("communication", 0) + level_map[communication_level], 3)

    user_data = pd.DataFrame([[
        final_python, final_sql, final_stats,
        final_ml, final_dl, final_nlp,
        final_excel, final_comm
    ]], columns=[
        "python", "sql", "statistics",
        "ml", "dl", "nlp",
        "excel", "communication"
    ])

    career = label_encoder.inverse_transform(model.predict(user_data))[0]

    # ================= Intent Detection & Explanation (NEW) =================
    intents = detect_user_intent(level_map, selected_levels)
    intent_msg = get_intent_message(career, intents)

    if intent_msg:
        st.info(intent_msg)


    st.markdown(
        f"""
        <div style="background-color:#f5f9ff;padding:22px;border-radius:14px">
            <h2 style="color:#1f3c88;">🎯 Recommended Career</h2>
            <h3 style="color:#1f3c88;">{career}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ================= Skill Gap (ROLE-AWARE FIX) =================
    st.subheader("🧠 Skill Gap Analysis")

    skill_values = {
        "Python": final_python,
        "SQL": final_sql,
        "Statistics": final_stats,
        "Machine Learning": final_ml,
        "Deep Learning": final_dl,
        "NLP": final_nlp,
        "Excel": final_excel,
        "Communication": final_comm
    }

    for skill in ROLE_SKILL_REQUIREMENTS.get(career, []):
        show_skill_status(skill, skill_values[skill])

    # ================= Role Readiness (UNCHANGED) =================
    st.subheader("📊 Role Readiness")
    readiness = int(
        sum(skill_values[s] for s in ROLE_SKILL_REQUIREMENTS[career]) /
        (len(ROLE_SKILL_REQUIREMENTS[career]) * 3) * 100
    )
    st.progress(readiness)
    st.caption(f"You are approximately {readiness}% ready for this role")

    # ================= Skill Level Classification =================
    if readiness < 40:
        user_level = "Beginner"
    elif readiness < 70:
        user_level = "Intermediate"
    else:
        user_level = "Ready"

    st.subheader("🧭 Your Current Level")
    st.success(f"You are at **{user_level}** level for the {career} role")

    st.subheader("📘 Personalized Guidance")

    guidance_text = get_role_specific_guidance(career, user_level)
    st.info(guidance_text)


    # ================= Roadmap (UNCHANGED) =================
    with st.expander("📌 View Personalized Roadmap"):
        st.write("### 🔧 Skills to Improve")
        for skill in ROLE_SKILL_REQUIREMENTS[career]:
            if skill_values[skill] < 2:
                st.write(f"✔ {skill}")

# ================= Footer =================
st.markdown("---")
st.caption("Built with ❤️ using Python, Machine Learning & Streamlit")
