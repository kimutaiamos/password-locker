
#! /usr/bin/env python3
import pyperclip
from user_credentials import User, credential, save_credentials

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
	checking_user = credential.check_user(first_name,password)
	return checking_user


def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=credential(user_name,site_name,account_name,password)
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
        return credential.display_credentials(user_name)

def copy_credentials(site_name):
    '''
    copy credentials details to clipboard
    '''
    return credential(site_name)

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
				short_code = input('Enter a choice: ').lower().strip()
				print("-"*60)
				if short_code == 'EX':
					print(" ")
					print(f'Goodbye {user_name}')
					break
				elif short_code == 'CC':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('choose an option for entering a password: \n EP-enter existing password \n GP-generate a password \n EX-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'EP':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'GP':
								password = generate_password()
								break
							elif psw_choice == 'EX':
								break
							else:
								print('oops! wrong details entered.Try again!.')

						save_credentials(create_credential(user_name,site_name,account_name,password))
						print('')
						print(f'credential created: site Name:{site_name} - Account Name:{account_name} -password: {password}')
						print(' ')
				elif short_code == 'DC':
					print(' ')
					if display_credentials(user_name):
						print('Here is a list of credentials')
						print(' ')
						for credential in display_credentials(user_name):
							print(f'site Name:{credential.site_name} -Account Name: {credential.account_name} - pasword:{credential.password}')
							print(' ')
						else:
							print(' ')
							print("looks like you have no credentials yet")
							print(' ')
				elif short_code == 'CO':
					print(' ')
					chosen_date = input('Enter the site name for the credential password to CO: ')
					copy_credentials()
					print(' ')
				else:
					print('Wrong option entered.Try again!.')
			else:
				print(' ')
				print('Wrong options entered.Try again or create new Account.')

		else:
			print("-"*60)
			print(' ')
			print('Wrong option entered.Try again!. ')

if __name__ == '__main__':
	main()
				         
				
			