
#👾💻Final Challenge: Create a program that simulates an ATM withdrawal process. The program should:
#Steps:



#Raise an exception if the input is invalid (non-numeric or negative).
try:

    print("try")
    #Allow the user to input an amount to withdraw.
    withdraw = input("Amount to Withdraw ")
    withdrawl_amount = int(withdraw)
    print(f"$, {withdrawl_amount}$$", )
except ValueError:
    print("Value Error enter a quntity number 1 or more")

else:
    print("No exceptions Occured in the Try Block")

finally:
    withdrawl_amount = 0
    withdrawl_amount += withdrawl_amount
    print("Withdrawl ",withdrawl_amount)
#Ensure that the withdrawal doesn’t exceed the account balance, raising an appropriate exception.
#Always display the remaining balance, even if an error occurs.
#account_balance = 1500

