# Task Manager with User Authentication

## Overview

This project implements a **Task Manager** system with **user authentication**. It allows users to create, view, update, and delete tasks, while ensuring that tasks are only accessible by the authenticated user. Each user’s tasks are stored separately in a file, and the application supports both user login and signup functionalities.

The application uses **password hashing** for security and **file handling** to persist user data and tasks.

## Features

- **User Authentication:**
  - Signup: Users can create a new account with a unique username and password.
  - Login: Users can log in using their credentials, and the system validates them by comparing the entered password (hashed) with the stored password.
  
- **Task Management:**
  - Add Task: Users can add tasks with a description, due date, and an initial status of "Pending."
  - View Tasks: Users can view all tasks with their description, due date, and current status.
  - Update Task: Users can update the status of a task (e.g., mark as "Completed").
  - Delete Task: Users can delete tasks from their list.

- **Persistent Storage:**
  - User credentials are stored in a file (`users.txt`).
  - Tasks for each user are stored in separate files based on the username (e.g., `username_task.txt`).

- **Clear Console Interface:**
  - Interactive menu system for managing tasks.
  - The program handles user inputs and provides clear prompts.

## Requirements

- Python 3.x
- `tabulate` library (for displaying tasks in a tabular format)

You can install the required library using:
```bash
pip install tabulate
```

## How to Use

1. Clone or Download the Code
Clone the repository or download the Python file (task_manager.py) to your local machine.

```bash
git clone https://github.com/sdeepak001/Task_Manager.git
```


2. Running the Program
To start the program, run the following command in your terminal:

```
python task_manager.py
```
This will initiate the login menu.

3. User Authentication
    - Login: Enter your existing username and password. If the credentials are valid, you will be logged in and redirected to the task manager menu.
    - Signup: If you don't have an account, you can sign up by entering a unique username and a password.
4. Task Management
Once logged in, you will be able to manage your tasks:

    - Add Task: Adds a new task with a description, due date, and status.
    - View Task: Displays all tasks associated with your account.
    - Update Task: Allows you to update the status of a task (Pending/Completed).
    - Delete Task: Allows you to delete a task from your task list.
    - Logout: Logs out the user and returns to the login menu.
5. Data Storage
    - User credentials are stored in users.txt.
    - Each user's tasks are stored in a file named after the username with a _task.txt suffix (e.g., john_doe_task.txt).

## Code Structure
### Classes
1. UserLogin: Handles user login, signup, and password hashing.
    - login(): Prompts the user to enter login credentials and verifies them.
    - signup(): Prompts the user to create a new account.
    - load_users(): Loads user credentials from users.txt.
    - __hash_password(): Hashes the user's password using SHA-256.
2. Taskmanager: Manages tasks for the logged-in user.
    - add_task(): Adds a new task.
    - view_task(): Displays all tasks.
    - update_task(): Updates the status of a task.
    - delete_task(): Deletes a task.
    - load_task(): Loads the tasks from the user's task file.
    - update_file(): Saves the tasks to the user's task file.

### Methods
    - signal_handler(): Handles the exit signal and ensures the program exits cleanly.
    - clear_console(): Clears the console based on the operating system (Windows or Unix).

## Example

```
Welcome to Task Manager [User: john_doe]
1. Add Task
2. View Task
3. Update Task
4. Delete Task
5. Logout
Please enter your choice between 1-5: 1

Enter the task: Finish homework
Enter the date (YYYY-MM-DD): 2025-01-31
Task added and saved successfully.

Press any key to continue...
```

## License
This project is licensed under the Apache License, Version 2.0 - see the LICENSE for details.

## Contact
If you have any questions or feedback, feel free to contact me at:
- Deepak Soma Reddy
- Email: sdeepak001@gmail.com
