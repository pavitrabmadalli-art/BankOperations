def bankOper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updateBal = totalBal - withdraw

    return totalBal, updateBal

if __name__== "__main__":
    initialBal = int(input("Enter amount as initial Balance: "))
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter withdraw amount: "))

    totalBal, updateBal = bankOper(initialBal, deposit, withdraw)

    print("Total Balance: ", totalBal)
    print("Updated Balance: ", updateBal)