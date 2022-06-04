def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            website, uName, pswd = data.split('|')
            print("Website: ", website, "Username: ", uName, "Password: ", pswd)

def add():
    websiteName = input("Please enter the website name: ")
    userName = input("Please enter your username for " + websiteName + " : ")
    password = input("Please enter the password: ")

    with open('password.txt', 'a') as f:
        f.write(websiteName + " | " + userName + " | " + password + "\n")

while True:
    mode = input("Would you like to add a new password or view the existing ones (Add/View)? Or press Q to quit. ").lower()

    if mode == "q":
        quit()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
        continue