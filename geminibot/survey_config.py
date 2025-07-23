survey = {
    "SECTION 1: Demographics": [
        ("age", "What is your age?", "text"),
        ("employment", "What is your employment status?", ["Full-time", "Part-time", "Student", "Unemployed", "Retired"]),
        ("gender", "What is your gender?", ["Female", "Male", "Other", "Prefer not to say"]),
        
    ],
    "SECTION 2: Commuting Patterns": [
        ("mode", "What is your primary mode of transportation?", ["Bus", "Car"]),
        ("bus_lines", "Which bus line(s) do you use most often in Almere?", "text"),
        ("departure_time", "What time do you usually leave for work/school?", "time"),
        
    ],
    "SECTION 3: Experience with Transit and Crowding": [
        ("crowdedness", "How crowded is your usual bus during peak hours?", ["Not crowded", "Slightly crowded", "Very crowded", "Overcrowded"]),
        ("frustrations", "What issues frustrate you most?", ["Overcrowding", "Delays", "No real-time updates", "Cost", "Long walking distance", "None"]),
        
    ],
    "SECTION 4: Attitudes and Preferences (TPB)": [
        ("tpb_convenience", "Public transport is convenient for me.", "radio"),
        ("tpb_norms", "Most people I know use or recommend it.", "radio"),
        ("tpb_control", "I can change my travel time if needed.", "radio"),
        ("tpb_shift", "I would change my time if bus is full.", "radio"),
        ("tpb_environment", "I care about reducing pollution.", "radio"),
        ("tpb_self_control", "I feel in control of my commute.", "radio"),
        ("tpb_preplan", "I rarely think about crowding.", "radio"),
        ("tpb_ignore_crowd", "Full buses don’t affect me.", "radio"),
    ],
    "SECTION 5: Hypothetical Reactions": [
        ("reaction", "If your bus is 90% full, what would you do?", ["Wait", "Change time", "Switch line", "Board anyway", "Cancel"]),
        ("why_avoid", "Why do you (not) avoid crowded buses?", "text"),
    ],
}
