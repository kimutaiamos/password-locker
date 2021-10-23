from _typeshed import Self
import pyperclip
import random
import string

#variables
# Global Variables
global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	
	# global users_list
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
def save_user(self):
    """
    function to save a newly created user
    """
    User.users_list.append(self)
class credential:
    """
    class to create credentials ,generate passwords and save their information
    """
#class variables
credential_list = []
user_credentials_list = []
@classmethod
def check_user(cls,first_name,password):
    """
    method that checks if the name and password entered matches with the original enries
    """
    current_user = ''
    for user in User.users_list:
        if(user.first_name == first_name and user.password == password):
            current_user = user.first_name
            return current_user
            
