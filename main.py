import getpass
import zxcvbn as zx
import pprint as pretty_print




print("\nPassword Strength Checker")
password = input("\nEnter a password: ")
result = zx.zxcvbn(password)
pretty_print.pprint(result)





# Default to code!

# So use version control with git.
# Use chatGPT to provide feedback on how to build a strong password. 
# The more you code the more ideas you get and you search stuff up and expose yourself to new ideas
# So you learn what's possible 

# This is your phrase. 
# Default to code!