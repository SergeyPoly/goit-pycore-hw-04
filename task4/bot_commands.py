def add_contact(args: list, contacts: dict) -> str:
    if len(args) < 2:
        return "Missing arguments (name or phone)"
    name, phone = args

    if name in contacts:
        return change_contact(args, contacts)
    
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    if len(args) < 2:
        return "Missing arguments (name or phone)"
    name, phone = args

    if name not in contacts:
        return f"No such name: '{name}' in contacts"
    
    contacts[name] = phone
    return "Contact updated."
    

def show_phone(args: list, contacts: dict) -> str:
    if not args:
        return "Missing argument (name)"
    
    name = args[0]
    if name not in contacts:
        return f"No such name: '{name}' in contacts"
    
    return contacts[name]


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts available."
    
    return "\n".join(f"{name:<10}: {phone}" for name, phone in contacts.items())
