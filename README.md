# TeamFuture Ntsoekhe 

# Project Overview
This project aims to develop a basic distributed database management system, Ntsoekhe,  specifically tailored for use in the digital health sector. It should enable secure, efficient handling  and storage of a patient's health data across multiple distributed nodes, ensuring data integrity,  availability, and confidentiality.

The database has one relation named "patients" and it is fragmented horizontally based on location/region. No replication. Each node stores its data locally using SQLite. Central node stores the patients information for patients residing in the central resgion of Lesotho. South node for South region patients and North node for North region patients.
The achitecture used is peer-to-peer, with all nodes being equal and each node having its own server.

# Tools Used:

-Python with FLASK (for building an application)

-SQLite (for local storage)

-RESTful APIs (for internode communication)

-Visual Studio Code (the development environment)

# Requirements/ Installations
1. **Download and install git from the official website.**
   
    *Can be downloaded here:*
  ```bash
     https://git-scm.com/download
  ```
*Follow these steps to ensure that git will be recognised as a command in your terminal or command prompt:*

   - In the Start Menu or taskbar search, search for "environment variable".
   - Select "Edit the system environment variables".
   - Click the "Environment Variables" button at the bottom.
   - Double-click the "Path" entry under "System variables".
   With the "New" button in the PATH editor, add C:\Program Files\Git\bin\ and
     C:\Program Files\Git\cmd\ to the end of the list.
   - Close and re-open your console.

2. **Download and install python 3.11.9 or latest version.**

   *Can be downloaded here:*
   ```bash
   https://www.python.org/downloads/
   ```

3. **Clone the repository:**
   
Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, use the git clone command followed by the URL of the GitHub repository:

*Copy this command and paste it in command prompt or terminal:*

  ```bash
  
   git clone https://github.com/TebelloMotuba/Team-Future---NTSOEKHE
  ```

The project folder containing all the files will be created on the directory you have specified.

4. **Add each of the folders to the visual studio code workspace.**
   
    *Follow these steps:*

    - Launch VSC
   
    - Click on "File" from the options on the tittle bar.
   
    - Click on "Add Folder". A file explorer window will open, allowing you to navigate to the folder you want to add to the workspace.
   
      Navigate to the project directory and select one of the folders (north, south or central).
   
    -  Click on "File" again to add the other folder to the workspace. Click on "Add Folder to Workspace". Select one of the two remaining folders.
         Repeat this for the other remaining folder.
5. **Create virtual environments in VSC for each of the folders.**
  
   *Follow these steps:*
   
   - On the title bar click on "view", click "Command Palette" on the dropdown options.
   
   - On the text field that appears type "python: create...".
   
   - Select "Python: Create environment".
   
   - You will be asked to select the environment type. Select "Venv creates a '.venv'...".

   - Select a folder for which to create a virtual environment.
   
   - You will be asked to select a python installation. Select the latest python version from the list.
   
   - You will then be asked to select dependencies to install. Click on "requirements.txt" and click "ok".
   
   - This will install the dependencies for this project such as flask and requests API.

    
   

6. **Run each node's Flask application in separate terminals:**
   
  Navigate to the project directory on terminal/ command prompt and execute the following code to run node South:
```bash
cd south
python app.py
```
It will generate a url at which it is running. Copy it and paste it in the browser to access the healthcare system from South node.

On a different terminal, navigate to the project directory then execute the following code to run node North:
```bash
cd north
python app.py
```
It will generate a url at which it is running. Copy it and paste it in the browser to access the healthcare system from North node.

On a different terminal, navigate to the project directory then execute the following code to run node Central:
```bash
cd central
python app.py
```
It will generate a url at which it is running. Copy it and paste it in the browser to access the healthcare system from Central node.

# Usage
- **Displaying the list of patients:**

The home page gives a doctor an option to view either local (current region) patients or all country patients.
On viewing all country patients, the node communicates with other nodes through requests (RESTful API) to retrieve thier database records in order to display all patients from all the three nodes.

- **Searching for Patient Records:** 

After choosing any of the two lists, the user can use the search form at the top of the page to search for patient records by name. Enter the patient's name in the search field and click `Search` button to view matching results. This is necessary in cases where the patient list is too long.

