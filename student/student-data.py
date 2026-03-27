## Student Data using the class
class Student:
    def __init__(self):
        # Dictionary to store student data
        # Key = roll number, Value = student details (another dictionary)
        self.students ={}

    def add_student(self):
        print("\n---Add Student---")
        roll = input("Ënter Roll No:")


    #checking if the roll nbr already exits

        if roll in self.students:
           print("Student Already Exist")
           return

        name = input("Student Name:")
        level = input("Student Level:")
        address = input("Student Address:")

        # Stores data in dictionary
        self.students[roll] ={
            "name":name,
            "level":level,
            "address":address,
        }

        print("Student Added Successfully")

    def show_students(self):
        print("\n---Student List---:")
## Loop through dict and display data
        for roll ,info in self.students.items():
            print(f"\nRoll No: {roll}")
            print(f"Name: {info['name']}")
            print(f"Level: {info['level']}")
            print(f"Address: {info['address']}")
    # 3. Update student data
    def update_student(self):
        print("\n--- Update Student ---")
        roll = input("Enter Roll No to update: ")

        # Check if student exists
        if roll not in self.students:
            print("Student not found!")
            return

        print("Enter new details:")
        name = input("Enter Name: ")
        level = input("Enter Level of Education: ")
        address = input("Enter Address: ")

        # Update data
        self.students[roll] = {
            "name": name,
            "level": level,
            "address": address
        }

        print("Student updated successfully!")

    # 4. Delete student data
    def delete_student(self):
        print("\n--- Delete Student ---")
        roll = input("Enter Roll No to delete: ")

        # Check if student exists
        if roll in self.students:
            del self.students[roll]  # remove from dictionary
            print("Student deleted successfully!")
        else:
            print("Student not found!")

## Main Program
def main():
    obj = Student()
    while True:
        print("\n====== Student Management Menu ======")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            obj.add_student()
        elif choice == '2':
            obj.show_students()
        elif choice == '3':
            obj.update_student()
        elif choice == '4':
            obj.delete_student()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
main()




