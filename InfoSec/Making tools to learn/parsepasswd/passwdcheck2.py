def is_service_account(uid, shell):
    # Define the UID range for user accounts (adjust as needed)
    user_uid_range = (1000, 65534)  # Common range for user accounts

    # Check if UID falls outside the user account range or shell is restricted
    return uid < user_uid_range[0] or shell in ['/sbin/nologin', '/bin/false']


def differentiate_accounts():
    try:
        with open('/etc/passwd', 'r') as passwd_file:
            accounts = []
            for line in passwd_file:
                parts = line.split(':')
                username = parts[0]
                uid = int(parts[2])
                shell = parts[-1].strip()
                accounts.append((username, uid, shell))

            # Sort the accounts based on user accounts first and then by shell path
            sorted_accounts = sorted(accounts, key=lambda x: (
                is_service_account(x[1], x[2]), x[2]))

            root_header = "Root Accounts:"
            user_header = "User Accounts:"
            service_header = "Service Accounts:"
            current_header = None

            for username, _, shell in sorted_accounts:
                if username == 'root':
                    if current_header != root_header:
                        print(root_header)
                        print("{:<20} {:<10}".format("Username", "Shell Path"))
                        print("=" * 30)
                        current_header = root_header
                elif is_service_account(_, _):
                    if current_header != service_header:
                        print(service_header)
                        print("{:<20} {:<10}".format("Username", "Shell Path"))
                        print("=" * 30)
                        current_header = service_header
                else:
                    if current_header != user_header:
                        print(user_header)
                        print("{:<20} {:<10}".format("Username", "Shell Path"))
                        print("=" * 30)
                        current_header = user_header

                if current_header:
                    print("{:<20} {:<10}".format(username, shell))

    except FileNotFoundError:
        print("/etc/passwd not found. Are you running this on a Linux system?")


if __name__ == "__main__":
    differentiate_accounts()
