# Basic authentication

## Definition
It is an authentication mechanism used by web applications to verify the identity of a user. It involves sending a username and password with each request, typically in the HTTP header. While it's straightforward, it's not considered secure for transmitting sensitive information over the internet without additional security measures, such as HTTPS

---

## Prerequisites

1. Client Request:
The client (e.g., a web browser or a mobile app) sends an HTTP request to the server.

2. Authorization Header:
The client includes an Authorization header in the HTTP request.

The header value is created by combining the username and password with a colon, encoding the result in Base64.
```
Authorization: Basic base64(username:password)
Authorization: Basic dXNlcjpwYXNz
```
3. Server Authentication:
The server receives the request and extracts the username and password from the `Authorization` header.
The server validates the credentials against its user database.

4. Access Granted or Denied:
If the credentials are valid, the server processes the request and responds with the requested resource.
If the credentials are invalid, the server responds with a 401 Unauthorized status, indicating that the client needs to provide valid credentials.

### Resources
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://intranet.alxswe.com/rltoken/HG5WXgSja5kMa29fbMd9Aw)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

### Learning Objectives
```
    What authentication means
    What Base64 is
    How to encode a string in Base64
    What Basic authentication means
    How to send the Authorization header
```

### Requirements
```
    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/env python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
```

### Project Tasks

| Task | Description |
| ---- | ----------- |
| 0. Simple-basic-API | Download and start your project from this `archive.zip` In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files. |

