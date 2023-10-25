from datetime import datetime, timedelta, date
from collections import defaultdict

def get_birthdays_per_week(users):
    # Prepare data
    current_date = date.today()
    birthdays = defaultdict(list)

    # Iterate through users
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days
        if delta_days >= 0 and delta_days < 7:
            day_of_week = (current_date + timedelta(days=delta_days)).strftime('%A')
            birthdays[day_of_week].append(name)

    # Print the result
    for day, celebrants in birthdays.items():
        print(f"{day}: {', '.join(celebrants)}")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added."

def change_contact(username, new_phone, contacts):
    if username in contacts:
        contacts[username] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(username, contacts):
    if username in contacts:
        return contacts[username]
    else:
        return "Contact not found."

def show_all(contacts):
    return "\n".join(f"{username}: {phone}" for username, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you.")
        
        elif command == "add":
            if len(args) == 2:
                username, phone = args
                print(add_contact(username, phone, contacts))
            else:
                print("Invalid command.")
        
        elif command == "change":
            if len(args) == 2:
                username, new_phone = args
                print(change_contact(username, new_phone, contacts))
            else:
                print("Invalid command.")

        elif command == "phone":
            if len(args) == 1:
                username = args[0]
                result = show_phone(username, contacts)
                print(result)
            else:
                print("Invalid command.")

        elif command == "all":
            result = show_all(contacts)
            print(result)
        
        elif command == "birthdays":
            # Example users list with birthdays
            users = [
                {"name": "Anton Kryvosheienko", "birthday": date(1990, 11, 23)},
                {"name": "Tesolkina Kateryna", "birthday": date(1990, 4, 12)},
                {"name": "Kuzin Vadym", "birthday": date(2023, 10, 30)},
                {"name": "Svetlana Negrova", "birthday": date(1940, 4, 12)},
                {"name": "Pishokha Asya", "birthday": date(2039, 1, 30)}
            ]

            get_birthdays_per_week(users)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
