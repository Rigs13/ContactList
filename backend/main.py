# Main routes or endpoints; CRUD Application approach
from flask import request, jsonify
from config import app, db
from models import Contact

# get for contact endpoint
@app.route('/contacts', methods=['GET'])
def get_contacts():
    # handle get requests
    contacts = Contact.query.all()
    # create json list from python using to_json method
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({'contacts': json_contacts})

# create context
@app.route('/create_contact', methods=['POST'])
def create_contact():
    # get the data for the contact to create
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')

    if not first_name or not last_name or not email:
        return (
            jsonify({'message': "You must include a first name, last name, and email."}),
            400,
        )

    # create new contact
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    # add contact to the db
    try:
        db.session.add(new_contact)
        db.session.commit()
    # catch exceptions and return the error with a bad request code
    except Exception as e:
        return jsonify({'message': str(e)}), 400

    # return feedback after passing try/except block (201 specific)
    return jsonify({"message": "Contact has been created."}), 201


# update context
@app.route('/update_contact/<int:user_id>', methods=['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    # check if user exists
    if not contact:
        return jsonify({'message': 'Contact not found.'}), 404

    # dictionary retrieval
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)

    # commit the updated information
    db.session.commit()

    return jsonify({'message': 'Contact has been updated.'}), 200


# Deletion context
@app.route('/delete_contact/<int:user_id>', methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    # check if user exists
    if not contact:
        return jsonify({'message': 'Contact not found.'}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message': 'Contact has been deleted.'}), 200


# run the application
if __name__ == '__main__':
    # instance of db
    with app.app_context():
        db.create_all()

    app.run(debug=True)
