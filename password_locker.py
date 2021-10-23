import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user


def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def sav_credential(credential):
        """
        function to save a newly created credential
        """
        credential.save_credentials(credential)
def display_credentials(user_name):
        """
        function to display saved credential for a user
        """
        return Credential.display_credentials(user_name)

def copy_credentials(site_name):
    '''
    copy credentials details to clipboard
    '''
    return Credential(site_name)

def main():
	print(' ')
	print('Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n CA-Create an Account \n LO-Log In \n EX-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'EX':
			break

		elif short_code == 'LO':
		 print("-"*60)
		print(' ')
		print('To login, enter your account details:')
		user_name = input('Enter your first name - ').strip()
		password = str(input('Enter your password - '))
		user_exists = verify_user(user_name,password)
		if user_exists == user_name:
			print(" ")
			print(f'Welcome {user_name}.choose an option to continue.')
			while True:
				print("-"*60)
				print('Navcodes: \n CC-Create a Credential \n DC-Display Credentials \n CP-Copy Password \n EX-Exit')