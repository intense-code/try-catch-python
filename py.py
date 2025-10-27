
#👾💻Final Challenge: Create a program that simulates an ATM withdrawal process. The program should:
#Steps:


account_balance = 1500
#Raise an exception if the input is invalid (non-numeric or negative).
try:
    
    print("try Bank of U")
    #Allow the user to input an amount to withdraw.
    withdraw = input("Amount to Withdraw ")
    withdrawl_amount = int(withdraw)
    if withdrawl_amount > account_balance:
        print("Funds Not Valid")
    print(f"$, {withdrawl_amount}$$", )
except ValueError:
    print("Value Error enter a quntity number 1 or more")

else:
    print("No exceptions Occured in the Try Block")

finally:
    withdrawl_amount = 0
    withdrawl_amount += withdrawl_amount
    #Always display the remaining balance, even if an error occurs.
    print("Withdrawl & Account Balance ",account_balance ,withdrawl_amount)



