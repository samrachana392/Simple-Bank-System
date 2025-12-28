bank_data= {
   "aliace": 1000,
   "Bob": 500
}
def Deposit(user):
    amount = float(input("Enter amount to deposit: "))
    if amount>0:
        bank_data[user] += amount
        print(f"{amount} deposited successfully!")
    else:
        print("Invalid amount, amount must be greater than 0")


def Withdraw(user):
    amount = float(input("Enter amount you want to withdraw: "))
    if (amount <=0):
        print("invalid amount, must be grater than 0")
    elif amount > bank_data[user]:
        print("Insufficient balance")
    else:
        bank_data[user]-=amount
        print("amount withdrawn successfully!")

def View_balance(user):
    print(f"Balance: {bank_data[user]}")

def exit_system(user):
    print("Thank you for visiting us!")
    exit()


def menu():
    print("1 - Deposit money")
    print("2 - Withdraw money")
    print("3 - View Balance")
    print("4 - Exit")

menu_actions={
    1 : Deposit,
    2 : Withdraw,
    3 : View_balance,
    4 : exit_system
} # this dictionary must be used after all functions are defined

# Main Program 
user=input("Enter your name: ")

if user not in bank_data:
    print("No user found. Creating new account.")
    bank_data[user]=0
    print("Account created with 0 balance.")

while True: 
    menu()

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Invalid input, enter a number.")
        continue # skips all the remaining part of loop and goes to the next iteration, here next iteration is it again goes to the start of loop

    choice = int(choice)

    # calling function directly form dictionary menu_actions
    action=menu_actions.get(choice)
    if action:
        action(user)
    else:
        print("invalid choice")
    input("Press enter to return to the menu")