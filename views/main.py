from views.App import App
from views.user import User

if __name__ == '__main__':
    app = App()
    print("Welcome to Eden Shopping ")
    print(" Enter the following details to register ")

    first_name = input(" Enter your first name :")
    last_name = input(" Enter your last name :")
    email = input(" Enter your email :")
    password = input("Enter your password :")
    confirm_password = input("Confirm your password :")
    phone_number = input("Enter phone_number :")

    app = App()
    print("Login Page")
    email = input("Enter email :")
    password = input("Enter Password :")

    user = User(email, password, )

    app.registerUser(user)

    print(app.users[0])

    user = User(email, password)
    app.loginUser(user)
    print(app.users[0])
