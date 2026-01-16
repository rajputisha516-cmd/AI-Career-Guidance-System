# 🎓 AI Career Guidance System

An intelligent, end-to-end **AI-powered Career Guidance System** that recommends suitable career roles based on a user's **skills, resume analysis, and proficiency levels**, and provides **skill gap analysis, readiness score, projects, and learning roadmap**.

This project is designed especially for **students and freshers** who want clear direction in AI/ML-related career paths.

---

## 🚀 Features

- 📄 **Resume Parsing (3 Ways)**
  - Upload Resume (PDF)
  - Paste Resume URL
  - Paste Resume Text directly (no download needed)

- 🧠 **Skill Extraction from Resume**
  - Automatically detects skills like Python, ML, DL, SQL, NLP, Statistics

- 🔧 **Manual Skill Selection with Levels**
  - None / Basic / Intermediate / Advanced

- ⚖️ **Smart Skill Merging Logic**
  - Combines resume skills + manual input
  - Caps skill level to avoid fake resume inflation

- 🎯 **Career Prediction**
  - Data Analyst  
  - Machine Learning Engineer  
  - AI Engineer  
  - Business Analyst  

- 🧩 **Skill Gap Analysis**
  - Highlights weak, intermediate, and strong skills

- 📊 **Role Readiness Meter**
  - Shows percentage readiness for the predicted role

- 🛠 **Suggested Mini & Major Projects**
  - Role-specific real-world projects

- 🗺 **Personalized Learning Roadmap**
  - Curated YouTube learning resources

- 💬 **Mini Career Chatbot**
  - Answers basic career-related questions

- 🎨 **Clean & Professional Streamlit UI**

---

## 🧠 Tech Stack

- **Python**
- **Machine Learning (Scikit-learn)**
- **Pandas & NumPy**
- **Streamlit**
- **Pickle**
- **Resume Parsing (PDF/Text/URL)**

---

## 📂 Project Structure

AI_Career_Guidance_System/
│
├── data/
│ └── career_dataset.csv
│
├── model/
│ ├── career_model.pkl
│ └── label_encoder.pkl
│
├── app.py
├── train_model.py
├── resume_parser.py
├── recommendation.py
├── requirements.py
├── README.md
└── pycache/

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rajputisha516-cmd/AI_Career_Guidance_System.git
cd AI_Career_Guidance_System
