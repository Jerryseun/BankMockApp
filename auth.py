# register
# - username, password, email,
# - UserId
# -

# login
# account number and password


# bank operations

# Initialize the system

import random
from validator import validate
import getpass4
from email_validator import validate_email, EmailNotValidError

database = {
    1536626349: ["Jeremiah", "Adetunji", "adetunjijeremiah1@gmail.com", "passwordJerry"]
}

# dictionary gets updated as new_user register


def init():
    print('Welcome to BankPHP')
    have_account = int(input('Do you have account with us?: 1. Yes 2. No \n'))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('You have selected an invalid option')
        init()


def login():
    account_number_from_user = int(input("What is your account number? \n"))

    if account_number_from_user in database.keys():
        #is_valid_account_number = account_number_from_user
        password = getpass4.getpass(prompt="What is your password? \n")
        #password = getpass("What is your password?: \n")
        for password in database.values():
            bankOperation("user")
        else:
            print("Invalid password")
            login()
    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    # is_account_registered = False
    # while not is_account_registered:
    print('****** Register ******')

    user_email = input('What is your email? \n') #validate required

    # validate email
    try:
        # Validate.
        valid = validate_email(user_email)

        # Update with the normalized form.
        email = valid.email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        register()
    first_name = input('What is your first_name? \n') #validate required
    last_name = input('What is your last_name? \n') ##validate required
    password = input("Create a password for yourself \n") #validate required

    account_number = generateAccountNumber()

    database[account_number] = {first_name, last_name, user_email, password, 0}

    print('Your account has been created')
    print('== ==== ====== ===== ===')
    print('Your account number is: %s' % account_number)
    print('Make sure you keep it safe')
    print('== ==== ====== ===== ===')

    # Activate account and go back to login function
    login()


def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[0]))
    selected_option = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Complaint (4) Logout (5) '
                                'Exist \n'))

    if selected_option == 1:
        deposit_operation(current_balance)
    elif selected_option == 2:
        withdraw_operation(current_balance)
    elif selected_option == 3:
        complaint_operation()
    elif selected_option == 4:
        print("Thanks for banking with BankPHP")
        print("==== **** ==== **** ==== ****")
        init()
    elif selected_option == 5:
        exit()
    else:
        print('Invalid Option Selected')
        bankOperation(user)

current_balance = 15000


def deposit_operation(current_balance):
    balance = float(input('How much would you like to deposit? \n'))
    available_balance = current_balance + balance
    print(f"The deposit of {balance} is successfully ")
    print(f"Your new balance is {available_balance}")
    another_operation()


def withdraw_operation(available_balance):
    withdraw_amount = float(input('How much would you like to withdraw? \n'))
    # catch withdrawal amount input error
    if available_balance > withdraw_amount:
        print('Take your cash')
        # deduct withdrawn amount form current balance
        new_balance = available_balance - withdraw_amount
        current_balance = new_balance
        # display current balance
        print(f"Your available balance is {current_balance}")
    else:
        print("Insufficient balance")
        # perrform another bank operation
    another_operation()



def complaint_operation():
    input('What issue will you like to report? \n')
    print('Thank you for contacting us. Your complaint will be treated with highest urgency')
    another_operation()


def another_operation():
    option = int(input("Would you like to perform another operation? 1. Yes 2. No \n"))
    if option == 1:
        bankOperation("User")
    elif option == 2:
        exit()
    else:
        print("Invalid option: Select 1 or 2")
        another_operation()


def generateAccountNumber():
    return random.randrange(1111111111, 2222222222)


#def get_current_balance(user_details):
    #return user_details[4]


### ACTUAL BANK SYSTEM ###
init()
# print (generateAccountNumber())
