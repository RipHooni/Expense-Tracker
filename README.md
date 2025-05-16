# Expense Tracker CLI
# [Project URL](https://roadmap.sh/projects/expense-tracker)

Command-line expense tracker built with Python:

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.

## Usage
- **Add an Expense**: Record a new expense with a description and amount.
  ```sh
    python Tracker.py add --description expenseDescription --amount 25
    ```
- **List Expenses**: Display a table of all recorded expenses.
  ```sh
    python Tracker.py list
    ```
- **Delete an Expense**: Remove an expense by its unique ID.
  ```sh
    python Tracker.py delete --id 1
    ```
- **Summary**: Display a summary of total expenses or a monthly breakdown.
  ```sh
    python Tracker.py summary
    ```
  OR
  
  ```sh
    python Tracker.py summary --month 3
    ```

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```

2. Navigate to project directory:
    ```sh
    cd <project-directory>
    ```

## Usage
1. Run the script with desired commands:
   
   ex)
    ```sh
    python Tracker.py add --description lunch --amount 50
    ```
