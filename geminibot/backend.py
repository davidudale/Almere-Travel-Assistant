import google.generativeai as genai

genai.configure(api_key="AIzaSyCyRjqmkEDptcVSZPkmIg-QeTddgBVNyCY")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def GenerateResponse(user_input, profile):
    try:
        prompt = f"""
You are TravelMate, a smart assistant trained to help commuters in Almere using real survey insights.

User profile:
- Mode: {profile.get('mode')}
- Flexibility: {profile.get('flexibility')}
- Punctuality: {profile.get('punctuality')}
- Environment concern: {profile.get('environmental_concern')}

Context:
- Bus crowding is highest 7:30–9:00 and 16:30–18:00.

- Students bike more and shift times.
- Workers prefer predictability.

User: {user_input}
Response:
        """
        return model.generate_content(prompt).text
    except Exception as e:
        print(f"Error: {e}")
        return "⚠️ Sorry, I'm currently unavailable due to high traffic. Please try again later."
