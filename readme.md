# Django REST API Authentication System

This Django REST API is designed to provide a secure and reliable authentication system for your web applications. It allows users to register, log in, and perform authenticated actions using token-based authentication.

## Prerequisites

- Python 3.7 or above
- Django 3.0 or above
- Django REST Framework 3.11 or above

## Installation

1. Clone the repository:
```shell
git clone 
```
2. Navigate to the project directory:
```shell
cd project
```
3. Install the dependencies:
```shell
pip install -r requirements.txt
```
4. Set up the database:
```shell
python manage.py migrate
```
5. Start the development server:
```shell
python manage.py runserver
```

## API Endpoints

### Registration

- `POST /api/create/`

Registers a new user with the provided username, email, and password.

**Request Body:**

```json
{
 "username": "your-username",
 "email": "your-email@example.com",
 "password": "your-password"
}
```

Response:
```json
{
  "id": 1,
  "username": "your-username",
  "email": "your-email@example.com"
}
```
### Login
- `POST /api/token/`

Authenticates a user and generates an authentication token.

**Request Body:**
```json
{
  "username": "your-username",
  "password": "your-password"
}
```
Response:
```json
{
  "token": "your-authentication-token"
}
```

### User Profile
- `GET /api/me/`
Retrieves the authenticated user's profile information. </br>
`Note:`Authentication toke is needed on header inorder to recive data
```shell
Authorization: Token your-authentication-token
```
Response:
```json
{
  "id": 1,
  "username": "your-username",
  "email": "your-email@example.com"
}
```
### Error Handling
The API follows RESTful principles and returns appropriate status codes and error messages for invalid requests. Here are some common error responses:

- 400 Bad Request: Invalid request data.
- 401 Unauthorized: Missing or invalid authentication token.
- 404 Not Found: Resource not found.
- 500 Internal Server Error: Unexpected server error.

### Conclusion
With this Django REST API authentication system, you can easily integrate user registration, login, and secure authenticated actions into your web applications. Feel free to customize and extend the API to fit your specific requirements.