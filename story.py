# story.py
from ai_engine import generate_story_segment

def run_story():
    print("✨ Welcome to DreamChoice AI ✨")
    name = input("What is your name, dream traveler? ")
    path = []

    while True:
        segment = generate_story_segment(name, ' → '.join(path))
        print("\n" + segment)
        choice = input("Your choice (A/B): ").strip().upper()
        if choice in ['A', 'B']:
            path.append(choice)
        else:
            print("Please enter A or B.")

        if len(path) > 5:
            print("\n🌙 Your dream fades into memory... The End.")
            break
