#BANK SIMULATION
current_balance = 1000

while True:
    print("1 - CURRENT BALANCE")
    print("2 - DEPOSİT MONEY")
    print("3 - WİTHDRAW MONEY")
    print("4 - EXİT")

    select = input("Enter an option: ")

    if select == "1":
        print(f"Your current balance {current_balance} TL")

    elif select == "2":
        deposit_money = int(input("enter the amount: "))
        current_balance += deposit_money
        print(f"deposited amount {deposit_money} TL")

    elif select == "3":
        withdraw_money = int(input("enter the amount: "))
        if withdraw_money <= current_balance:
           current_balance -= withdraw_money
           print(f"withdraw amount {withdraw_money} TL\n remaining amount {current_balance}")
        else:
           print("This amount exceeds the current balance.")
        
    elif select == "4":
        print("EXİTİNG SYSTEM...\nTRANSACTİON COMPLETED. ")
        break


    
    



        
    




    
