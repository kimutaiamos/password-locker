# from _typeshed import Self
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

def _init_(self,user_name,site_name,account_name,password):
    """
    method define properties for each user object will hold
    """
    self.username = user_name
    self.site_name = site_name
    self.account_name = account_name
    self.password = password

def save_credentials(self):
    """
    function to save a new user instance
    """
    credential.credentials_list.append(self)

def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    """
    function to generate password
    """
    gen_pass=''.join(random.choice(char) for _ in range(size))
    return gen_pass

def display_credentials(cls,user_name):
    """
    class method to display the list of credentials saved
    """
    user_credentials_list = []
    for credential in cls.credentials_list:
        if credential.user_name == user_name:
            user_credentials_list.append(credential)
            return user_credentials_list


def copy_credential(cls,site_name):
		"""
		Class method that copies a credential's info after the credential's site name is entered
		"""
		find_credential = credential.find_by_site_name(site_name)
		return pyperclip.copy(find_credential.password)