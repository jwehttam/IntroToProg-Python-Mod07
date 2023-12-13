[//]: # (Title: Assignment08)

[//]: # (Description: A collection of classes for managing the application)

[//]: # (ChangeLog: (Who, When, What)

[//]: # (MJohnson,12.04.2023,Created Script)


# Employee Rating Application
**Note:** This documentation was created with assistance from ChatGPT (heavily edited), Draw.IO for creating diagrams,
and Jupyter Notebook for the Ratings Graph.

## Diagrams and Jupyter Notebook Graph Examples (Mod09)

---

### Use Case Diagram
![The use case diagram of the application](./images/Mod08_Use_Case_UML.jpg)

### Class Diagram
![The class diagram of the application](./images/Mod08_Class_UML.jpg)

### SOC Diagram
![The Separation of Concerns Diagram of the application](./images/Mod08_SOC_UML.jpg)

### Jupyter Notebook Overall Ratings Bar Graph
![The Jupyter Notebook Ratings_Example](./images/Mod09_JN_Ratings.jpg)

### Jupyter Notebook Ratings Distribution by Year Bar Graph
![The Jupyter Notebook Ratings_Distribution_by_Year_Example](./images/Mod09_JN_RDBY.jpg)

## Project Description

---

Welcome to the Employee Rating Application – This application offers a straightforward menu-driven interface, allowing
users to view, enter, and save employee rating data. Whether you're a Team Lead,
HR professional, or just someone keen on keeping track of performance metrics, this application is designed to make
your life easier.

## Features
The Employee Rating Application provides a user-friendly menu with the following options:
- Show Current Employee Rating Data: View the existing set of employee ratings.
- Enter New Employee Rating Data: Input new ratings for employees.
- Save Data to a File: Securely save the current employee data to a file for future reference.
- Exit the Program: Safely close the application.

## Usage
Upon launching the Employee Rating Application, users are greeted with a simple and intuitive menu:

```
---- Employee Ratings ----------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
```

Users can navigate through the menu by entering the number corresponding to their choice.

## Example Workflow
- View Ratings: Users can view current employee ratings by selecting option 1.
- Enter Ratings: To add new ratings, select option 2 and follow the prompts to enter the necessary information.
- Save Data: After entering new data, users can choose to save it by selecting option 3.
- Exit: To exit the application, users can simply choose option 4.

## Key Features
- No Installation Needed: Run the application directly and get down to business.
- Menu-Driven Interface: Navigate through the application with a clear and intuitive menu.
- Employee Data Management: Enter and track employee ratings with minimal fuss.
- Persistent Data Storage: Save all the details into EmployeeRatings.json for longevity.
- Error Handling: Well structured error handling for all user inputs.

## Classes and Functions
- FileProcessor: Handles the reading and writing of employee data to and from EmployeeRatings.json.
- IO: Manages all user interactions, data input, and presentation.
- Person: The base class that defines the properties of an individual.
- Employee (Inherits from Person): Stores and manages employee-specific data like review dates and ratings.
- Utility Functions: A collection of static methods to support data processing and error messaging.

## Properties
- employee_first_name: The first name of the employee, initialized to an empty string.
- employee_last_name: The last name of the employee, initialized to an empty string.
- review_date: The date of the performance review, with a default historic date.
- review_rating: An integer representing the employee's performance rating, defaulting to the middle of the scale.

## Methods
- Data Extraction: Extracts comma-separated data from each data class to ease processing.
- Validation: Simple validation to ensure data integrity.

## Input / Output
- Add Data: Prompt for employee data entry with structured inputs for names, dates, and ratings.
- View Data: Present collected data neatly to the user.
- Data Storage: All data collected is stored in a two-dimensional list (a list of Employee objects).

## Processing
- Auto-Load: On startup, the application auto-loads data from EmployeeRatings.json into the list.
- Save Data: Option to save current session data back to EmployeeRatings.json.
- Graceful Exit: Exits the application cleanly.

## Error Handling
Structured error handling is implemented for:
- Reading data from file
- User input for first and last names
- Review date entry in YYYY-MM-DD format
- Review rating entry (1 to 5 scale)
- Writing data to file

# Getting Started with main.py

---

The **main.py** file serves as the entry point to the Employee Rating Application. It ties together various modules and orchestrates the flow of the application. Here's a quick overview:

## How it Works
- **Initialization:** Imports necessary modules and initializes constants and variables.
- **Data Loading:** Reads existing employee data from EmployeeRatings.json into the application.
  - **User Interaction:**
    - Displays a user menu with four options.
    - Handles user input to navigate through the menu options.

## Menu Options
- **Option 1:** Display the current employee ratings data.
- **Option 2:** Enter new employee ratings, view the updated data.
- **Option 3:** Save the current data back to EmployeeRatings.json.
- **Option 4:** Exit the application.

## Usage
To start the application, run the main.py script in your Python environment. The script will automatically load any pre-existing data and present you with the main menu.

```python
if __name__ == '__main__':
# Application starts here
```

# Data Classes - data_classes.py

---

The **data_classes.py** file defines the structure and behavior of the data entities in the Employee Rating Application. Here's what's happening inside:

## Person Class
- **What It Is:** A base class for representing a person with a first and last name.
  - **Properties:**
    - `first_name`: Stores the first name, ensuring it only contains alphabetic characters.
    - `last_name`: Stores the last name with the same character constraints.

## Employee Class (Inherits from Person)
- **What It Is:** Represents an employee with additional details for performance reviews.
  - **Properties:**
    - Inherits `first_name` and `last_name` from Person.
    - `review_date`: A date object representing when the review took place.
    - `review_rating`: An integer (1-5) representing the employee's performance rating.

## Validation
- The properties include validation to ensure that the data is correct (like names must be alphabetic, ratings must be between 1 and 5, etc.).

## Example Usage
```python
# Create an Employee object
jane_doe = Employee(first_name="Jane", last_name="Doe", review_date="2023-04-12", review_rating=4)

# Output the employee's details
print(jane_doe)
# Output: "Jane Doe, Review Date: 2023-04-12, Rating: 4"
```

# Processing Layer - processing_classes.py

---

The **processing_classes.py** module is where the application's data processing magic happens, specifically interfacing with JSON files to load and save employee data.

## FileProcessor Class
- **Purpose:** Provides static methods to read from and write to JSON files, specifically tailored for Employee objects.
  - **Main Functions:**
    - `read_employee_data_from_file`: Reads employee data from a JSON file and populates a list of Employee objects.
    - `write_employee_data_to_file`: Serializes a list of Employee objects into JSON and writes it to a file.

## Exception Handling
- The class includes exception handling for file operations, ensuring any file I/O errors are caught and logged.

## Example Usage
```python
# Reading employee data from file
employees = FileProcessor.read_employee_data_from_file('EmployeeRatings.json', [], Employee)

# Writing employee data to file
FileProcessor.write_employee_data_to_file('EmployeeRatings.json', employees)
```

# Presentation Layer - presentation_classes.py

---

The **presentation_classes.py** file contains the user interface components of the Employee Rating Application, responsible for presenting information to the user and handling user input.

## Constants
- **MENU:** A string constant that holds the main menu text for the application.

## IO Class
- **Purpose:** Manages all user-facing interactions, including displaying menus, capturing user input, and showing error messages.
  - **Features:**
    - `output_error_messages`: Shows error messages to the user.
    - `output_menu`: Displays the application's main menu.
    - `input_menu_choice`: Captures and validates the user's menu selection.
    - `output_employee_data`: Prints out all employee ratings.
    - `input_employee_data`: Collects new employee data from the user.

## User Interface Flow
- The class ensures a smooth user experience by guiding the user through the data input process, validating input, and providing feedback.

## Example Workflow
```python
# Displaying the menu
IO.output_menu(MENU)

# Capturing user menu choice
choice = IO.input_menu_choice()

# Displaying employee data
IO.output_employee_data(employees)

# Adding a new employee
IO.input_employee_data(employees, Employee)
```

# Testing

---

The application comes with a suite of unit tests to ensure that everything is functioning as expected. Running these tests is a great way to make sure that all components are in shape before you start tracking those employee ratings.

To run the tests, navigate to the application directory in your terminal and execute:

```bash
python -m unittest discover
```

This command will automatically find and run all the tests in the tests directory. Each test case is well documented, so you can understand what's being tested and why.
