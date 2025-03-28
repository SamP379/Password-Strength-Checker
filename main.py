import getpass
import zxcvbn as zx
import pprint as pretty_print




print("\nPassword Strength Checker")
password = input("\nEnter a password: ")
result = zx.zxcvbn(password)

print(f"Score: {result["score"]}/4")
print(f"{result['crack_times_display']["offline_slow_hashing_1e4_per_second"]}")
print(result["feedback"]["suggestions"])