# simple_bank_system
## Prerequisites
- **Python 3.x**: Ensure that Python 3 is installed on your system. You can download Python from [python.org](https://www.python.org/).


## How to Use the System

###	1.	Run the Script:
	•	Save the code to a file
	•	Run the script from the terminal with python main.py
###	2.	Commands:
	•	Create Account: create <name> <initial_balance>
	•	Deposit Money: deposit <name> <amount>
	•	Withdraw Money: withdraw <name> <amount>
	•	Transfer Money: transfer <from_name> <to_name> <amount>
	•	Check Balance: balance <name>
	•	Save Accounts: save
	•	Load Accounts: load
	•	Exit: exit
###	3.	Example Usage:
	•	To create an account with an initial balance: create Alice 100
	•	To deposit money: deposit Alice 50
	•	To withdraw money: withdraw Alice 20
	•	To transfer money from Alice to Bob: transfer Alice Bob 30
	•	To check balance: balance Alice
	•	To save the state: save
	•	To load the state: load
	•	To exit: exit


## How to Test the System
	•	Run the script from the terminal with python -m unittest discover -s tests
    •	It will produce a file named test_accounts.csv

