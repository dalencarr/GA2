# Dalen Carr dcarr18@student.gsu.edu
# Matias Espinoza -- mespinoza2@student.gsu.edu
# Elizabeth Poythress–epoythress3@student.gsu.edu

# ask for password
pw = input("Please enter a password: ")
# check password length, make sure it contains letters and numbers
if 10 < len(pw) < 16 and pw.isalnum() and not pw.isalpha() and not pw.isnumeric():
    # verify password
    pw_check = input("Re-enter password: ")
    if pw == pw_check:
        print("Password created.")
    else:
        print("Passwords do not match.")

else:
    print("Your password should contain 10 to 15 characters and should be only numbers and letters.")
