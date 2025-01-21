import json


def remove_user(user_to_be_deleted: str, bank_path: str = "bank.json", auth_path: str = "auth.json" , clients_path: str = "clients.json"):


    # here I need to change to make this more efficient
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    with open(auth_path, "r") as f:
        credentials = json.loads(f.read())

    with open(clients_path, "r") as f:
        clients = json.loads(f.read())

    accounts.pop(user_to_be_deleted, None)
    credentials.pop(user_to_be_deleted, None)
    clients.pop(user_to_be_deleted, None)

    with open(bank_path, "w") as f:
        f.write(json.dumps(accounts, indent=4))

    with open(auth_path, "w") as f:
        f.write(json.dumps(credentials, indent=4))

    with open(clients_path, "w") as f:
        f.write(json.dumps(clients, indent=4))






def add_new_client(username: str, password: str, initial_balance: int, currency: str, auth_path: str = "auth.json", bank_path: str = "bank.json"):

    try:
        file = open(auth_path, "r")
        credentials = json.load(file)
        file.close()
    except FileNotFoundError:
        credentials = {}

    try:
        file = open(bank_path, "r")
        accounts = json.load(file)
        file.close()
    except FileNotFoundError:
        accounts = {}

    if username in credentials:
        print("User existent. Introduceti un alt username")
        return

    credentials[username] = password
    file = open(auth_path, "w")
    json.dump(credentials, file, indent=4)
    file.close()

    accounts[username] = {"value": initial_balance, "currency": currency}
    file = open(bank_path, "w")
    json.dump(accounts, file, indent=4)
    file.close()

    print(f"Ai adaugat cu succes un client nou: {username} cu soldul: {initial_balance} {currency}.")
