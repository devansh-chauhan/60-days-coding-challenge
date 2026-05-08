valid_username = "admin"
valid_password = "admin234"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter your username:")
    password = input("Enter your password:")

    if username == valid_username and password == valid_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Invalid username or password! Attempts left:{remaining_attempts}")

if attempts == max_attempts:
    print("Too many failed attempts.")