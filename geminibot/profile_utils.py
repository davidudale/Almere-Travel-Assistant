def infer_persona_from_responses(responses):
    score = int(responses.get("tpb_shift", 3)) + int(responses.get("tpb_control", 3))
    green = int(responses.get("tpb_environment", 3))
    flexibility = "high" if score >= 7 else "low"
    env_pref = "high" if green >= 4 else "low"

    return {
        "mode": responses.get("mode", "bus"),
        "flexibility": flexibility,
        "punctuality": "high" if responses.get("tpb_convenience", 3) >= 4 else "low",
        "environmental_concern": env_pref,
        
    }
