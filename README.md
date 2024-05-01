# Project Overview
This project aims to develop a basic distributed database management system, Ntsoekhe,  specifically tailored for use in the digital health sector. It should enable secure, efficient handling  and storage of a patient's health data across multiple distributed nodes, ensuring data integrity,  availability, and confidentiality.

The database is fragmented horizontally based on location/region. No replication. Each node stores its data locally using SQLite. Central node stores the patients information for patients residing in the central resgion of Lesotho. South node for South region patients and North node for North region patients.
The achitecture used is peer-to-peer, with all nodes being equal and each node having its own server.

# Tools Used:

-Python with FLASK (for building an application)

-SQLite (for local storage)

-RESTful APIs (for internode communication)

-Visual Studio Code (the development environment)

# Requirements/ Installations
1. **Download and install git from the official website.**
    *You can download it here:*
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

2. **Download and install python 3.8. or latest version.**

   *Can be downloaded here:*
   ```bash
   https://www.python.org/downloads/
   ```

3. **Clone the repository:**
   
Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, use the git clone command followed by the URL of the GitHub repository:

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
6. **Create virtual environments in VSC for each of the folders.**
  
   *Follow these steps:*
   
   - On the title bar click on "view", click "Command Palette" on the dropdown options.
   
   - On the text field that appears type "python: create...".
   
   - Select "Python: Create environment".
   
   - You will be asked to select the environment type. Select "Venv creates a '.venv'...".

   - Select a folder for which to create a virtual environment.
   
   - You will be asked to select a python installation. Select the latest python version from the list.
   
   - You will then be asked to select dependencies to install. Click on "requirements.txt" and click "ok".
   
   - This will install the dependencies for this project such as flask and requests API.

    
   

7. **Run each node's Flask application in separate terminals:**
   
  Navigate to the project directory and execute the following code to run node South:
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
**Adding a New Patient Record:** 

Click on the "Add New Patient" button and fill out the required fields in the form. Select the patient's location from the dropdown list (South, Central, or North) and click "Submit" to add the record.

**Updating a Patient Record:** 

Click on the "Update" button next to the patient record you want to modify. The update form will appear with the current details pre-filled. Make any necessary changes and click "Save Changes" to update the record.

**Searching for Patient Records:** 

Use the search form at the top of the page to search for patient records by name. Enter the patient's name in the search field and click "Search" to view matching results.

**Deleting a Patient Record:** 

Click on the "Delete" button next to the patient record you want to remove. Confirm the deletion when prompted



