try:
    print(" WELCOME!!")
    choice = int(input("Enter your account type: \n 1) Current account\n 2) Saving account\n 3) Exit \n "))
    if choice == 3:
        print("You choosed to Exit")
    elif choice == 1 or choice == 2:
        def account_details(acc_num,pin):
            if acc_num == account[0] and pin == pinn[0]:
                print(f"Yours account number is: {acc_num}")
                print(f"Your account balance is: {balance[0]}")
                if with_amount <= balance[0]:
                    print("processing amount",with_amount)
                    return f"Your Remaining balance is: {balance[0] - with_amount}"

                else:
                    return "Insufficient Balance"

            elif acc_num == account[1] and pin == pinn[1]:
                print(f"Yours account number is: {acc_num}")
                print(f"Your account balance is: {balance[1]}")
                if with_amount <= balance[1]:
                    print("processing amount",with_amount)
                    return f"Your Remaining balance is: {balance[1] - with_amount}"

                else:
                    return "Insufficient Balance"
            elif acc_num == account[2] and pin == pinn[2]:
                print(f"Yours account number is: {acc_num}")
                print(f"Your account balance is: {balance[2]}")
                if with_amount <= balance[2]:
                    print("processing amount: ",with_amount)
                    return f"Your Remaining balance is: {balance[2] - with_amount}"

                else:
                    return "Insufficient Balance"
            else:
                return f"Please enter correct account number or pin"

        account = ["123","456","789"]
        pinn = ["199","666","999"]
        balance = [200000.0,3900000.0,450000.34]
        acc_num = input("Please enter your account number: ")
        pin = input("Please enter your pin number: ")
        with_amount = float(input("Enter the withdrawl amount"))
        if with_amount < 0:
            print(f"enter the correct amount!!")
        else:
            print(account_details(acc_num,pin))
    else:
        print("Please enter the Valid Choice")
except ValueError:
    print("Error: Please enter correct value...")


