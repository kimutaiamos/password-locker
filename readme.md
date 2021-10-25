# Password Locker

## Built By sir amos kimutai on 20th october 2021

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
|dispay prompt for credentials|*enter :dc**|show credentials|
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |
## SetUp / Installation Requirements
### Prerequisites
* python3.9
* pip
* pyperclip


### Cloning
* In your terminal:
        
        $ git clone https://github.com/kimutaiamos/password-locker.git
        $ cd PasswordLocker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password.py
        $ ./password.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.9 run.py
        
## Technologies Used
* Python3.9
### License
[License](./license)
### contributing
our website is build with little knowledge in the three language,it is however,open to anyone who would wish to contribute to our project.
you can also refer here https://stackoverflow.com/questions/8503559/what-is-linting to learn more and run tests.
software methods and tools refer herehttp://www.methodsandtools.com/archive/archive.php?id=33.
###copyright @ 2021

