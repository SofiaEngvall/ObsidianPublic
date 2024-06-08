# Define the file path to /etc/passwd
passwd_file_path = '/etc/passwd'

# Initialize empty lists for root, user, and service accounts
root_accounts = []
user_accounts = []
service_accounts = []

try:
    # Open and read the /etc/passwd file
    with open(passwd_file_path, 'r') as passwd_file:
        for line in passwd_file:
            fields = line.strip().split(':')

            # Check if the account is a root account (UID 0)
            if fields[2] == '0':
                root_accounts.append(fields[0])
            # Check if the account is a service account (UID between 1 and 999)
            elif 1 <= int(fields[2]) <= 999:
                service_accounts.append(fields[0])
            # All other accounts are considered user accounts
            else:
                user_accounts.append(fields[0])

    # Sort the lists alphabetically
    root_accounts.sort()
    user_accounts.sort()
    service_accounts.sort()

    # Print the accounts in the specified order: root, user, service
    print("Root Accounts:")
    for account in root_accounts:
        print(account)

    print("\nUser Accounts:")
    for account in user_accounts:
        print(account)

    print("\nService Accounts:")
    for account in service_accounts:
        print(account)

except FileNotFoundError:
    print(f"File not found: {passwd_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
