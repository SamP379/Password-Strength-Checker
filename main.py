import getpass
import zxcvbn as zx
import pprint as pretty_print



def check_password(password : str) -> dict:
    password_feedback = zx.zxcvbn(password)
    return password_feedback


def main():

    # Get password and assess it
    print("\nPassword Strength Checker")
    password = input("\nEnter a password: ")
    password_feedback = check_password(password)

    # Display password feedback
    print(f"Score: {password_feedback["score"]}/4")
    print(f"{password_feedback['crack_times_display']["offline_slow_hashing_1e4_per_second"]}")
    print(password_feedback["feedback"]["suggestions"])


    # Default to code!