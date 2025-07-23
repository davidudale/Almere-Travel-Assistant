import pandas as pd

def load_survey(filepath="almere_survey.csv"):
    return pd.read_csv(filepath)

def get_profile_from_survey_row(row):
    flexibility = "high" if int(row["tpb_control"]) + int(row["tpb_shift"]) >= 8 else "low"
    environmental_concern = "high" if int(row["tpb_environment"]) >= 4 else "low"
    punctuality = "high" if int(row.get("tpb_convenience", 3)) >= 4 else "low"

    return {
        "mode": row["mode"].lower(),
        "flexibility": flexibility,
        "punctuality": punctuality,
        "environmental_concern": environmental_concern,
        
    }
