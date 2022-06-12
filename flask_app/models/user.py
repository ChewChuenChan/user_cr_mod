# import the functions that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


#model the class after the users table from database
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#use class method to query database
#call the connectToMySQL function with the targeting schema
#create an empty list to append the instances
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_schema.users;"
        result = connectToMySQL('users_schema').query_db(query)
        all_users = []
        for one_user in result:
            all_users.append(cls(one_user))
        return all_users


#class method to save our friend to the database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW());"
        return connectToMySQL('users_schema').query_db(query,data)
