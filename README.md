# Project Overview
This project aims to develop a basic distributed database management system, Ntsoekhe,  specifically tailored for use in the digital health sector. It should enable secure, efficient handling  and storage of health-related data across multiple distributed nodes, ensuring data integrity,  availability, and confidentiality

The database has three nodes. The folders contains the three folders representing each node. 

# Requirements/ Installations
1. Download and install git from the official website.
    You can download it here:
  ```bash
     https://git-scm.com/download
  ```
2. Clone the repository:
Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, use the git clone command followed by the URL of the GitHub repository:

  ```bash
  
   git clone https://github.com/TebelloMotuba/Team-Future---NTSOEKHE
  ```
3. Navigate to the project directory:
   Copy the following code:
  ```bash
  cd Team-Future---NTSOEKHE
  ```
4. Run each node's Flask application in separate terminals:
   Copy the following code running South:
```bash
cd south
python app.py
```

Copy the following code for running North:
```bash
cd ../north
python app.py
```
Copy the following code for running Central:
```bash
cd ../central
python app.py
```
5. Open your web browser and go to the respective ports for each node to access the healthcare system:
   
   South: http://localhost:5000
   
   Central: http://localhost:5001
   
   North: http://localhost:5002



