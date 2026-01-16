import random
import pandas as pd
import os

# ---------------------------
# CONFIG
# ---------------------------
ROWS_PER_ROLE = 120
OUTPUT_PATH = "data/raw/career_dataset_v3.csv"

# ---------------------------
# ROLE SKILL BASE PROFILES
# ---------------------------
ROLE_PROFILES = {
    "ML Engineer": {
        "python": (2, 3),
        "sql": (1, 2),
        "statistics": (2, 3),
        "ml": (2, 3),
        "dl": (1, 2),
        "nlp": (0, 1),
        "excel": (0, 1),
        "communication": (1, 2)
    },

    "AI Engineer": {
        "python": (2, 3),
        "statistics": (1, 2),
        "ml": (2, 3),
        "dl": (2, 3),
        "nlp": (2, 3),
        "sql": (0, 1),
        "excel": (0, 1),
        "communication": (1, 2)
    },

    "Data Scientist": {
        "python": (2, 3),
        "sql": (2, 3),
        "statistics": (2, 3),
        "ml": (2, 3),
        "dl": (0, 1),
        "nlp": (0, 1),
        "excel": (1, 2),
        "communication": (1, 2)
    },

    "Data Analyst": {
        "python": (0, 1),
        "sql": (2, 3),
        "statistics": (2, 3),
        "ml": (0, 0),
        "dl": (0, 0),
        "nlp": (0, 0),
        "excel": (2, 3),
        "communication": (2, 3)
    },

    "Business Analyst": {
        "python": (0, 1),
        "sql": (1, 2),
        "statistics": (1, 2),
        "ml": (0, 0),
        "dl": (0, 0),
        "nlp": (0, 0),
        "excel": (2, 3),
        "communication": (2, 3)
    },

    "Backend Developer": {
        "python": (2, 3),
        "sql": (2, 3),
        "statistics": (0, 1),
        "ml": (0, 0),
        "dl": (0, 0),
        "nlp": (0, 0),
        "excel": (0, 1),
        "communication": (1, 2)
    }
}

# ---------------------------
# CREATE DATASET
# ---------------------------
os.makedirs("data/raw", exist_ok=True)

data = []

for role, skills in ROLE_PROFILES.items():
    for _ in range(ROWS_PER_ROLE):
        row = {}
        for skill, (low, high) in skills.items():
            row[skill] = random.randint(low, high)
        row["role"] = role
        data.append(row)

df = pd.DataFrame(data)
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Dataset generated successfully!")
print(f"📄 File saved at: {OUTPUT_PATH}")
print(f"📊 Total rows: {len(df)}")
