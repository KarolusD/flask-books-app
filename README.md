## Flask Books Library App

Web application written in flask where you can store your favourite books.

#### 🛠 Instruction to run this project on your own machine

**1. Clone this repo on your machine** (macOS or UNIX - Bash)

```
git clone https://github.com/KarolusD/flask-books-app.git
```

**2. Re-create virtual enviornment** (macOS or UNIX - Bash)

```
python3 -m pip venv venv
source /venv/bin/activate
python3 -m pip install -r requirements.txt
```

**2. Re-create virtual enviornment** (Windows - CMD)

```
python -m pip venv venv
\venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

**3. Create .env file in /app folder to store your config variables safely**

```
cd app
touch .env
```

**4. Write down all config variables in .env file**

```
EMAIL='your_email'
EMAILPASS='your_email_password'
SECRET_KEY='your_secret_key'
SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS=False
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
```

**5. That's all! Now you can run your app by typing...**
_make sure that you're in main folder (flask-books-app)_

```
python3 run.py
```

### 🐍 Happy hacking!
