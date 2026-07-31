# Class Student with Static Method to calculate average marks

class Student:  
    # Constructor to initialize student details
    def __init__(self, name, mark1, mark2, mark3):  # Initialize student with name and 3 marks
        self.name = name  # Store student name
        self.mark1 = mark1  # Store first mark
        self.mark2 = mark2  # Store second mark
        self.mark3 = mark3  # Store third mark
    
    # Static method to calculate average of 3 marks
    @staticmethod  # Decorator to define static method
    def calculate_average(mark1, mark2, mark3):  # Static method takes 3 marks as parameters
        """Static method that calculates average of 3 marks"""  
        average = (mark1 + mark2 + mark3) / 3  
        return average  
    
    # Instance method to display student information
    def display_result(self):  # Instance method to display student details
        """Display student name and average marks"""  
        avg = Student.calculate_average(self.mark1, self.mark2, self.mark3)  # Call static method to calculate average
        print(f"Student Name: {self.name}")  # Print student name
        print(f"Marks: {self.mark1}, {self.mark2}, {self.mark3}")  # Print all three marks
        print(f"Average: {avg:.2f}\n")  # Print average with 2 decimal places


# Create student objects
student1 = Student("Alice", 85, 90, 78)  # Create first student object for Alice
student2 = Student("Bob", 92, 88, 95)  # Create second student object for Bob
student3 = Student("Charlie", 75, 80, 82)  # Create third student object for Charlie

# Display results for each student
student1.display_result()  # Display Alice's result
student2.display_result()  # Display Bob's result
student3.display_result()  # Display Charlie's result

# Call static method directly without creating object
print("Direct static method call:")  # Print header for direct static method call
avg_marks = Student.calculate_average(70, 75, 80)  # Call static method without object instance
print(f"Average of 70, 75, 80: {avg_marks:.2f}")  # Print the calculated average