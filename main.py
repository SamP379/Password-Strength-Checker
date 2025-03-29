import zxcvbn as zx
from langchain_ollama import OllamaLLM




def assess_password(password : str) -> dict:
    assessment = zx.zxcvbn(password)
    return assessment

def generate_feedback(password : str) -> str:
    model = OllamaLLM(model = "llama3.2")
    feedback = model.invoke(input = f"Short response. Give feedback on the strength of this password: {password}")
    return feedback


def main():

    # Get password and assess it's strength
    print("\nPassword Strength Checker")
    password = input("\nEnter password: ")
    password_assessment = assess_password(password)

    # Display password feedback
    password_score = password_assessment["score"]
    password_crack_time = password_assessment['crack_times_display']["offline_slow_hashing_1e4_per_second"]
    print(f"\nScore: {password_score}/4")
    print(f"Crack time: {password_crack_time}\n")


    wants_feedback = input("Would you like some feedback?")

    #feedback = generate_feedback(password)
    #print(feedback)




main()