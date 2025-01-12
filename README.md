# Budget Tracker

#### Video Demo: [https://youtu.be/3EJgveJBj2Q]

---

## Description:
The **Budget Tracker** is a Python program designed to help users manage their daily expenses effectively. With an intuitive interface and simple functionality, this program empowers users to:

- **Add an expense**: Enter the name of the item and its associated cost to track spending.
- **View recorded expenses**: Display a list of all recorded expenses in a structured format.
- **Calculate total expenses**: Compute the total amount spent based on all recorded entries.

This program is a practical tool for users looking to improve their financial awareness and budgeting skills. It also serves as an excellent demonstration of basic Python programming principles, including control flow, data structures, and exception handling.

---

## Features:
1. **Add an Expense**:
   - Users can input the name of an item and its corresponding cost.
   - Expenses are stored as dictionaries within a list, ensuring easy manipulation and retrieval.
   - Input validation prevents invalid entries, enhancing user experience.

2. **View All Expenses**:
   - Displays all recorded expenses in a neat, enumerated list.
   - If no expenses are recorded, the program informs the user.

3. **Calculate Total Expenses**:
   - Sums up the costs of all recorded expenses and displays the total with proper formatting.

4. **User-Friendly Interface**:
   - Provides a menu-based interaction for ease of use.
   - Handles invalid inputs gracefully with error messages and prompts for retry.

---

## Files:
1. **`project.py`**:
   - The main program file containing the core logic of the Budget Tracker.
     - **`main()`**: Runs the main interface, allowing users to choose from the menu options.
     - **`add_expense(expenses)`**: Handles adding a new expense to the list.
     - **`view_expenses(expenses)`**: Displays all recorded expenses in a structured format.
     - **`calculate_total(expenses)`**: Computes and returns the total cost of all expenses.

2. **`test_project.py`**:
   - A set of unit tests written using `pytest` to verify the correctness of the core functions:
     - Tests for `add_expense` ensure expenses are added correctly.
     - Tests for `view_expenses` validate the display functionality.
     - Tests for `calculate_total` confirm accurate total calculation.

3. **`requirements.txt`**:
   - Lists the required external libraries to run and test the project:
     - **`pytest`**: For unit testing the program.

---

## Design Choices:
1. **Data Storage**:
   - Expenses are stored as a list of dictionaries. Each dictionary represents an expense with two keys: `item` (name of the item) and `cost` (associated cost). This structure ensures flexibility and ease of manipulation.

2. **User Input Validation**:
   - The program handles invalid inputs (e.g., non-numeric costs) using exception handling (`try-except` blocks), making it robust against user errors.

3. **Menu System**:
   - A simple menu system guides users through the available functionalities, ensuring clarity and ease of navigation.

---

## Usage:
1. Run the program by executing `project.py` in a Python environment.
2. Follow the on-screen instructions to:
   - Add new expenses.
   - View recorded expenses.
   - Calculate the total of all expenses.
3. Exit the program at any time by selecting the "Exit" option from the menu.

---

## Future Improvements:
- Add the ability to categorize expenses (e.g., food, travel, utilities).
- Implement data persistence using a file or database to save expenses between sessions.
- Include graphical representations (e.g., pie charts) of expense distribution.

---

## Conclusion:
The Budget Tracker is a straightforward yet powerful tool for managing daily expenses. It demonstrates practical Python programming skills and provides a foundation for further development in financial management applications. With potential improvements and added features, it could become a more comprehensive budgeting solution.

---

## Requirements:
To run this project, ensure you have Python 3.x installed along with the `pytest` library. You can install the dependencies by running:

```bash
pip install -r requirements.txt# Project-Expense-Tracker
