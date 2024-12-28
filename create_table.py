import mysql.connector

# Connect to MySQL
def connect_to_mysql():
    connection=mysql.connector.connect(host="localhost",user="root",password="Naresh@28072004")
    print("Connected to MySQL successfully!")
    return connection

# Create database and table
def create_database_and_table():
    connection=connect_to_mysql()
    cursor=connection.cursor()

    # Database and table creation
    database_name="simple_database"
    print(f"Database '{database_name}' and table 'users' created successfully.")
    # Clean up
    cursor.close()
    connection.close()

# Insert a record
def insert_record():
    connection=connect_to_mysql()
    connection.database="simple_database"
    cursor = connection.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    cursor.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", (name, age, email))
    connection.commit()
    print("Record inserted successfully.")

    cursor.close()
    connection.close()

# Display all records
def display_records():
    connection=connect_to_mysql()
    connection.database="simple_database"
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM users")
    records=cursor.fetchall()
    if records:
        print("\nUsers Table Records:")
        for record in records:
            print(record)
    else:
        print("No records found.")

    cursor.close()
    connection.close()

# Update a record
def update_record():
    connection = connect_to_mysql()
    connection.database = "simple_database"
    cursor = connection.cursor()

    record_id = int(input("Enter record ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    email = input("Enter new email: ")
    cursor.execute("UPDATE users SET name=%s, age=%s, email=%s WHERE id=%s", (name, age, email, record_id))
    connection.commit()
    print("Record updated successfully.")

    cursor.close()
    connection.close()

# Delete a record
def delete_record():
    connection = connect_to_mysql()
    connection.database = "simple_database"
    cursor = connection.cursor()

    record_id = int(input("Enter record ID to delete: "))
    cursor.execute("DELETE FROM users WHERE id=%s", (record_id,))
    connection.commit()
    print("Record deleted successfully.")

    cursor.close()
    connection.close()

# Main menu
def main():
    # Create database and table on first run
    create_database_and_table()

    while True:
        print("\nMenu:")
        print("1. Insert a record")
        print("2. Display records")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            insert_record()
        elif choice == "2":
            display_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
