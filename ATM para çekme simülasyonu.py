#BANK SIMULATION
current_balance = 1000
while True:
    
    print("1- check balance")
    print("2- deposit money")
    print("3- get money")
    print("4- exit")
    select = input("Enter an option.")

    if select == "1":
        print(f"Checking balance...\nCurrent balance = {current_balance} TL")

    elif select == "2":
        deposit = input("enter deposit amount: ")
        print(f"deposited amount: {deposit}")

    elif select == "3":
        withdrawal_amount = input("enter the amount you want to withdraw: ")
        print(f"withdrawn amount: {withdrawal_amount}")

    elif select == "4":
        print("exiting...")
        break


    
    



        
    




    
