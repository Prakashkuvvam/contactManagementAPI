# Contact Management API

This is a simple Flask-based REST API for managing contacts. It allows users to:

- Add a new contact
- Update an existing contact
- Delete a contact
- Search for a contact
- Retrieve all contacts

## Prerequisites

Ensure you have the following installed on your local machine:

- Python (>= 3.6)
- `pip` (Python package manager)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
The server will start at `http://0.0.0.0:5000`.

## API Endpoints

### 1. Add a Contact
- **Endpoint**: `POST /add-contact`
- **Request Body**:
  ```json
  {
    "first_name": "John",
    "phone_number": "1234567890"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Contact added successfully",
    "data": [
      {
        "first_name": "John",
        "phone_number": "1234567890"
      }
    ]
  }
  ```

### 2. Update a Contact
- **Endpoint**: `PUT /update-contact`
- **Request Body**:
  ```json
  {
    "first_name": "John",
    "phone_number": "9876543210"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Contact updated successfully",
    "data": [
      {
        "first_name": "John",
        "phone_number": "9876543210"
      }
    ]
  }
  ```

### 3. Delete a Contact
- **Endpoint**: `DELETE /delete-contact`
- **Request Body**:
  ```json
  {
    "first_name": "John"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Contact deleted successfully",
    "data": []
  }
  ```

### 4. Search for a Contact
- **Endpoint**: `GET /search-contact`
- **Query Parameter**: `?first_name=John`
- **Response** (if found):
  ```json
  {
    "message": "Contact found",
    "data": {
      "first_name": "John",
      "phone_number": "1234567890"
    }
  }
  ```
- **Response** (if not found):
  ```json
  {
    "error": "Contact not found"
  }
  ```

### 5. Get All Contacts
- **Endpoint**: `GET /contacts`
- **Response**:
  ```json
  {
    "contacts": [
      {
        "first_name": "John",
        "phone_number": "1234567890"
      }
    ]
  }
  ```

## Notes

- Ensure no duplicate entries are added. If you attempt to add a contact with the same `first_name` and `phone_number`, the server will respond with:
  ```json
  {
    "error": "Contact with this name and phone number already exists"
  }
  ```
- The application is currently backed by an in-memory datastore. Data will not persist after restarting the server. For persistence, integrate a database like SQLite or PostgreSQL.

## Testing the API

You can test the API using tools like:

1. **Postman**:
   - Import the endpoints and test the requests with the appropriate headers (`Content-Type: application/json`) and body.

2. **cURL**:
   - Example: Adding a contact
     ```bash
     curl -X POST http://127.0.0.1:5000/add-contact \
     -H "Content-Type: application/json" \
     -d '{"first_name": "John", "phone_number": "1234567890"}'
     ```

3. **Python Requests Library**:
   - Example:
     ```python
     import requests

     url = "http://127.0.0.1:5000/add-contact"
     payload = {"first_name": "John", "phone_number": "1234567890"}
     response = requests.post(url, json=payload)
     print(response.json())
     ```

## Contributing

Contributions are welcome! If you'd like to add features or fix bugs, please:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

