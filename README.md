# XMLParser
A sample web application featuring data uploading and data parsing of XML file containing student details. The application also features Account Registration, Login, Data Analytics like Viewing, Sorting, Filtering, PDF Download, Excel Download and Printing 

### Project Setup
#### Step 0: Prerequisites:
##### Install Python3.7, pip and virtualenv
##### Install MySQL Ver 14.14 Distrib 5.7.31
#### Step 1: Clone the repo:
`git clone https://github.com/ShahidYousuf/XMLParser.git`
#### Step 2: Create a Python Virtualenv:
###### If you are using some ide like Pycharm, you may not manually need to install pip and virtualenv or create virtualenv via terminal.
`virtualenv -p python3.7 ENV_PY37_XMLParser`
#### Step 3: Change to Project directory of Step 1
`cd XMLParser/xmlparser`
#### Step 4: Activate the Virtual Environment of Step 2:
`source /path/to/your/virtual_env/bin/activate`
#### Step 5: Install the project requirements:
`pip install -r requirements.txt`
#### Step 6: Create a MySQL database instance and database settings in the project settings.py file:
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<INSERT_YOUR_MYSQL_DB_NAME_HERE>',
        'USER': '<INSERT_MYSQL_USER_HERE>',
        'PASSWORD': '<INSERT_MYSQL_USERS_PASSWORD_HERE>'
    }
}`
#### Step 7: Run project migrations which create database tables/schemas:
`python manage.py migrate`
#### Step 8: Run the project:
`python manage.py runserver`
#### Step 9: See if you can view the website, default on http://localhost:8000
