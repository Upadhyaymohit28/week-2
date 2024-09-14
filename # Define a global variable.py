# Creating a set
original_set = {1, 2, 3, 4, 5}

# Aliasing the original set
alias_set = original_set

# Modifying the alias set
alias_set.add(6)

# Printing both sets to show that they both reflect the change
print("Original Set:", original_set)
print("Alias Set:", alias_set)

# Creating a list
original_list = [1, 2, 3, 4, 5]

# Aliasing the original list
alias_list = original_list

# Modifying the alias list using append
alias_list.append(6)

# Printing both lists to show that they both reflect the change
print("Original List:", original_list)
print("Alias List:", alias_list)

# Creating a new list to show the difference
new_list = original_list.copy()

# Modifying the new list using append
new_list.append(7)

# Printing all lists to show the difference
print("Original List after copy:", original_list)
print("New List:", new_list)
# Demonstrating the difference between append and extend

# Using append to add a list to the original list
original_list_append = original_list.copy()
original_list_append.append([8, 9])

# Using extend to add elements to the original list
original_list_extend = original_list.copy()
original_list_extend.extend([8, 9])

# Printing the results
print("Original List after append:", original_list_append)
print("Original List after extend:", original_list_extend)

# Checking if a number is positive, negative, or zero using nested if
num = float(input("Enter a number: "))

if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
else:
        print("Negative number")
 # Dictionary to store student names and their grades
        students = {}

        def add_student(name):
            if name not in students:
                students[name] = []
                print(f"Student {name} added.")
            else:
                print(f"Student {name} already exists.")

        def add_grade(name, grade):
            if name in students:
                students[name].append(grade)
                print(f"Added grade {grade} for student {name}.")
            else:
                print(f"Student {name} does not exist. Please add the student first.")

        def print_grades(name):
            if name in students:
                print(f"Grades for {name}: {students[name]}")
            else:
                print(f"Student {name} does not exist.")

        # Example usage
        add_student("Alice")
        add_grade("Alice", 90)
        add_grade("Alice", 85)
        print_grades("Alice")

        add_student("Bob")
        add_grade("Bob", 78)
        print_grades("Bob")

global_var = "I am a global variable"

def my_function():
    # Local variable
    local_var = "I am a local variable"
    
    # Accessing global variable inside the function
    print(global_var)
    
    # Accessing local variable inside the function
    print(local_var)

# Calling the function
my_function()

# Accessing global variable outside the function
print(global_var)

# Define a global variable
ex = 10

def modify_ex():
    global ex
    ex = 20  # This modifies the global variable

def shadow_ex():
    ex = 30  # This creates a local variable that shadows the global variable

print(f"Initial global ex: {ex}")
modify_ex()
print(f"Global ex after modify_ex: {ex}")
shadow_ex()
 

    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
            print(f"Added grade {grade} for student {name}.")
        else:
            print(f"Student {name} does not exist. Please add the student first.")

    def print_grades(self, name):
        if name in self.students:
            print(f"Grades for {name}: {self.students[name]}")
        else:
            print(f"Student {name} does not exist.")

# Example usage
student_grades = StudentGrades()
student_grades.add_student("Alice")
student_grades.add_grade("Alice", 90)
student_grades.add_grade("Alice", 85)
student_grades.print_grades("Alice")

student_grades.add_student("Bob")
student_grades.add_grade("Bob", 78)
student_grades.print_grades("Bob")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        student = Student(name, grade)
        self.students[name] = student

    def get_grade(self, name):
        student = self.students.get(name)
        if student:
            return student.grade
        else:
            return "Student not found"

def main():
    gradebook = GradeBook()
    
    while True:
        action = input("Enter 'add' to add a student, 'get' to get a grade, or 'quit' to exit: ").strip().lower()
        
        if action == 'add':
            name = input("Enter student name: ").strip()
            grade = input("Enter student grade: ").strip()
            gradebook.add_student(name, grade)
            print(f"Added {name} with grade {grade}.")
        
        elif action == 'get':
            name = input("Enter student name to get the grade: ").strip()
            grade = gradebook.get_grade(name)
            print(f"{name}'s grade: {grade}")
        
        elif action == 'quit':
            break
        
        else:
            print("Invalid action. Please enter 'add', 'get', or 'quit'.")

if __name__ == "__main__":
    main()