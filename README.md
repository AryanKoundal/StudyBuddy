# StudyBuddy
[StudyBuddy](https://aryankoundal-studybuddy.herokuapp.com/) is a free messaging service.
Users have the ability to communicate with  text messaging, media and files in private chats or as part of communities called "rooms".

# Run App Locally

## Clone the repository
:arrow_right: Clone the repository using the command below :  
```
git clone https://github.com/AryanKoundal/StudyBuddy
```

:arrow_right:Move into the directory where we have the project files :
```
# Install virtualenv first
$ pip install virtualenv

# Then create virtual environment
$ virtualenv env(environmentname)

# Activate the virtual environment
$ source env/bin/activate # for linux
$ env/Scripts/activate.bat //In Windows CMD
$ env/Scripts/Activate.ps1 //In Powershel

# Deactivate the virtual environment
$ deactivate

```
:arrow_right: Install the requirements
```
$ pip install -r requirements.txt

# Create the data models
$ python3 manage.py makemigrations

# Updates the data
$ python3 manage.py migrate

# Edit the file ~//settings.py and change the allowed hosts to:
# ALLOWED_HOSTS = [ '*' ] # Set to open for all access
```

## Running the App
```
$ Running the App
```
> The development server will be started at http://127.0.0.1:8000/


# Technologies Used
<img align="left" alt="python" width="30px" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img align="left" alt="HTML" width="30px" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img align="left" alt="DJANGO" width="30px" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
<img align="left" alt="JAVASCRIPT" width="30px" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img align="left" alt="CSS" width="30px" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />

<br>

# Features
1. User Login/Register
1. Create/Delete a room with multiple topic tags
1. Send/Delete Messages in a room
1. See all the participants of that room
1. Search rooms using any topic/tag
1. See all the old topics in the number of rooms of them
1. See recent activity on the website
1. View other user's profile
1. Edit your own profile with an about section

# App Preview




