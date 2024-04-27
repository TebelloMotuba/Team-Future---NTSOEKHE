This project aims to develop a basic distributed database management system, Ntsoekhe, 
specifically tailored for use in the digital health sector. It should enable secure, 
efficient handling and storage of health-related data across multiple distributed nodes, 
ensuring data integrity, availability, and confidentiality Our database has three nodes. 

Tools used:
Python with FLASK (for building an application)
SQLite (for local storage)
RESTful APIs (for internode communication)


The three folders(central/north/south) each represent a node. 

Step by step guide to running this project:

1. Add all the three folders each to visual studio 
code ( the environment we have used. It is necessary to install python extensions: python and python debugger).

2. Create a virtual environment on each folder. 

3. Execute the following command on the python terminal in the virtual environment: 

"python -m pip install -r requirements.txt" 

This will install all the necessary tools needed to run this project such as FLASK. 

4. When the installations have completed, the user should run the python file "app.py". 
This will generate the port at which the node is running. 

5. Copy the URL and paste it in the browser. 

6. Do step 1 to 5 for all the nodes. 
Each node will generate its own port. When all the nodes are running on their ports, 
the user can be able to view and manage patients in both local and other nodes.
