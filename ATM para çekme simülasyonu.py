#BANK SIMULATION
current_balance = 1000
while True:
    print("1 - CURRENT BALANCE")
    print("2 - DEPOSIT MONEY")
    print("3 - WITHDRAW MONEY")
    print("4 - EXIT")

    select = input("Enter an option: ")

    if select == "1":
    
        print(f"Your current balance {current_balance} TL")

    elif select == "2":
        deposit_money = int(input("enter the amount: "))
        current_balance += deposit_money
        print(f"deposited amount {deposit_money} TL")

    elif select == "3":
        withdraw_money = int(input("enter the amount: "))
        current_balance -= withdraw_money
        print(f"withdraw amount {withdraw_money} TL")

    elif select == "4":
        print("EXITING SYSTEM...\nTRANSACTION COMPLETED. ")
        break


    
    



        
    




    
