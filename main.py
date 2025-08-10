import json
from tabulate import tabulate

# Load contracts from JSON file
def load_contracts():
    try:
        with open("contracts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # returns empty list if file not found

# Save contracts back to JSON
def save_contracts(contracts):
    with open("contracts.json", "w") as f:
        json.dump(contracts, f, indent=4)

# This function displays all contracts in a table
def view_contracts(contracts):
    if not contracts:
        print("\nNo contracts found.")
        return
    table = [
        [c["player"], c["team"], c["years"], f"${c['salary']} million"] 
        for c in contracts
    ]
    print("\n" + tabulate(table, headers=["Player", "Team", "Years", "Salary"], tablefmt="grid"))

# Adds a new contract to the list and saves it to the JSON file
def add_contract(contracts):
    player = input("Enter player name: ")
    team = input("Enter team: ")
    years = input("Enter contract years: ")
    salary = float(input("Enter salary (in millions): "))
    contracts.append({
        "player": player,
        "team": team,
        "years": years,
        "salary": salary
    })
    save_contracts(contracts)
    print(f"\nContract for {player} added successfully.")

def filter_by_name(contracts, needle: str):
    return [c for c in contracts if needle.lower() in c["player"].lower()]

def filter_by_salary(contracts, threshold: float):
    return [c for c in contracts if float(c["salary"]) > float(threshold)]

# Search/filter contracts
def search_contracts(contracts):
    choice = input("\nSearch by (1) Player name or (2) Salary above: ")
    if choice == "1":
        name = input("Enter player name to search: ").lower()
        results = filter_by_name(contracts, name)
    elif choice == "2":
        threshold = float(input("Enter salary threshold (in millions): "))
        results = filter_by_salary(contracts, threshold)
    else:
        print("Invalid choice.")
        return

    if results:
        view_contracts(results)
    else:
        print("\nNo matching contracts found.")

# Main menu
def main():
    contracts = load_contracts()

    while True:
        print("\n--- SportsPlay Contract Tracker ---")
        print("1. View all contracts")
        print("2. Add new contract")
        print("3. Search contracts")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_contracts(contracts)
        elif choice == "2":
            add_contract(contracts)
        elif choice == "3":
            search_contracts(contracts)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()