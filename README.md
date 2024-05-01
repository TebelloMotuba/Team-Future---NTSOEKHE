# Project Overview
This project aims to develop a basic distributed database management system, Ntsoekhe,  specifically tailored for use in the digital health sector. It should enable secure, efficient handling  and storage of health-related data across multiple distributed nodes, ensuring data integrity,  availability, and confidentiality

The database has three nodes. The folders contains the three folders representing each node. 

#Requirements/ Installations
To be able to use the files, the user should download all files and add all the three folders each to visual studio code ( the environment we have used. It is necessary to install python extensions; python and python debugger).

Create a virtual environment on each folder. They should then run the following command on the python terminal in the virtual environment:

"python -m pip install -r requirements.txt" 

This will install all the necessary tools needed to run this project such as FLASK.

When the installations have completed, run the file "app.py". This will generate the port at which the node is running. Copy the URL and paste it in the browser.

Do this for all the nodes. Each node has its own port. When all the ports are running, the user can be able to view and manage patients in both local and other nodes. 

#How to run the project

