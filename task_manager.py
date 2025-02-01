# Copyright (C) ${2025} ${Deepak Soma Reddy} (${sdeepak001@gmail.com})

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import signal
import datetime, time
from tabulate import tabulate
from getpass import getpass
import hashlib


def signal_handler(signal, frame):
    print("\n\nExiting the program.")
    sys.exit(0)

class UserLogin:
    def __init__(self):
        self.users = []
        pass

    def __hash_password(self, password) -> str:
        password = password.encode('utf-8')  # Convert the password to bytes
        hash_object = hashlib.sha256(password)   # Choose a hashing algorithm (e.g., SHA-256)
        return hash_object.hexdigest()        # Get the hexadecimal digest of the hashed password

    def load_users(self):
        if os.path.exists("users.csv"):
            with open("users.csv", "r") as file:
                for line in file:
                    user = line.strip().split(",")
                    self.users.append({"username": user[0], "password": user[1]})

    def login(self) -> dict:
        print("\nEnter your login credentials")
        username = input("Username: ")
        password = getpass()

        user = list(filter(lambda user: user["username"] == username, self.users))
        if len(user) > 0:
            if user[0]["password"] == self.__hash_password(password):
                print("Login successful. Please wait for task manager menu to load.")
                time.sleep(2)
                return user[0]
            else:  
                print("Invalid password. Please enter a valid password.")
                return {}
        print("User does not exist. Please signup.")
        return {}

    def signup(self):
        print("\nEnter Username and Password to signup")
        username = input("Username: ")
        password = getpass()

        user = list(filter(lambda user: user["username"] == username, self.users))
        if len(user) > 0:
            print("User already exists. Please try with new username.")
            return
        
        hash_password = self.__hash_password(password)
        self.users.append({"username": username, "password": hash_password})

        with open("users.csv", "a") as file:
            file.write(f"{username},{hash_password}\n")

        print("User created successfully.")
        pass

    def __login_menu(self):
        while True:
            print("\nUser Login")
            print("1. Login")
            print("2. Signup")
            choice = input("Please enter your choice between 1-2: ")

            if choice in ["1", "2"]:
                return int(choice)
            else:
                input("Invalid choice. Please enter a valid choice. press any key to continue to retry...")
                os.system("clear")

    def user_login(self):
        user = {}
        while True:
            choice = self.__login_menu()
            if choice == 1:
                user = self.login()
                if user == {}:
                    continue
                break
            elif choice == 2:
                if not self.signup():
                    continue
                break
            else:
                print("Invalid choice. Please enter a valid choice.")
                input()
                os.system("clear")
        return user

class Taskmanager:

    def __init__(self):
        self.__task = []
        pass

    # Check if the date is in correct format
    def __validate_date(self, date) -> bool:
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter date in yyyy-mm-dd format.")
            return False
        return True
    
    def load_task(self, user) -> None:
        self.__task = []
        user = user.replace(" ", "_")
        task_file = f"{user}_task.csv"
        try:
            if os.path.exists(task_file):
                with open(task_file, "r") as file:
                    for line in file:
                        task = line.strip().split(",")
                        self.__task.append({"Taskid": task[0], "Task": task[1], "Date": task[2], "Status": task[3]})
            else:
                with open(task_file, "w") as file:
                    pass
        except Exception as e:
            print(f"Error loading the task file: {str(e)}")
            return

    def update_file(self, user) -> None:
        user = user.replace(" ", "_")
        with open("{}_task.csv".format(user), "w") as file:
            for task in self.__task:
                file.write(f"{task['Taskid']}, {task['Task']},{task['Date']},{task['Status']}\n")

    def add_task(self, loginuser) -> None:
        task = {}
        task["Task"] = input("Enter the task: ")
        if task["Task"] == "":
            print("Task cannot be empty. Please enter a valid atask.")
            return
        
        task["Date"] = input("Enter the date (YYYY-MM-DD): ")
        if not self.__validate_date(task["Date"]):
            print("Invalid date. Please enter a valid date.")
            return
        
        task["Status"] = "Pending"
        task["Taskid"] = str(len(self.__task) + 1)
        self.__task.append(task)

        self.update_file(loginuser["username"])
        print("Task added and saved successfully.\n")

    def view_task(self) -> None:
        print("\nView Task:")
        if not self.__task and len(self.__task) == 0:
            print("No task to view.")
            return
        print(tabulate(self.__task, headers="keys", tablefmt="grid"))

    def update_task(self, loginuser) -> None:
        print("\nUpdate Task:")
        if not self.__task and len(self.__task) == 0:
            print("No task to update.")
            return
        print(tabulate(self.__task, headers="keys", tablefmt="grid"))
        task = input("Enter the task id to update: ")
        task = list(filter(lambda t: t["Taskid"] == str(task), self.__task))
        if len(task) == 0:
            print("Task not found. Please enter a valid task.")
            return
        
        task = task[0]
        task["Status"] = input("Enter the status (Pending/Completed): ")
        if task["Status"] not in ["Pending", "Completed"]:
            print("Invalid status. Please enter a valid status.")
            return
        
        self.update_file(loginuser["username"])
        print("Task updated successfully.\n")

    def delete_task(self, loginuser) -> None:
        print("\nDelete Task:")
        if not self.__task and len(self.__task) == 0:
            print("No task to delete.")
            return
        print(tabulate(self.__task, headers="keys", tablefmt="grid"))
        task = input("Enter the task id to delete: ")
        task = list(filter(lambda t: t["Taskid"] == str(task), self.__task))
        if len(task) == 0:
            print("Task not found. Please enter a valid task.")
            return
        self.__task.remove(task[0])
        
        # Reassign Task IDs after deletion to keep them sequential
        for idx, task in enumerate(self.__task):
            task["Taskid"] = str(idx + 1)  # Reassign Task IDs starting from 1

        self.update_file(loginuser["username"])
        print("Task deleted successfully.\n")

    def task_choice(self, choice, loginuser) -> dict:
        if choice == 1:
            self.add_task(loginuser)
        elif choice == 2:
            self.view_task()
        elif choice == 3:
            self.update_task(loginuser)
        elif choice == 4:
            self.delete_task(loginuser)
        elif choice == 5:
            print("Logging out. Please wait for the login menu to load.")
            time.sleep(2)
            os.system("clear")
            user = UserLogin()
            user.load_users()
            return user.user_login()
        else:
            print("Invalid choice. Please enter a valid choice.")
            input()
        return loginuser
    
    def task_menu(self, loginuser) -> int:
        while True:
            print("\n\nWelcome to Task Manager [User: {}]".format(loginuser["username"]))
            print("1. Add Task")
            print("2. View Task")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Logout")
            choice = input("Please enter your choice between 1-5: ")

            if choice in ["1", "2", "3", "4", "5"]:
                return int(choice)
            else:
                input("Invalid choice. Please enter a valid choice. press any key to continue to retry...")
                os.system("clear")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    # Login
    user = UserLogin()
    user.load_users()
    loginuser = user.user_login()

    #os.system("clear")
    # Create an instance of Taskmanager class
    task = Taskmanager()
    while loginuser != {}:
        # Display the menu
        choice = task.task_menu(loginuser)
        # Load the task from the file
        task.load_task(loginuser["username"])

        # Manage the task
        loginuser = task.task_choice(choice, loginuser)
        input("Press any key to continue...")
        #os.system("clear")
