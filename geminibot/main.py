import streamlit as st
from backend import GenerateResponse

st.set_page_config(page_title="TravelMate Almere", layout="centered")
st.title("🚍 TravelMate - Almere Chatbot")

# SECTION: User Profile Form
st.subheader("🧾 Tell us a bit about yourself")

with st.form("user_profile_form"):
    age = st.number_input("Age", min_value=10, max_value=100, value=30)
    employment = st.selectbox("Employment Status", ["Full-time", "Part-time", "Student", "Unemployed", "Retired"])
    mode = st.selectbox("Primary Mode of Transportation", ["Bus", "Train", "Bike", "Car", "Walking", "Other"])
    submit = st.form_submit_button("Save Profile")

# Save profile to session
if submit or ("profile" not in st.session_state):
    st.session_state.profile = {
        "age": age,
        "employment": employment,
        "mode": mode,
        "flexibility": "medium",  # you can infer or ask
        "punctuality": "medium",
        "environmental_concern": "high"
    }
    st.success("✅ Profile saved!")

# SECTION: Chat
st.header("💬 Ask TravelMate about commuting")

prompt = st.text_input("What's your question?")
if prompt and "profile" in st.session_state:
    profile = st.session_state.profile

    # Display user message
    st.markdown(f"""
    <div style="display:flex;align-items:center;margin-bottom:0.5rem;">
        <div style="font-size:24px;margin-right:8px;">🧑</div>
        <div style="background-color:transparent;padding:10px;border-radius:10px;">{prompt}</div>
    </div>
    """, unsafe_allow_html=True)

    # Generate and display bot response
    response = GenerateResponse(prompt, profile)

    st.markdown(f"""
    <div style="display:flex;align-items:center;margin-bottom:1rem;">
        <div style="font-size:24px;margin-right:8px;">🤖</div>
        <div style="background-color:transparent;padding:10px;border-radius:10px;">{response}</div>
    </div>
    """, unsafe_allow_html=True)
