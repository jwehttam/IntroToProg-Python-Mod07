# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error handling
# Change Log: (Who, When, What)
#   MJohnson, 11/26/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json

#############
# Constants #
#############
MENU: str = '''
------ Course Registration Program ------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''
FILE_NAME: str = 'Enrollments.json'

#############
# Variables #
#############
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


################
# Person Class #
################
class Person:
    """
    A class representing a person, with first and last name attributes.
    Validates that names contain only letters.

    ChangeLog:
    - MJohnson, 11.26.2023, Created Class
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        """
        Initializes a new instance of the Person class.

        :param first_name: string representing the first name of the person.
        :param last_name: string representing the last name of the person.
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """ Property getter for first_name. """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """ Property setter for first_name, validates input. """
        if value.isalpha() or value == '':
            self.__first_name = value
        else:
            raise ValueError('The first name should only contain letters')

    @property
    def last_name(self):
        """ Property getter for last_name. """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """ Property setter for last_name, validates input. """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError('The last name should only contain letters')

    def __str__(self):
        """ String representation of a Person instance in comma-separated format. """
        return f'{self.first_name},{self.last_name}'


#################
# Student Class #
#################
class Student(Person):
    """
    A class representing a student, inheriting from Person.
    Adds a course_name attribute specific to students.

    ChangeLog:
    - MJohnson, 11.26.2023, Created Class
    """

    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        """
        Initializes a new instance of the Student class.

        :param first_name: string representing the first name of the student.
        :param last_name: string representing the last name of the student.
        :param course_name: string representing the course name the student is enrolled in.
        """
        super().__init__(first_name, last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        """ Property getter for course_name. """
        return self.__course_name.title()

    @course_name.setter
    def course_name(self, value: str):
        """ Property setter for course_name, validates input to allow letters, numbers, and spaces. """
        if all(char.isalnum() or char.isspace() for char in value):
            self.__course_name = value
        else:
            raise ValueError('The course name should only contain letters, numbers, and spaces')

    def __str__(self):
        """ String representation of a Student instance in comma-separated format. """
        return f'{self.first_name},{self.last_name},{self.course_name}'

    def to_dict(self):
        """ Converts a Student instance to a dictionary. Useful for JSON storage. """
        return {'FirstName': self.first_name, 'LastName': self.last_name, 'CourseName': self.course_name}


#######################
# FileProcessor Class #
#######################
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog:
    - MJohnson, 11.26.2023, Created Class
    """

    @staticmethod
    def read_data_from_file(student_data: list):
        """
        Reads data from the 'Enrollments.json' file and loads it into a list of dictionary rows.

        ChangeLog:
        - MJohnson, 11.26.2023, Created function

        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """
        file = None  # Initialize variable to avoid UnboundLocalError in case of exception
        try:
            file = open(FILE_NAME, 'r')
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message='Error: There was a problem with reading the file.', error=e)

        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(student_data: list):
        """
        Writes data to the 'Enrollments.json' file from a list of dictionary rows.

        ChangeLog:
        - MJohnson, 11.26.2023, Created function

        :param student_data: list of dictionary rows to be written to the file

        :return: None
        """
        file = None  # Initialize variable to avoid UnboundLocalError in case of exception
        try:
            file = open(FILE_NAME, 'w')
            json.dump(student_data, file, indent=4)
            file.close()
        except Exception as e:
            message = 'Error: There was a problem with writing to the file.\n'
            message += 'Please check that the file is not open by another program.'
            IO.output_error_messages(message=message, error=e)
        finally:
            if not file.closed:
                file.close()


############
# IO Class #
############
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog:
    - MJohnson, 11.26.2023, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

        ChangeLog:
        - MJohnson, 11.26.2023, Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end='\n\n')
        if error is not None:
            print('-- Technical Error Message -- ')
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        ChangeLog:
        - MJohnson, 11.26.2023, Created function

        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user and handles keyboard interrupts.

        ChangeLog:
        - MJohnson, 11.26.2023, Created function
        - MJohnson, 11.27.2023, Added KeyboardInterrupt handling

        :return: string with the users choice or 'INTERRUPTED' if a keyboard interrupt is detected
        """
        choice = '0'
        try:
            choice = input('Enter your menu choice number: ')
            if choice not in ('1', '2', '3', '4'):
                raise Exception('Please, choose only 1, 2, 3, or 4')
        except KeyboardInterrupt:
            # If a keyboard interrupt is detected, return 'INTERRUPTED'
            return 'INTERRUPTED'
        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """
        This function displays the student and course names to the user

        ChangeLog:
        - MJohnson, 11.26.2023, Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print('-' * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print('-' * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the student's first name and last name, with a course name from the user
        and asks if the user wants to register another student.

        ChangeLog:
        - MJohnson, 11.26.2023, Created function
        - MJohnson, 11.27.2023, Added feature to register another student

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        while True:  # Loop to allow for multiple student registrations
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError('The first name should only contain letters.')
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError('The last name should only contain letters.')

                course_name = input('Please enter the name of the course: ')
                if not all(char.isalnum() or char.isspace() for char in course_name):
                    raise ValueError('The course name should only contain letters, numbers, and spaces')

                # Create a new Student object and append it to the student_data list
                student = Student(first_name=student_first_name, last_name=student_last_name, course_name=course_name)
                student_data.append(student.to_dict())

                print(f'You have registered {student.first_name} {student.last_name} for {course_name}.')

                # Ask if the user wants to register another student
                another = input('Would you like to Register Another Student? (y/n): ').lower().strip()
                if another != 'y':
                    break  # Exit the loop if the user does not enter 'y'

            except ValueError as e:
                print(f'Error: {e}')  # Print the error message and continue the loop
                continue  # Skip the rest of the loop and start over

        return student_data


################################################################################
# -- When the program starts, read the file data into a list of dictionaries --#
################################################################################
students = FileProcessor.read_data_from_file(student_data=students)

###################
# -- Main Loop -- #
###################
while True:
    try:
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == 'INTERRUPTED':
            print('\nProgram terminated by user. Goodbye!')
            break
        elif menu_choice == '1':
            IO.input_student_data(students)
        elif menu_choice == '2':
            print('The following students are registered:')
            IO.output_student_and_course_names(students)
        elif menu_choice == '3':
            FileProcessor.write_data_to_file(students)
            print('The following data has been saved to Enrollments.json:')
            IO.output_student_and_course_names(students)
        elif menu_choice == '4':
            print('Goodbye!')
            break
        else:
            print('Please only choose option 1, 2, 3 or 4')

    except Exception as e:
        IO.output_error_messages('An unexpected error occurred', e)
