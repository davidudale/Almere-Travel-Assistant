import streamlit as st
from survey_config import survey
from backend import GenerateResponse
from profile_utils import infer_persona_from_responses

st.set_page_config(page_title="Almere Travel Assistant", layout="centered")
st.title("🚌 Almere Travel Assistant")

# Initialize session
if "section_idx" not in st.session_state:
    st.session_state.section_idx = 0
    st.session_state.responses = {}

section_titles = list(survey.keys())

# Show current section
current_title = section_titles[st.session_state.section_idx]
st.subheader(current_title)

for q_key, q_text, q_type in survey[current_title]:
    if q_type == "text":
        st.session_state.responses[q_key] = st.text_input(q_text, key=q_key)
    elif q_type == "time":
        st.session_state.responses[q_key] = st.time_input(q_text, key=q_key)
    elif q_type == "slider":
        st.session_state.responses[q_key] = st.slider(q_text, 1, 5, 3, key=q_key)
    elif isinstance(q_type, list):  # radio
        st.session_state.responses[q_key] = st.radio(q_text, options=q_type, key=q_key)

# Navigation
if st.button("Next"):
    if st.session_state.section_idx < len(section_titles) - 1:
        st.session_state.section_idx += 1
        st.rerun()
    else:
        st.success("✅ Survey complete! Your profile has been created.")
        st.session_state.profile = infer_persona_from_responses(st.session_state.responses)
        st.session_state.messages = []
        st.rerun()

# Chat mode
if "profile" in st.session_state:
    st.header("🧠 Ask Almere Travel Assistant")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("What's your question about commuting with in Almere?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = GenerateResponse(prompt, st.session_state.profile)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
