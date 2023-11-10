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


