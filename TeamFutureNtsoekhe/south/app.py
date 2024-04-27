from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import requests
import logging

app = Flask(__name__)
DATABASE = 'south.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        contacts INT,
                        location TEXT
                    );''')
        conn.commit()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('enternew.html')

@app.route('/add_patients', methods=['POST'])
def add_patient():
    largest_id = get_largest_patient_id()

    # Get the current maximum ID from the database
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT MAX(id) FROM patients')
        max_id_result = cursor.fetchone()
        max_id = max_id_result[0] if max_id_result[0] is not None else 0

    # Increment the largest ID by 1 to generate a new ID
    new_id = max(largest_id, max_id) + 1
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    contacts = request.form['contacts']
    location = request.form['location']
    
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO patients (id, first_name, last_name, contacts, location)
                        VALUES (?, ?, ?, ?, ?)''',
                     (new_id, first_name, last_name, contacts, location))
        conn.commit()
    return redirect(url_for('all_patients'))

def get_largest_patient_id():
    # List of URLs of the nodes
    node_urls = ['http://127.0.0.1:5002/patients/json', 'http://127.0.0.1:5001/patients/json']

    # Initialize the largest ID to 0
    largest_id = 0

    for node_url in node_urls:
        try:
            response = requests.get(node_url)
            response.raise_for_status()
            patients = response.json()
            # Get the largest ID from the patients in the current node
            if patients:
                max_id = max(patient['id'] for patient in patients)
                largest_id = max(largest_id, max_id)
        except requests.RequestException as e:
            print(f"Failed to fetch patients from {node_url}: {e}")

    return largest_id

# New route to return list of patients in JSON format
@app.route('/patients/json', methods=['GET'])
def get_patients_json():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    # Convert patients to a list of dictionaries
    patients_list = [dict(patient) for patient in patients]
    return jsonify(patients_list)


# Function to fetch patients from the local database
def list_patients_local():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return [dict(patient) for patient in patients]

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Function to fetch patients from other nodes (South and North)
def fetch_patients_from_nodes():
    # URLs of the South and North nodes
    nodes = ['http://127.0.0.1:5002/patients/json', 'http://127.0.0.1:5001/patients/json']
    all_patients = []
    for node in nodes:
        try:
            response = requests.get(node)
            response.raise_for_status()
            all_patients.extend(response.json())
        except requests.RequestException as e:
            print(f"Failed to fetch from {node}: {e}")
    return all_patients




@app.route('/all_patients', methods=['GET'])
def all_patients():
    # Fetch local patients first
    local_patients = list_patients_local()
    # Then fetch patients from other nodes
    fetched_patients = fetch_patients_from_nodes()
    # Combine results
    all_patients = local_patients + fetched_patients
    return render_template('list_patients.html', patients=all_patients, all_nodes=True)

@app.route('/search_patient', methods=['POST'])
def search_patient():
    search_query = request.form['search_query']
    # Search in local database
    local_patients = search_patients_local(search_query)
    # Search in other nodes
    fetched_patients = search_patients_in_nodes(search_query)
    # Combine results
    search_results = local_patients + fetched_patients
    return render_template('list_patients.html', patients=search_results, all_nodes=True)


def search_patients_local(query):
    conn = get_db_connection()
    patients = conn.execute("SELECT * FROM patients WHERE first_name LIKE ? OR last_name LIKE ?", 
                            ('%'+query+'%', '%'+query+'%')).fetchall()
    conn.close()
    return [dict(patient) for patient in patients]

NODES_SEARCH_URLS = ['http://127.0.0.1:5001/search_patients', 'http://127.0.0.1:5002/search_patients']

def search_patients_in_nodes(query):
    search_results = []
    for url in NODES_SEARCH_URLS:
        try:
            response = requests.get(url, params={'query': query})
            response.raise_for_status()  # Raises an exception for 4XX or 5XX responses
            patients = response.json()
            search_results.extend(patients)
        except requests.RequestException as e:
            print(f"Failed to search in {url}: {e}")
    return search_results



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_patient(id):
    conn = get_db_connection()
    # Handle the form submission (POST request)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contacts = request.form['contacts']
        location = request.form['location']

        conn.execute('UPDATE patients SET first_name = ?, last_name = ?, contacts = ?, location = ? WHERE id = ?',
                     (first_name, last_name, contacts, location, id))
        conn.commit()
        conn.close()
        return redirect(url_for('all_patients'))

    # Handle the display of the form with existing patient data (GET request)
    patient = conn.execute('SELECT * FROM patients WHERE id = ?', (id,)).fetchone()
    conn.close()
    if patient is None:
        return "Patient not found", 404
    
    return render_template('update_patient.html', patient=patient)

# @app.route('/delete/<int:id>', methods=['POST'])
# def delete_patient(id):
#     conn = get_db_connection()
#     conn.execute('DELETE FROM patients WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('all_patients'))

# @app.route('/delete_patient', methods=['POST'])
# def delete_patient_node():
#     data = request.json
#     patient_id = data.get('id')

#     if patient_id is None:
#         return jsonify({"error": "Patient ID is missing"}), 400

#     conn = get_db_connection()
#     conn.execute('DELETE FROM patients WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()

#     return jsonify({"message": f"Patient with ID {id} deleted successfully"}), 200


@app.route('/delete/<int:id>', methods=['POST'])
def delete_patient(id):
    # Forward the delete request to other nodes
    delete_patient_from_nodes(id)
    
    # Delete the patient locally
    conn = get_db_connection()
    conn.execute('DELETE FROM patients WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": f"Patient with ID {id} deleted successfully"}), 200

@app.route('/delete_patient', methods=['POST'])
def delete_patient_node():
    data = request.json
    patient_id = data.get('patient_id')

    if patient_id is None:
        return jsonify({"error": "Patient ID is missing"}), 400

    # Delete the patient from the local database
    conn = get_db_connection()
    conn.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Patient with ID {patient_id} deleted successfully"}), 200


def delete_patient_from_nodes(id):
    # URLs of the South and North nodes
    nodes = ['http://127.0.0.1:5000/delete_patient', 'http://127.0.0.1:5001/delete_patient']
    
    for node in nodes:
        try:
            response = requests.post(node, json={"patient_id": id})
            response.raise_for_status()
            print(f"Patient with ID {id} deleted successfully from {node}")
        except requests.RequestException as e:
            print(f"Failed to delete patient with ID {id} from {node}: {e}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
