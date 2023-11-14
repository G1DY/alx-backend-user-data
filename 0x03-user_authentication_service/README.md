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

