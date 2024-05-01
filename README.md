# Project Overview
This project aims to develop a basic distributed database management system, Ntsoekhe,  specifically tailored for use in the digital health sector. It should enable secure, efficient handling  and storage of health-related data across multiple distributed nodes, ensuring data integrity,  availability, and confidentiality

The database has three nodes. The folders contains the three folders representing each node. 

# Tools Used:

-Python with FLASK (for building an application)

-SQLite (for local storage)

-RESTful APIs (for internode communication)

-Visual Studio Code (the development environment)

# Requirements/ Installations
1. Download and install git from the official website.
    You can download it here:
  ```bash
     https://git-scm.com/download
  ```
Follow these steps to ensure that git will be recognised as a command in your terminal or command prompt:

2. Download and install python 3.8. or latest version.

   Can be downloaded here:
   ```bash
   https://www.python.org/downloads/
   ```

3. Clone the repository:
   
Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, use the git clone command followed by the URL of the GitHub repository:

  ```bash
  
   git clone https://github.com/TebelloMotuba/Team-Future---NTSOEKHE
  ```
4. Add each of the folders to the visual studio code workspace. Follow these steps:

    i) Launch VSC
   
    ii) Click on "File" from the options on the tittle bar.
   
    iii) Click on "Add Folder". A file explorer window will open, allowing you to navigate to the folder you want to add to the workspace.
   
   Navigate to the project directory and select one of the folders (north, south or central).
   
    iv)  Click on "File" again to add the other folder to the workspace. Click on "Add Folder to Workspace". Select one of the two remaining folders.
         Repeat this for the other remaining folder.
5. Create virtual environments in VSC for each of the folders. Follow these steps:
   
   i) On the title bar click on "view", click "Command Palette" on the dropdown options.
   
   ii) On the text field that appears type "python: create...".
   
   iii) Select "Python: Create environment".
   
   iv) Select a folder for which to create a virtual environment.
   
   v) Select "Venv creates a '.venv'...".
   
   vi) Select the latest python version from the list.
   
   vii) You will then be asked to select dependencies to install. Click on requirements.txt and click "ok".
   
   viii) This will install the dependencies for this project such as flask and 

    
   

4. Run each node's Flask application in separate terminals:
   
   Copy the following code to run South:
```bash
cd south
python app.py
```

On a different terminal navigate to the project directory then copy  following code to run North:
```bash
cd north
python app.py
```
Copy the following code to run Central:
```bash
cd central
python app.py
```
5. Open your web browser and go to the respective ports for each node to access the healthcare system:
   
   South: http://localhost:5000
   
   Central: http://localhost:5001
   
   North: http://localhost:5002



