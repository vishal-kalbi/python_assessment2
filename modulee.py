import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7665901107",
    database="vishal"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create the users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        role VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# Create the medicines table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        manufacturer VARCHAR(255) NOT NULL,
        stock INT NOT NULL
    )
""")

# Function to register a user
def register_user(role):
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Insert the new user into the database
    cursor.execute("""
        INSERT INTO users (role, username, password)
        VALUES (%s, %s, %s)
    """, (role, username, password))

    db.commit()
    print("User registered successfully!")

# Function to perform user login
def login(role):
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the user credentials exist in the database
    cursor.execute("""
        SELECT * FROM users
        WHERE role = %s AND username = %s AND password = %s
    """, (role, username, password))

    user = cursor.fetchone()

    if user is not None:
        print("Login successful!")
        if role == "Pharmacy Manager":
            pharmacy_manager_menu()
        elif role == "Admin":
            admin_menu()
    else:
        print("Invalid credentials. Please try again.")

# Function to add a new medicine
def add_medicine():
    name = input("Enter medicine name: ")
    manufacturer = input("Enter manufacturer name: ")
    stock = int(input("Enter stock quantity: "))

    # Insert the new medicine into the database
    cursor.execute("""
        INSERT INTO medicines (name, manufacturer, stock)
        VALUES (%s, %s, %s)
    """, (name, manufacturer, stock))

    db.commit()
    print("Medicine added successfully!")

# Function to view all medicines
def view_medicines():
    cursor.execute("""
        SELECT * FROM medicines
    """)

    medicines = cursor.fetchall()

    if len(medicines) > 0:
        print("Medicine List:")
        for medicine in medicines:
            print("ID:", medicine[0])
            print("Name:", medicine[1])
            print("Manufacturer:", medicine[2])
            print("Stock:", medicine[3])
    else:
        print("No medicines found.")

# Function to delete a medicine
def delete_medicine():
    medicine_id = int(input("Enter medicine ID: "))

    # Delete the medicine from the database
    cursor.execute("""
        DELETE FROM medicines
        WHERE id = %s
    """, (medicine_id,))

    db.commit()
    print("Medicine deleted successfully!")

# Function to view all users (only available to Admin)
def view_users():
    cursor.execute("""
            SELECT * FROM users
    """)

    users = cursor.fetchall()

    if len(users) > 0:
        print("User List:")
        for user in users:
            print("ID:", user[0])
            print("Role:", user[1])
            print("Username:", user[2])
    else:
        print("No users found.")

# Function to view all medicines (only available to Admin)
def view_medicines_admin():
    cursor.execute("""
        SELECT * FROM medicines
    """)

    medicines = cursor.fetchall()

    if len(medicines) > 0:
        print("Medicine List:")
        for medicine in medicines:
            print("ID:", medicine[0])
            print("Name:", medicine[1])
            print("Manufacturer:", medicine[2])
            print("Stock:", medicine[3])
    else:
        print("No medicines found.")

# Pharmacy Manager menu
def pharmacy_manager_menu():
    while True:
        print("\nPharmacy Manager Menu")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Delete Medicine")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            view_medicines()
        elif choice == "3":
            delete_medicine()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. View All Managers")
        print("2. View All Medicines")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_users()
        elif choice == "2":
            view_medicines_admin()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Main program loop
while True:
    print("\nPharmacy Management System")
    print("1. Pharmacy Manager")
    print("2. Admin")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user("Pharmacy Manager")
        login("Pharmacy Manager")
    elif choice == "2":
        register_user("Admin")
        login("Admin")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
db.close()

       
