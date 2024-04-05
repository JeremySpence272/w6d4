# w6d4

Assignment Tasks:

Enhanced Database Schema Design:

- Design an enhanced database schema for storing user information. Include additional fields for user profile information, such as age, gender, and address.

Database Setup and Migration:

- Set up a SQLite database using Python's SQLite3 module.

- Create a user table in the database based on the enhanced schema designed in Task 1.

- Implement a migration script to update the existing user table with the new schema changes.

CRUD Operations Implementation:

- Write Python functions to perform the following advanced CRUD operations on the user table:

  - `create_user_with_profile`: Create a new user with profile information in the database.

  - `retrieve_users_by_criteria`: Retrieve users based on specified criteria, such as age range or gender.

  - `update_user_profile`: Update user profile information in the database.

  - `delete_users_by_criteria`: Delete users based on specified criteria, such as address or gender.

Unit Testing:

- Write comprehensive unit tests to validate the functionality of each advanced CRUD operation.

- Ensure that the unit tests cover various scenarios, including edge cases and error handling.

Assignment Submission:

- Once you have completed the assignment, submit the following files:

  - `advanced_user_operations.py`: Python file containing the implementation of advanced CRUD operations.

  - `test_advanced_user_operations.py`: Python file containing the provided unit tests for advanced CRUD operations.

---

Solution Framework:

```python

# advanced_user_operations.py



import sqlite3



class AdvancedUserOperations:

    def __init__(self):

        self.conn = sqlite3.connect('user_database.db')

        self.cursor = self.conn.cursor()



    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):

        pass



    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):

        pass



    def update_user_profile(self, email, age=None, gender=None, address=None):

        pass



    def delete_users_by_criteria(self, gender=None):

        pass



    def __del__(self):

        self.conn.close()



```

Test Case

Test Case Script: Save the following script in a file with a `.py` extension, such as `test_case.py`. This script tests the functionality of the `AdvancedUserOperations` class by running various scenarios and printing the results.

```python

from advanced_user_operations import AdvancedUserOperations



# Initialize AdvancedUserOperations instance

advanced_user_ops = AdvancedUserOperations()



# Test creating a new user with profile information

print("Creating a new user...")

result_create = advanced_user_ops.create_user_with_profile('John Doe', 'john.doe@example.com', 'test123', age=30, gender='Male', address='123 Main St')

print("User creation result:", result_create)



# Test retrieving users based on specified criteria

print("\nRetrieving users...")

users = advanced_user_ops.retrieve_users_by_criteria(min_age=25, max_age=40, gender='Male')

print("Retrieved users:", users)



# Test updating user profile information

print("\nUpdating user profile...")

result_update = advanced_user_ops.update_user_profile('john.doe@example.com', age=35, address='456 Oak St')

print("User profile update result:", result_update)



# Test deleting users based on specified criteria

print("\nDeleting users...")

result_delete = advanced_user_ops.delete_users_by_criteria(gender='Female')

print("User deletion result:", result_delete)

```

Run Command: Open a terminal or command prompt, navigate to the directory where the test case script is located, and execute the following command:

```

python test_case.py
```
