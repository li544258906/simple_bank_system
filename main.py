from bank_system import BankingSystem

def print_help():
    print("""
Commands:
    create <name> <initial_balance>  - Create a new account
    deposit <name> <amount>          - Deposit money into an account
    withdraw <name> <amount>         - Withdraw money from an account
    transfer <from> <to> <amount>    - Transfer money between accounts
    balance <name>                   - Check balance of an account
    save                             - Save the current state to file
    load                             - Load the state from file
    exit                             - Exit the program
""")

def main():
    bank = BankingSystem()
    
    print("Welcome to the Simple Banking System!")
    print_help()
    
    while True:
        try:
            command = input("> ").strip().split()
            if not command:
                continue
            
            cmd = command[0].lower()
            
            if cmd == "create":
                if len(command) != 3:
                    print("Usage: create <name> <initial_balance>")
                else:
                    name, balance = command[1], float(command[2])
                    bank.create_account(name, balance)
                    print(f"Account '{name}' created with balance {balance}.")
            
            elif cmd == "deposit":
                if len(command) != 3:
                    print("Usage: deposit <name> <amount>")
                else:
                    name, amount = command[1], float(command[2])
                    bank.deposit(name, amount)
                    print(f"Deposited {amount} to '{name}'.")
            
            elif cmd == "withdraw":
                if len(command) != 3:
                    print("Usage: withdraw <name> <amount>")
                else:
                    name, amount = command[1], float(command[2])
                    bank.withdraw(name, amount)
                    print(f"Withdrew {amount} from '{name}'.")
            
            elif cmd == "transfer":
                if len(command) != 4:
                    print("Usage: transfer <from> <to> <amount>")
                else:
                    from_name, to_name, amount = command[1], command[2], float(command[3])
                    bank.transfer(from_name, to_name, amount)
                    print(f"Transferred {amount} from '{from_name}' to '{to_name}'.")
            
            elif cmd == "balance":
                if len(command) != 2:
                    print("Usage: balance <name>")
                else:
                    name = command[1]
                    account = bank.get_account(name)
                    print(f"Balance for '{name}': {account.balance}")
            
            elif cmd == "save":
                bank.save_accounts()
                print("Accounts saved.")
            
            elif cmd == "load":
                bank.load_accounts()
                print("Accounts loaded.")
            
            elif cmd == "exit":
                print("Exiting...")
                break
            
            else:
                print("Unknown command.")
                print_help()
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()