## Import required libraries

import psycopg2
from psycopg2 import sql

class Database:
    """"
    this class handles:
    1. creating database (if not exits)
    2. connecting to database
    3. creating tables
    4. inserting data
    5. updating data
    6. deleting data
    7.closing database
    """

    # Constructor (runs automatically ehen object is created)
    def __init__(self):
        print("\n Initializing Database setup...")

        # Database configuration
        self.db_name="anuska_db"
        self.user ="postgres"
        self.password ="Rekha123"
        self.host ="localhost"
        self.port ="5432"
    # Step 1 : Check and create database if not exits
    def create_database_if_not_exists(self):
        print("\n Step 1: Checking database...")

        try:
            # Connect to default 'postgres' database
            conn = psycopg2.connect(
                dbname= "postgres",
                user= self.user,
                password= self.password,
                host= self.host,
                port= self.port
            )

            # Enable auto commit (needed to create database)
            conn.autocommit = True

            # Create cursor to execute SQL queries
            cursor = conn.cursor()

            # Check if database already exists

            cursor.execute("SELECT 1 from pg_database WHERE datname =%s",
                           (self.db_name,)
                           )
            exists = cursor.fetchone()

            # If exists --> print message
            if exists:
                print(f"Database {self.db_name} already exists")

            #if not exists --> create database
            else:
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}") .format(
                    sql.Identifier(self.db_name)
                )
            )
                print(f"Database {self.db_name} created successfully")

            # Close cursor and connection

            cursor.close()
            conn.close()

        except Exception as e:
            print("Error while creating database",e)


    # Step 2: Connect to the created databse

    def connect(self):
        print("\n Step 2: Establishing Connection...")

        try:
            #Connect to the actual database
            self.conn = psycopg2.connect(
                dbname= self.db_name,
                user= self.user,
                password= self.password,
                host= self.host,
                port= self.port
            )

            #Create Cursor
            self.cursor = self.conn.cursor()
            print(f"Connected to {self.db_name} database")

        except Exception as e:
            print("Connection failed:", e)

    #Step 3 : Create table

    def create_tables(self):
        print("\n Step 3: Creating tables...")


        try:
            #SQL Query to create table
            query="""(
            CREATE TABLE IF NOT EXISTS students 
            roll_no SERIAL PRIMARY KEY,
            name VARCHAR(100),
            dob DATE,
            education VARCHAR(100),
            address TEXT
            );
            """

            #Execute Query
            self.cursor.execute(query)
            #Save Changes
            self.conn.commit()
            print("Table created successfully")

        except Exception as e:
            print("Table creation failed:", e)

    # Step 4 : Inserting data
    def insert_student(self,  name, dob, education, address):
        print("\n Step 4: Inserting data...")
        try:
            query="""INSERT INTO students (name, dob , education , address)
             VALUES (%s, %s, %s, %s);
             """
            self.cursor.execute(query, (name, dob, education, address))
            self.conn.commit()

            print("Data inserted successfully")
        except Exception as e:
            print("Data insertion failed:", e)

    # Step 5 : Update data
    def update_student(self, roll_no, name, dob, education, address):
        print("\n Step 5: Updating data...")

        try:
            query="""UPDATE students
            SET name = %s, dob = %s, education = %s, address = %s
            WHERE roll_no = %s;
            """
            self.cursor.execute(query, (name, dob, education, address, roll_no))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print("Roll no  does not exist")
            else:
                print("Updated successfully")
        except Exception as e:
            print("Error while updating data",e)

    # Step 6: delete data
    def delete_student(self, roll_no):
        print("\n Step 6: Deleting data...")
        try:
            query="""DELETE FROM students WHERE roll_no = %s;
            """
            self.cursor.execute(query, (roll_no,))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print("Roll no does not exist")
            else:
                print("Deleted successfully")
        except Exception as e:
            print("Error while deleting data",e)



    # Step last: Close Database connection

    def close(self):
        print("\n Closing Database...")

        try:
            # Close cursor and connection
            self.cursor.close()
            self.conn.close()
            print("Database closed")

        except Exception as e:
            print("Error while closing database",e)


## ------------MAIN PROGRAM ---------------#
db = Database()

#Call methods step by step
db.create_database_if_not_exists()
db.connect()
db.create_tables()
db.close()
