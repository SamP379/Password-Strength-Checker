import zxcvbn as zx
from langchain_ollama import OllamaLLM


LLAMA_JOKE_PROMPT = "Short response. No first person. Make a joke about how secure this password is: "
LLAMA_FEEDBACK_PROMPT = """Short response. Give feedback on how to make this password stronger, be 
                           humorous based on what the password is but still educational: """


def get_password() -> str:
    """Prompts the user to enter a password and returns it."""
    while not (password := input("Enter password: ")):
        pass
    return password


def get_password_assessment(password : str) -> dict:
    """Analyzes the strength of a given password using the zxcvbn library and returns the results."""
    assessment = zx.zxcvbn(password)
    return assessment


def display_assessment_results(assessment : dict):
    """Displays the results of the password assessment."""
    password_score = assessment["score"]
    password_crack_time = assessment['crack_times_display']["offline_slow_hashing_1e4_per_second"]
    print(f"\nScore: {password_score}/4")
    print(f"Crack time: {password_crack_time}\n")


def get_llama_response(prompt : str) -> str:
    """Generates a response from the llama3.2 LLM using a given prompt."""
    try:
        model = OllamaLLM(model = "llama3.2")
        response = model.invoke(input = prompt)
        return response
    except Exception as error:
        print(f"An error occured: {error}")
        return None


def main():

    print("\nPassword Strength Checker\n")

    # Get password from the user and assess its strength
    password = get_password()
    password_assessment = get_password_assessment(password)
    display_assessment_results(password_assessment)

    # Get an AI-generated joke about the entered password
    llama_prompt = LLAMA_JOKE_PROMPT + password
    llama_response = get_llama_response(prompt = llama_prompt)
    if llama_response is not None:
        print(llama_response + "\n")

    # Check if the user wants ai-generated feedback 
    wants_feedback = input("Would you like some feedback on how to make the password stronger? ").lower()
    if wants_feedback == "yes":
        llama_prompt = LLAMA_FEEDBACK_PROMPT + password
        llama_response = get_llama_response(prompt = llama_prompt)
        if llama_response is not None:
            print("\n\nFeedback:")
            print("\n\n" + llama_response + "\n")


if __name__ == "__main__":
    main()