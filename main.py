import zxcvbn as zx
from langchain_ollama import OllamaLLM


AI_JOKE_PROMPT = "Short response. No first person. Make a joke about how secure this password is: "


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
    """Displays the results of the password assessment using the zxcvbn library."""
    password_score = assessment["score"]
    password_crack_time = assessment['crack_times_display']["offline_slow_hashing_1e4_per_second"]
    print(f"\nScore: {password_score}/4")
    print(f"Crack time: {password_crack_time}\n")


def generate_ai_response(prompt : str) -> str:
    """Generates a response from the llama3.2 LLM using a given prompt."""
    model = OllamaLLM(model = "llama3.2")
    response = model.invoke(input = prompt)
    return response


def main():

    print("\nPassword Strength Checker\n")

    # Get a password from the user and assess its strength
    password = get_password()
    password_assessment = assess_password(password)
    display_assessment_results(password_assessment)

    # Get an ai-generated joke about the entered password
    ai_prompt = AI_JOKE_PROMPT + password
    password_joke = generate_ai_response(prompt = ai_prompt)
    print(password_joke + "\n")

    # wants_feedback = input("Would you like some feedback on how to make the password stronger?").lower()
    # if wants_feedback == "yes":
    #     ai_response = generate_response(f"Short response. Give feedback on how to make this password stronger, you can be a bit humours based on what the password is but still educational: {password}")
    #     print(ai_response)
    


main()