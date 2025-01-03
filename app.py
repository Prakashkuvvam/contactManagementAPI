from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" to store data
data_store = []

@app.route('/add-contact', methods=['POST'])
def add_contact():
    payload = request.get_json()
    first_name = payload.get('first_name')
    phone_number = payload.get('phone_number')

    if not first_name or not phone_number:
        return jsonify({"error": "Missing required fields"}), 400

    # Check for duplicates (same first_name and phone_number)
    for contact in data_store:
        if contact['first_name'] == first_name and contact['phone_number'] == phone_number:
            return jsonify({"error": "Contact with this name and phone number already exists"}), 409

    data_store.append({"first_name": first_name, "phone_number": phone_number})
    return jsonify({"message": "Contact added successfully", "data": data_store}), 201

@app.route('/update-contact', methods=['PUT'])
def update_contact():
    payload = request.get_json()
    first_name = payload.get('first_name')
    phone_number = payload.get('phone_number')

    if not first_name or not phone_number:
        return jsonify({"error": "Missing required fields"}), 400

    # Update contact
    for contact in data_store:
        if contact['first_name'] == first_name:
            contact['phone_number'] = phone_number
            return jsonify({"message": "Contact updated successfully", "data": data_store}), 200

    return jsonify({"error": "Contact not found"}), 404

@app.route('/delete-contact', methods=['DELETE'])
def delete_contact():
    payload = request.get_json()
    first_name = payload.get('first_name')

    if not first_name:
        return jsonify({"error": "Missing required fields"}), 400

    # Delete contact
    global data_store
    data_store = [contact for contact in data_store if contact['first_name'] != first_name]

    return jsonify({"message": "Contact deleted successfully", "data": data_store}), 200

@app.route('/search-contact', methods=['GET'])
def search_contact():
    first_name = request.args.get('first_name')

    if not first_name:
        return jsonify({"error": "Missing query parameter: first_name"}), 400

    # Search for contact
    for contact in data_store:
        if contact['first_name'] == first_name:
            return jsonify({"message": "Contact found", "data": contact}), 200

    return jsonify({"error": "Contact not found"}), 404

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({"contacts": data_store}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
