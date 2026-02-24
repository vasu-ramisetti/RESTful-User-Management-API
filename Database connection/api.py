from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='(Lsvs1919)',
        database='api_demo1'
    )

# GET API to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

# POST API to insert new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)", 
        (name, email)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully"}), 201
@app.route('/users', methods=['DELETE'])
def delete_user():
    data = request.json
    name = data['name']
    email = data['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE users from VALUES name=%s and email=%s", 
        (name, email)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

