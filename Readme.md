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


# Flask Contact Management API

This is a simple Flask-based API for managing contacts. It supports CRUD operations: adding, updating, deleting, and searching contacts.

## Features:
- **Add Contact**: Add a new contact with `first_name` and `phone_number`.
- **Update Contact**: Update a contact's phone number by `first_name`.
- **Delete Contact**: Delete a contact by `first_name`.
- **Search Contact**: Search for a contact by `first_name`.
- **Get All Contacts**: Retrieve all stored contacts.

## Endpoints

1. **POST `/add-contact`**
   - Adds a new contact with `first_name` and `phone_number`.
   - Returns `201` and a success message if the contact is added.

2. **PUT `/update-contact`**
   - Updates a contact's phone number using `first_name`.
   - Returns `200` and the updated list of contacts.

3. **DELETE `/delete-contact`**
   - Deletes a contact by `first_name`.
   - Returns `200` and the updated list of contacts.

4. **GET `/search-contact`**
   - Searches for a contact by `first_name`.
   - Returns `200` if found, `404` if not.

5. **GET `/contacts`**
   - Retrieves all contacts in the system.
   - Returns a list of contacts.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Unit Testing

Unit tests are written using the `unittest` framework and Flask's test client.

### How to Run the Tests

1. Ensure the Flask application (`app.py`) is running or ready to be tested.
2. Save the test cases in a file, for example `test_app.py`.
3. Run the tests using the following command:

   ```bash
   python -m unittest test_app.py
   ```

   This will run the unit tests and display the results in the terminal.

### What the Unit Tests Cover:

- **Add Contact**:
  - Verifies that a new contact can be added successfully.
  - Tests that attempting to add a duplicate contact returns the correct error.

- **Update Contact**:
  - Verifies that the phone number of an existing contact can be updated.
  - Tests that attempting to update a non-existent contact returns a "Contact not found" error.

- **Delete Contact**:
  - Verifies that a contact can be deleted by `first_name`.
  - Tests that attempting to delete a non-existent contact does not cause an error (it silently does nothing).

- **Search Contact**:
  - Verifies that an existing contact can be searched by `first_name`.
  - Tests that searching for a non-existent contact returns a "Contact not found" error.

- **Get Contacts**:
  - Verifies that all contacts can be retrieved.
  - Ensures that newly added contacts appear in the list.

### Example Output from Running Tests:

```bash
$ python -m unittest test_app.py
....
----------------------------------------------------------------------
Ran 5 tests in 0.004s

OK
```

## Notes

- The API uses an in-memory list (`data_store`) to store contacts, which means that data will be lost if the application is restarted.
- The application is intended for demonstration purposes and should be adapted for production with proper data storage and security mechanisms.


### Key Sections:

- **Unit Testing Instructions**: How to run the unit tests and what the tests cover.
- **What the Tests Cover**: Describes each part of the functionality tested, such as adding, updating, and deleting contacts.
- **How to Run Tests**: Detailed steps for running the unit tests with the `unittest` framework.

This README gives users and developers a comprehensive overview of how to interact with your Flask app and run tests.


## Contributing

Contributions are welcome! If you'd like to add features or fix bugs, please:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