- **Adding a New Patient Record:** 

Click on the `Add New Patient` button and fill out the required fields in the form. Select the patient's location from the dropdown list (South, Central, or North) and click `Submit` button to add the record.

*Currently, the doctors are allowed to add patients only at their nodes. We are yet to finalise and make a decision on whether it is necessary for a doctor who is in the South region to add a patient residing in the North.*

- **Updating a Patient Record:** 

Click on the `Update` button next to the patient record that they want to modify. The update form will appear with the current details pre-filled. Make any necessary changes and click `Save Changes` button to update the record. 


- **Deleting a Patient Record:** 

Click on the `Delete` button next to the patient record you want to remove. Confirm the deletion when prompted.

# Development
The Flask application, defined in `app.py`, serves as the backend of the distributed database management system. Below is the break down of how each part of the code achieves the purpose of the project:

1. **Initialization and Configuration:**
   - The application is initialized and configured with Flask.
   - A SQLite database, e.g `south.db`, is used for storing patient records.
   - The `init_db()` function initializes the database by creating a `patients` table if it does not exist already.
   - The `get_db_connection()` function establishes a connection to the SQLite database.
  
2. **Routes and Views:**

- **Home Route (`'/'`):**
   - Renders the home page (`home.html`) which provides navigation options to view all patients or add a new patient.

- **Add Patient Route (`'/add_patients'`):**
   - Accepts POST requests to add a new patient record to the local database.
   - Generates a new patient ID based on the largest ID found across all nodes.
   - Inserts the new patient record into the local database.
   - Redirects to the route for displaying all patients.
   - The `get_largest_patient_id()` function retrieves the largest patient ID across all nodes to generate a unique ID for a new patient.

- **Get Patients JSON Route (`'/patients/json'`):**
   - Returns JSON representation of all patients stored in the local database.
   - The `list_patients_local()` function retrieves a list of patients stored locally on the current node.

- **All Patients Route (`'/all_patients'`):**
   - Fetches all patients from the local database and other nodes.
   - The `list_patients_local()` function retrieves a list of patients stored locally on the current node.
   - The `fetch_patients_from_nodes()` function fetches patient records from other nodes via RESTful APIs.
   - Renders the page (`list_patients.html`) displaying a list of all patients.

- **Search Patient Route (`'/search_patient'`):**
   - Accepts POST requests with a search query.
   - Searches for matching patient records in the local database and other nodes.
   - Renders the page (`list_patients.html`) displaying search results.

- **Update Patient Route (`'/update'`):**
   - Accepts POST requests to update a patient record in the local database.
   - Updates the patient record with the provided data (first name, last name, contacts, location).
   - Also, forwards the update request to other nodes to ensure data consistency.
   - The `update_patient()` function updates a patient's information in the local database when the form is submitted.
   - The `update_patient_node()` function updates a patient's information on other nodes via RESTful APIs.

- **Delete Patient Route (`'/delete/<int:id>'`):**
   - Accepts POST requests to delete a patient record from the local database.
   - The `delete_patient()` function deletes a patient with a specified ID from the local database and forwards the deletion request to other nodes.

- **Delete Patient Node Route (`'/delete_patient'`):**
   - Accepts POST requests to delete a patient record from other nodes.
   - This route is used internally by other nodes to synchronize data deletion.
   - The `delete_patient_node()` function deletes a patient from other nodes via RESTful APIs.
   
   
3. **RESTful APIs:**
   - The `/patients/json` route exposes a JSON endpoint to retrieve patient records.
   - The `/update` and `/delete/<int:id>` routes handle patient update and deletion requests, respectively, using RESTful APIs.
   
4. **Node Communication:**
   - Patient data is synchronized across nodes through inter-node communication using requests to exchange patient information.

Each function within app.py is responsible for interacting with the local SQLite database, handling HTTP requests, and ensuring data consistency across distributed nodes. By implementing these routes and functions, the Flask application effectively manages patient data in a distributed environment, providing functionalities for adding, updating, searching, and deleting patient records while ensuring data integrity and availability.


