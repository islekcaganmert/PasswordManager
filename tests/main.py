from PasswordManager import Vault
from TheProtocols import TheProtocols, Session
from getpass import getpass
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

password = getpass()
vault_password = password
s: Session = TheProtocols(
    package_name='me.islekcaganmert.theprotocols.nonstandard.passwordmanager',
    permissions=[
    ]
).create_session(
    email='islekcaganmert@hereus.net',
    password=password
)

vault = None
while vault is None:
    try:
        vault = Vault(
            (s.data, s.data),
            vault_password
        )
    except ValueError as e:
        print("Your vault password is different than your account password.")
        vault_password = getpass("Vault password: ")
auto_save = s.preferences().get("auto_save", True)

while True:
    input(s.data({'ok': 'ok'}))
    input(s.data())
    clear()
    print(f"Welcome, {s.id}!\n")
    print("1. Add a credential")
    print("2. Get a credential")
    print("3. Remove a credential")
    print("4. Settings")
    print("s. Save")
    print("q. Exit")
    choice = input("\n> ")
    if choice == "1":
        domain = input("Domain: ")
        username = input("Username: ")
        password = input("Password: ")
        vault.add_credentials(domain, username, password)
        if auto_save:
            vault.save()
    elif choice == "2":
        domain = input("Domain: ")
        credential = vault.get_credentials(domain)
        print(f"Username: {credential.username}")
        print(f"Password: {credential.password}")
        print(f"Notes: {credential.notes}")
        input()
    elif choice == "3":
        domain = input("Domain: ")
        vault.remove_credential(domain)
        if auto_save:
            vault.save()
    elif choice == "4":
        print()
        print(f"1. [{'x' if auto_save else ' '}] Auto save")
        print("2. Sync vault password to account password")
        print("3. Change vault password")
        print('4. Erase all data')
        choice = input("\n> ")
        if choice == "1":
            auto_save = not auto_save
            p = s.preferences()
            p.update({"auto_save": auto_save})
            s.preferences(p)
        elif choice == "2":
            vault.save()
            vault_password = password
            vault = Vault(
                (s.data, s.data),
                vault_password
            )
        elif choice == "3":
            vault.save()
            vault_password = getpass()
            vault = Vault(
                (s.data, s.data),
                vault_password
            )
        elif choice == "4":
            s.data({})
            s.preferences({})
            break
        else:
            print("Invalid choice.")
    elif choice.lower() == "s":
        vault.save()
    elif choice.lower() == "q":
        vault.save()
        break
    else:
        print("Invalid choice.")
