def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact not found"
    contacts[name] = phone
    return "Contact changed."


def show_contact(args, contacts):
    name = args[0]
    return contacts[name]


def all_contacts(contacts):
    contact_strings = []
    if contacts:
        for name, phone in contacts.items():
            contact_strings.append(f"Name: {name}, phone: {phone}.")
    else:
        contact_strings.append("No contacts available.")
    return contact_strings


def main():

    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print("Good bye!")
            break

        elif command == 'hello':
            print("How can I help you?")

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_contact(args, contacts))

        elif command == 'all':
            contacts_strings = all_contacts(contacts)
            for contact_string in contacts_strings:
                print(contact_string)

        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
