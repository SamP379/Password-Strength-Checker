import zxcvbn as zx
from langchain_ollama import OllamaLLM


def get_password() -> str:
    """Prompts the user to enter a password and returns it."""
    while not (password := input("Enter password: ")):
        pass
    return password


def assess_password(password : str) -> dict:
    """Analyzes the strength of a given password using the zxcvbn library and returns the results."""
    assessment = zx.zxcvbn(password)
    return assessment


def display_assessment_results(assessment : dict):
    password_score = assessment["score"]
    password_crack_time = assessment['crack_times_display']["offline_slow_hashing_1e4_per_second"]
    print(f"\nScore: {password_score}/4")
    print(f"Crack time: {password_crack_time}\n")


def generate_response(prompt : str) -> str:
    model = OllamaLLM(model = "llama3.2")
    response = model.invoke(input = prompt)
    return response


def main():
    print("\nPassword Strength Checker\n")
    password = get_password()
    password_assessment = assess_password(password)
    display_assessment_results(password_assessment)
    ai_response = generate_response(f"Short response. No first person. Make a joke about how secure this password is: {password}")
    print(ai_response + "\n")

    wants_feedback = input("Would you like some feedback on how to make the password stronger?").lower()
    if wants_feedback == "yes":
        ai_response = generate_response(f"Short response. Give feedback on how to make this password stronger, you can be a bit humours based on what the password is but still educational: {password}")
        print(ai_response)
    



    


main()