from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_story_segment(user_name, path_summary):
    prompt = f"""
    You are a dream storyteller. A traveler named {user_name} has made these choices: {path_summary}.
    Write the next part of their surreal journey in vivid, poetic language. End with two choices: A and B.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()
