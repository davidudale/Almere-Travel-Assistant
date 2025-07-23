import google.generativeai as genai

genai.configure(api_key="AIzaSyCyRjqmkEDptcVSZPkmIg-QeTddgBVNyCY")

generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 1024,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def GenerateResponse(user_input, profile):
    prompt = f"""
You are Almere Travel Assistant, a smart commuter assistant for Almere citizens.

User Profile:
- Preferred Mode: {profile.get('mode')}
- Flexibility: {profile.get('flexibility')}
- Punctuality: {profile.get('punctuality')}
- Environmental Concern: {profile.get('environmental_concern')}


Use behavioral logic, survey insights, and TPB to offer friendly, practical travel advice for avoiding congestion and improving commuting experience.

User says: '{user_input}'
Assistant Response:
"""
    response = model.generate_content(prompt)
    return response.text
