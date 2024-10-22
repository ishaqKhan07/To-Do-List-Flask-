# Personal Assessment To-Do List Web Application

This is a simple web application built with Flask that allows users to manage their personal assessments. Users can add, edit, view, and mark assessments as complete. The application uses SQLite as the database for storing assessment data.

## Features

- Add new assessments with title, module code, deadline, description, and completion status.
- View all assessments (both completed and uncompleted).
- Edit existing assessments.
- View details of individual assessments.
- Mark assessments as complete.
- Filter assessments to view only uncompleted or completed ones.

## Technologies Used

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- SQLite

## Installation

###Create a virtual environment:

    python -m venv .venv

###Activate the virtual environment:
    
    .venv\Scripts\activate  

###Install the required packages:
    
    pip install -r requirements.txt

###Run the application:

    python run.py
