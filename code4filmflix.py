import sqlite3
import os
print("Current Working Directory:", os.getcwd())

def create_database():
    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Creating table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tblFilms (
            filmID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            yearReleased INTEGER,
            rating TEXT,
            duration INTEGER,
            genre TEXT
        )
    ''')

    connection.commit()
    connection.close()


# Function to add a record to the database
def add_record():
    title = input("Enter the title: ")
    year_released = int(input("Enter the year released: "))
    rating = input("Enter the rating: ")
    duration = int(input("Enter the duration (in minutes): "))
    genre = input("Enter the genre: ")

    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Inserting the record into the table
    cursor.execute('''
        INSERT INTO tblFilms (title, yearReleased, rating, duration, genre)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, year_released, rating, duration, genre))

    connection.commit()
    connection.close()
    print("Record added successfully!")

# Function to delete a record from the database
def delete_record():
    film_id = int(input("Enter the filmID of the record to delete: "))

    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Deleting the record from the table
    cursor.execute('''
        DELETE FROM tblFilms WHERE filmID = ?
    ''', (film_id,))

    connection.commit()
    connection.close()
    print("Record deleted successfully!")

# Function to update a record in the database
def update_record():
    film_id = int(input("Enter the filmID of the record to update: "))
    field = input("Enter the field to update (title/yearReleased/rating/duration/genre): ")
    new_value = input(f"Enter the new value for {field}: ")

    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Updating the record in the table
    cursor.execute(f'''
        UPDATE tblFilms SET {field} = ? WHERE filmID = ?
    ''', (new_value, film_id))

    connection.commit()
    connection.close()
    print("Record updated successfully!")

# Function to print all records in tblFilms
def print_all_records():
    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Fetching all records from the table
    cursor.execute('''
        SELECT * FROM tblFilms
    ''')
    records = cursor.fetchall()

    for record in records:
        print(record)

    connection.close()

# Function to print details of all films
def print_all_films():
    print_all_records()

# Function to print all films of a particular genre
def print_films_by_genre():
    genre = input("Enter the genre to filter: ")

    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Fetching records based on genre
    cursor.execute('''
        SELECT * FROM tblFilms WHERE genre = ?
    ''', (genre,))
    records = cursor.fetchall()

    for record in records:
        print(record)

    connection.close()

# Function to print all films of a particular year
def print_films_by_year():
    year = int(input("Enter the year to filter: "))

    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Fetching records based on year
    cursor.execute('''
        SELECT * FROM tblFilms WHERE yearReleased = ?
    ''', (year,))
    records = cursor.fetchall()

    for record in records:
        print(record)

    connection.close()

# Function to print all films of a particular rating
def print_films_by_rating():
    rating = input("Enter the rating to filter: ")

    connection = sqlite3.connect("filmflix.db")
    cursor = connection.cursor()

    # Fetching records based on rating
    cursor.execute('''
        SELECT * FROM tblFilms WHERE rating = ?
    ''', (rating,))
    records = cursor.fetchall()

    for record in records:
        print(record)

    connection.close()

# Main function to run the application
def main():
    while True:
        print("\nOptions Menu:")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Amend a record")
        print("4. Print all records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            delete_record()
        elif choice == '3':
            update_record()
        elif choice == '4':
            print("\nReports Menu:")
            print("1. Print details of all films")
            print("2. Print all films of a particular genre")
            print("3. Print all films of a particular year")
            print("4. Print all films of a particular rating")
            print("5. Exit")

            report_choice = input("Enter your report choice: ")

            if report_choice == '1':
                print_all_films()
            elif report_choice == '2':
                print_films_by_genre()
            elif report_choice == '3':
                print_films_by_year()
            elif report_choice == '4':
                print_films_by_rating()
            elif report_choice == '5':
                break
            else:
                print("Invalid report choice. Please try again.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
