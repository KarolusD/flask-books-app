## Design

- [x] Create basic mockup for our to-do app

### How it works

- [x] A little bit of a theory behind how web works

### Front-end

- [x] Create client folder
- [x] Create html document
- [x] Create basic html structure
- [x] Create basic css styles (mockup data)
- [ ] Setup eslint - js linter
- [ ] App frontend functionalities:
  - [x] Make a DELETE request to delete book
  - [x] Make a PUT request to edit a book
  - [ ] apply theme switcher (_optional_)
  - [ ] optimise code (_optional_)

### Back-end

- [x] Setup virtual enviornment
- [x] Instal flake8 - linter
- [x] Install autopep8 - formatter
- [x] Install flask
- [x] Create main.py
- [x] Create basic flask app
- [x] Create templates folder
- [x] Create index.html template
- [x] Create static folder
- [x] Create CSS and JS files in static folder
- [x] Create url_for to point on static folder
- [x] Create layout.html template
- [x] Use layout.html in index.html
- [x] Create flash message in the layout template
- [x] Create list with genres and render it using template engine (_optional_)
- [x] Create list with books and render it using template engine (_optional_)
- [x] Create registration route
- [x] Create login route
- [x] Instal flask-wtf
- [x] Install email-validator
- [x] Create registration form class
- [x] Create login form class
- [x] Create form helpers template
- [x] Create registration template
- [x] Create login template
- [x] Add form.csrf_token
- [x] Setup secret key in app config
- [x] Setup .env file with app config variables (like email password etc.)
- [x] Insert error messages into registration template
- [x] Insert error messages into login template
- [x] Create add_book form class
- [x] Create add_book template
- [x] Create add_book route
- [x] Create update_book form class
- [x] Create update_book template
- [x] Create update_book route
- [x] Create 403,404,500 template
- [x] Create 403,404,500 error handler

### Database

- [x] Instal ORM (Flask-SQLAlchemy)
- [x] Connect to database
- [x] Create User class (model)
- [x] Create Book class (model)
- [x] Create user in db from registration form
- [x] Create book in db from add_book form
- [x] Delete a book in db
- [x] Update a book in db
- [x] Update user data in db
- [x] Instal Pillow to manage images
- [x] Save user images in db

### Clean Up

- [x] Fix folder structure
- [x] Create run file
- [x] Introduce Blueprint for better code splitting
- [x] Create config file

### Authentication

- [x] Install flask-bcrypt
- [x] Hash users password
- [x] Add custom validation to registration form
- [x] Install flask-login
- [x] Create login_manager
- [x] Create login_manager.user_loader route
- [x] Inherit UserMixin in User model with methods like (isAuthenticated, isActive, isAnonymous)
- [x] Setup login_manager.login_view
- [x] Setup login_manager.login_message_category (CSS class)
- [x] Redirect user from login to home if it's not logout
- [x] Create account route and template
- [x] Redirect to login page if someone trying to access account without credentials
- [x] Redirect to login page if someone trying to access books view without credentials
- [x] Redirect to next page if user finally log in
- [x] Secure all pages that needs login user with @login_required decorator

### Further app logic

- [x] Update account template
- [x] Display profile picture
- [x] Make a form class for updating profile info
- [x] Make edit_account route and template
- [x] Insert form into edit_account template
- [x] Change update form validation
- [x] Test it!
- [x] Import FileField, FileAllowed from flask-wtf.file (_optional_)
- [x] Implement updating photo image (_optional_)
- [x] Install Pillow and resize images (_optional_)

### Deployment

- [x] Init git and connect with github repo (_optional_)
- [x] Setup requirements.txt file
- [x] Create linux server on linode
- [x] Configure ssh keys etc.
- [x] Copy project to server
- [x] Re-create virtual env
- [x] Install gunicorn
- [x] Install nginx
- [x] Configure guincorn and nginx
- [x] test running on server
- [x] Install and configure supervisor
