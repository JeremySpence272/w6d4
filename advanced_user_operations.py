import sqlite3

class AdvancedUserOperations:

    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()


    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
        self.cursor.execute('''
            INSERT INTO user_profiles (age, gender, address)
            VALUES (?, ?, ?)
        ''', (age, gender, address))
        
        profile_id = self.cursor.lastrowid

        self.cursor.execute('''
            INSERT INTO user_accounts (name, email, password, profile)
            VALUES (?, ?, ?, ?)
        ''', (name, email, password, profile_id))

        self.conn.commit()
        return("created person")




    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):
        query = '''
            SELECT user_accounts.name, user_accounts.email, user_profiles.age, user_profiles.gender, user_profiles.address
            FROM user_accounts
            JOIN user_profiles ON user_accounts.profile = user_profiles.id
            WHERE 1=1

            '''
        params = []
        if min_age is not None:
            query += ' AND user_profiles.age >= ?'
            params.append(min_age)
        if max_age is not None:
            query += ' AND user_profiles.age <= ?'
            params.append(max_age)
        if gender:
            query += ' AND user_profiles.gender = ?'
            params.append(gender)

        self.cursor.execute(query, params)
        users = self.cursor.fetchall()

        return users


        



    def update_user_profile(self, email, age=None, gender=None, address=None):
        fields = []
        params = []
        if age is not None:
            fields.append("age = ?")
            params.append(age)
        if gender is not None:
            fields.append("gender = ?")
            params.append(gender)
        if address is not None:
            fields.append("address = ?")
            params.append(address)

        if fields:
            update_stmt = f"UPDATE user_profiles SET {', '.join(fields)} WHERE id = (SELECT profile FROM user_accounts WHERE email = ?)"
            params.append(email)
            self.cursor.execute(update_stmt, params)
            self.conn.commit()

        return("updated person")



        



    def delete_users_by_criteria(self, gender=None):
        if gender is None:
            return 
    
        delete_stmt = "DELETE FROM user_profiles WHERE gender = ?"
        self.cursor.execute(delete_stmt, (gender,))

        return ("deleted person")
        



    def __del__(self):
        self.conn.close()
