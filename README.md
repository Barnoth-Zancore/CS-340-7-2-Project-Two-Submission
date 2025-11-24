CS-340 Project Two – Grazioso Salvare Dashboard

Author: Morgun Leonard
Course: Client/Server Development

Project Overview

This repository contains my full implementation of the Grazioso Salvare Dashboard, created as part of CS-340 Client/Server Development. The purpose of this project was to build an interactive data dashboard that connects to a MongoDB database and displays animal shelter data relevant to rescue training selection.

The dashboard allows users at Grazioso Salvare to:

Filter dogs based on rescue type criteria

View detailed animal records in an interactive data table

Visualize outcome data with dynamic charts

See geolocation markers for each selected animal

Query MongoDB dynamically through a custom CRUD module

This project demonstrates my ability to build a full client/server application, integrate database-driven interactions, and create interactive visual analytics using Dash, Python, and MongoDB.

| Component            | Technology                                     |
| -------------------- | ---------------------------------------------- |
| Programming Language | Python 3                                       |
| Database             | MongoDB (NoSQL)                                |
| Dashboard Framework  | Dash & JupyterDash                             |
| Visualization        | Plotly Express                                 |
| Mapping              | Dash Leaflet                                   |
| Data Manipulation    | Pandas                                         |
| Cloud Environment    | Codio                                          |
| CRUD Interface       | Custom Python module (`CRUD_Python_Module.py`) |

Repository Contents

CS-340-Project-Two
│
├── ProjectTwoDashboard.ipynb        # Full working dashboard
├── CRUD_Python_Module.py            # Custom CRUD module for MongoDB
├── Project Two Morgun.docx          # Documentation with screenshots
└── README.md                        # Portfolio reflection + full project details

Dashboard Functionality
1. Interactive Filters

The dashboard allows users to select a rescue type:

Reset (All Dogs)

Water Rescue

Mountain/Wilderness Rescue

Disaster or Tracking

Each selection triggers a MongoDB query using the CRUD module. The results immediately populate the data table.

2. Interactive DataTable

The data table includes:

Sorting

Filtering

Pagination

Column highlighting

Row selection

Selecting a row updates the map display automatically.

3. Outcome Visualization Chart

A Plotly pie chart shows distribution of outcome_type for the filtered results.
This chart updates instantly whenever the filter changes.

4. Geolocation Map

Built using Dash Leaflet, the map:

Centers on Austin, Texas (AAC shelter location)

Shows a marker for the selected animal

Displays a tooltip (breed)

Displays a popup (animal name)

Database Integration (CRUD Module)

The dashboard connects to MongoDB through a reusable CRUD class:

Establishes a client connection

Handles authentication

Implements create, read, update, and delete

Ensures clean separation between logic and UI

This modular approach keeps the dashboard clean and maintainable.

How to Run the Dashboard (Codio)
1. Open the Codio box for Project Two
2. Ensure MongoDB is running
sudo service mongodb start
3. Navigate to the dashboard directory
cd ~/workspace
4. Open and run the Jupyter Notebook
jupyter notebook
5. Run all cells in ProjectTwoDashboard.ipynb
6. Copy the Codio URL
Codio format will be similar to:
https://<boxname>-8051.codio.io/

This will load the live Dash dashboard.

Screenshots & Documentation

All required screenshots for the assignment are included inside:
Project Two Morgun.docx

This Word document contains:

Dashboard screenshots for each filter

Pie chart screenshots

Map screenshots

Filter interactions

Verification of database connection

Full written documentation

Portfolio Reflection
1. Writing Maintainable, Readable, and Adaptable Code

Maintainable programs rely on structure, clarity, and modularity. Creating a separate CRUD Python module allowed me to reuse database operations throughout the dashboard without duplicating code. 
This separation made the project cleaner, easier to debug, and more adaptable if the database structure ever changes. I can reuse this module for any future MongoDB projects.

2. My Approach to Solving Problems as a Computer Scientist

I approached this project by breaking requirements into smaller, manageable components: the CRUD module, database queries, dashboard layout, interactions, and visualization. 
Compared to earlier courses, this project required a full end-to-end system with code integration and iterative testing. Moving forward, I will continue using modular design, incremental development, and thorough testing to meet real-world client requirements.

3. What Computer Scientists Do and Why It Matters

Computer scientists design tools that help organizations operate more efficiently. This project demonstrates how software can transform raw data into actionable insights. 
For Grazioso Salvare, the dashboard makes it easier to identify animals suited for rescue training—improving accuracy, speed, and decision-making. Projects like this show how data and software can directly support business goals.

