# User authentication service
Ensures that only authorized individuals can interact with the system and its features

## Key Components

1. User Database:
Stores user credentials securely, usually in the form of usernames and hashed passwords
May include additional user information such as email addresses, roles, or permissions.

2. Authentication Mechanisms:
Password-based: Users provide a password associated with their account.
Multi-factor authentication (MFA): Requires users to provide two or more authentication factors (e.g., password, SMS code, fingerprint) for increased security

3. Session Management:
After successful authentication, a session is established to maintain the user's authenticated state.
Session tokens or cookies are often used to manage and validate sessions.

4. Token-based Authentication:
Utilizes tokens (e.g., JSON Web Tokens - JWT) to authenticate users instead of sending credentials with each request.
Enhances security by reducing the need to store sensitive information on the client side.

5. OAuth and OpenID Connect:
OAuth is a protocol for authorization, while OpenID Connect is an authentication layer on top of OAuth.
Widely used for third-party authentication, allowing users to log in using existing credentials from providers like Google, Facebook, or GitHub.

## Resources
- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
- [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

### Learning Objectives
```
    How to declare API routes in a Flask app
    How to get and set cookies
    How to retrieve request form data
    How to return various HTTP status codes
```

### Requirements
```
    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/env python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5)
    You should use SQLAlchemy 1.3.x
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    All your functions should be type annotated
    The flask app should only interact with Auth and never with DB directly.
    Only public methods of Auth and DB should be used outside these classes
```

### Setup
```
pip3 install bcrypt
```

### Project Tasks

0. User model 
```
In this task you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).

The model will have the following attributes:

    id, the integer primary key
    email, a non-nullable string
    hashed_password, a non-nullable string
    session_id, a nullable string
    reset_token, a nullable string
```

1. create user 
In this task, you will complete the `DB` class provided below to implement the `add_user` method.
```
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```
Note that `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.
Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object. The method should save the user to the database. No validations are required at this stage.

2. Find user 
In this task you will implement the DB.find_user_by method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point.
Make sure that SQLAlchemy’s NoResultFound and InvalidRequestError are raised when no results are found, or when wrong query arguments are passed, respectively.
- Warning:
NoResultFound has been moved from sqlalchemy.orm.exc to sqlalchemy.exc between the version 1.3.x and 1.4.x of SQLAchemy - please make sure you are importing it from sqlalchemy.orm.exc

3. update user 
In this task, you will implement the DB.update_user method that takes as argument a required user_id integer and arbitrary keyword arguments, and returns None.
The method will use find_user_by to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.
If an argument that does not correspond to a user attribute is passed, raise a ValueError.

4. Hash password 
In this task you will define a _hash_password method that takes in a password string arguments and returns bytes.
The returned bytes is a salted hash of the input password, hashed with bcrypt.hashpw

5. Register user
In this task, you will implement the Auth.register_user in the Auth class provided below:
```
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
```
Note that Auth._db is a private property and should NEVER be used from outside the class.
Auth.register_user should take mandatory email and password string arguments and return a User object
If a user already exist with the passed email, raise a ValueError with the message User <user's email> already exists.
If not, hash the password with _hash_password, save the user to the database using self._db and return the User object


