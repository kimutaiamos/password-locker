import pyperclip
from user_credentials import User, credential
def create_user(firstname, lastname, password)
"""
function to create a new user account
"""
new_user = User(firstname,lastname,password)
	return new_user
   
    def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)