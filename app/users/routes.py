from flask import Blueprint, request, jsonify
from app import db
from app.users.models import User
from app.users.schemas import user_schema, users_schema
from app.users.utils import validate_user_data, email_exists

user_bp = Blueprint('user', __name__)


@user_bp.route('', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    tags:
      - Users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
              description: User's name
            email:
              type: string
              description: User's unique email
    responses:
      201:
        description: User created successfully
      400:
        description: Invalid input or email already exists
    """
    data = request.get_json()

    validated_data, errors = validate_user_data(user_schema, data)
    if errors:
        return jsonify({"error": "Validation error", "details": errors}), 400

    if email_exists(User, data.get('email')):
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user": user_schema.dump(new_user)}), 201


@user_bp.route('', methods=['GET'])
def get_all_users():
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of all users
    """
    users = db.session.scalars(db.select(User)).all()
    return jsonify({"users": users_schema.dump(users)}), 200


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a specific user by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID
    responses:
      200:
        description: User found and returned
      404:
        description: User not found
    """
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user": user_schema.dump(user)}), 200


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: User's name
            email:
              type: string
              description: User's unique email
    responses:
      200:
        description: User updated successfully
      400:
        description: Invalid input or email already used by another user
      404:
        description: User not found
    """
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    validated_data, errors = validate_user_data(user_schema, data)
    if errors:
        return jsonify({"error": "Validation error", "details": errors}), 400

    if 'email' in data and data['email'] != user.email:
        if email_exists(User, data['email']):
            return jsonify({"error": "Email already in use by another user"}), 400

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()

    return jsonify({"message": "User updated successfully", "user": user_schema.dump(user)}), 200


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200
