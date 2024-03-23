from flask import Flask, request, jsonify
import hashlib
import pymysql.cursors

app = Flask(__name__)

# MariaDB Configuration
db_config = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'database_name',
    'cursorclass': pymysql.cursors.DictCursor
}

# connection = pymysql.connect(**db_config)

@app.route('/api/data', methods=['POST'])
def save_data():
    # Get request data
    data = request.get_json()

    # Extract string1 and string2 from the request data
    survey_result = data.get('survey_result')

    # Get user's IP address
    user_ip = request.remote_addr

    # Hash the user's IP address
    hashed_ip = hashlib.sha256(user_ip.encode()).hexdigest()

    # Check if the user with the same hashed IP has already submitted data
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM survey_phase_responses WHERE hashed_ip_address = %s", (hashed_ip,))
    #     existing_submission = cursor.fetchone()
    #
    #     if existing_submission:
    #         # User has already submitted data
    #         return jsonify({'error': 'You have already submitted data.'}), 400
    #
    #     # Save data to the database
    #     cursor.execute("INSERT INTO survey_phase_responses (survey_result, hashed_ip_address) VALUES (%s, %s)",
    #                    (survey_result, hashed_ip))
    #     connection.commit()

    return jsonify({'message': 'Data saved successfully.'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
