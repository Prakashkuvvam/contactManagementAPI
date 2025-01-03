# Flask Contact Management API

This is a simple Flask-based API for managing contacts. It supports CRUD operations: adding, updating, deleting, and searching contacts.

## Features:
- **Add Contact**: Add a new contact with `first_name` and `phone_number`.
- **Update Contact**: Update a contact's phone number by `first_name`.
- **Delete Contact**: Delete a contact by `first_name`.
- **Search Contact**: Search for a contact by `first_name`.
- **Get All Contacts**: Retrieve all stored contacts.

## Endpoints

### 1. **POST `/add-contact`**
   - **Description**: Adds a new contact with `first_name` and `phone_number`.
   - **Request Example**:
     ```bash
     POST /add-contact
     Content-Type: application/json

     {
       "first_name": "John",
       "phone_number": "1234567890"
     }
     ```
   - **Response Example**:
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
   - **Error Response (Duplicate Contact)**:
     ```json
     {
       "error": "Contact with this name and phone number already exists"
     }
     ```
     - Status Code: `409`

### 2. **PUT `/update-contact`**
   - **Description**: Updates a contact's phone number using `first_name`.
   - **Request Example**:
     ```bash
     PUT /update-contact
     Content-Type: application/json

     {
       "first_name": "John",
       "phone_number": "9876543210"
     }
     ```
   - **Response Example**:
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
   - **Error Response (Contact Not Found)**:
     ```json
     {
       "error": "Contact not found"
     }
     ```
     - Status Code: `404`

### 3. **DELETE `/delete-contact`**
   - **Description**: Deletes a contact by `first_name`.
   - **Request Example**:
     ```bash
     DELETE /delete-contact
     Content-Type: application/json

     {
       "first_name": "John"
     }
     ```
   - **Response Example**:
     ```json
     {
       "message": "Contact deleted successfully",
       "data": []
     }
     ```
   - **Error Response (Contact Not Found)**:
     ```json
     {
       "message": "Contact deleted successfully",
       "data": []
     }
     ```
     - Status Code: `200` (Note: Deletion is silent if the contact does not exist)

### 4. **GET `/search-contact`**
   - **Description**: Searches for a contact by `first_name`.
   - **Request Example**:
     ```bash
     GET /search-contact?first_name=John
     ```
   - **Response Example**:
     ```json
     {
       "message": "Contact found",
       "data": {
         "first_name": "John",
         "phone_number": "1234567890"
       }
     }
     ```
   - **Error Response (Contact Not Found)**:
     ```json
     {
       "error": "Contact not found"
     }
     ```
     - Status Code: `404`

### 5. **GET `/contacts`**
   - **Description**: Retrieves all contacts in the system.
   - **Request Example**:
     ```bash
     GET /contacts
     ```
   - **Response Example**:
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

## Installation

1. Clone the repository:

   ```bash
   git clone [<repository-url>](https://github.com/Prakashkuvvam/contactManagementAPI.git)
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

## Code Coverage Testing

To check the test coverage of your code, we use `coverage.py`.

### How to Run Code Coverage:

1. Install `coverage.py`:

   ```bash
   pip install coverage
   ```

2. Run the tests with coverage tracking:

   ```bash
   coverage run -m unittest test_app.py
   ```

3. Generate a code coverage report:

   ```bash
   coverage report
   ```

   This will print a summary of the coverage in your terminal.

4. (Optional) Generate an HTML report for easier viewing:

   ```bash
   coverage html
   ```

   Open the `htmlcov/index.html` file in your browser to view the detailed code coverage report.

### Example Output:

After running the tests with coverage, you will see a report similar to:

```bash
$ coverage report
Name               Stmts   Miss  Cover
--------------------------------------
app.py               45      4    91%
test_app.py          27      2    93%
--------------------------------------
TOTAL                72      6    92%
```

This means that your code is **92% covered** by the unit tests.

### Notes:

- You can exclude certain lines from coverage by adding `# pragma: no cover` in the code.
- Ensure that your tests are comprehensive to cover as much code as possible.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Updates:
- **Request and Response Examples**: For each API endpoint, I’ve added examples for both the request and the expected response.
- **Error Responses**: Provided sample error responses to make the error handling clearer for users interacting with the API.

This version should give users and developers a comprehensive guide on how to use your API, along with examples for each request. You can copy and paste this directly into your `README.md` file. Let me know if you need any further adjustments!
