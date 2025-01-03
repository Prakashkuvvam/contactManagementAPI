import unittest
import json
from app import app  # Replace 'app' with your script's name if different

class TestContactAPI(unittest.TestCase):

    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True

    def test_add_contact(self):
        # Add a new contact
        response = self.app.post(
            '/add-contact',
            data=json.dumps({"first_name": "John", "phone_number": "1234567890"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Contact added successfully", response.get_data(as_text=True))

        # Test duplicate contact
        response = self.app.post(
            '/add-contact',
            data=json.dumps({"first_name": "John", "phone_number": "1234567890"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)
        self.assertIn("Contact with this name and phone number already exists", response.get_data(as_text=True))

    def test_update_contact(self):
        # Add a contact first
        self.app.post(
            '/add-contact',
            data=json.dumps({"first_name": "Jane", "phone_number": "9876543210"}),
            content_type='application/json'
        )

        # Update the contact
        response = self.app.put(
            '/update-contact',
            data=json.dumps({"first_name": "Jane", "phone_number": "5555555555"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Contact updated successfully", response.get_data(as_text=True))

        # Try to update a non-existent contact
        response = self.app.put(
            '/update-contact',
            data=json.dumps({"first_name": "NonExistent", "phone_number": "1111111111"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn("Contact not found", response.get_data(as_text=True))

    def test_delete_contact(self):
        # Add a contact first
        self.app.post(
            '/add-contact',
            data=json.dumps({"first_name": "Mark", "phone_number": "4444444444"}),
            content_type='application/json'
        )

        # Delete the contact
        response = self.app.delete(
            '/delete-contact',
            data=json.dumps({"first_name": "Mark"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Contact deleted successfully", response.get_data(as_text=True))

        # Try to delete a non-existent contact
        response = self.app.delete(
            '/delete-contact',
            data=json.dumps({"first_name": "NonExistent"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)  # Deletes silently if not found

    def test_search_contact(self):
        # Add a contact first
        self.app.post(
            '/add-contact',
            data=json.dumps({"first_name": "Alice", "phone_number": "1112223333"}),
            content_type='application/json'
        )

        # Search for the contact
        response = self.app.get('/search-contact?first_name=Alice')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Contact found", response.get_data(as_text=True))

        # Search for a non-existent contact
        response = self.app.get('/search-contact?first_name=Bob')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Contact not found", response.get_data(as_text=True))

    def test_get_contacts(self):
        # Add a contact
        self.app.post(
            '/add-contact',
            data=json.dumps({"first_name": "Eve", "phone_number": "7777777777"}),
            content_type='application/json'
        )

        # Get all contacts
        response = self.app.get('/contacts')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Eve", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
