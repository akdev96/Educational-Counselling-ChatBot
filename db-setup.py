# Database Setup (SQLite)
import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('education_counseling.db')
c = conn.cursor()

# Create table for courses
c.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    details TEXT,
    requirement TEXT,
    price TEXT,
    offering_university TEXT
)
''')

# Create table for user interactions
c.execute('''
CREATE TABLE IF NOT EXISTS user_interactions (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    user_input TEXT,
    bot_response TEXT
)
''')

# Insert sample data
c.execute("INSERT INTO courses (name, details, requirement, price, offering_university) VALUES ('Computer Science', 'B.Sc. in Computer Science', 'High School Diploma', '10000', 'University A')")
c.execute("INSERT INTO courses (name, details, requirement, price, offering_university) VALUES ('Business Administration', 'BBA in Business Administration', 'High School Diploma', '8000', 'University B')")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Function to fetch course information
def fetch_courses():
    # Connect to SQLite database
    conn = sqlite3.connect('education_counseling.db')
    c = conn.cursor()

    # Fetch all courses
    c.execute("SELECT name, details, requirement, price, offering_university FROM courses")
    courses = c.fetchall()

    # Close the connection
    conn.close()

    # Format the result for display
    if courses:
        response = "Here are the courses we offer:\n"
        for course in courses:
            response += f"\nName: {course[0]}\nDetails: {course[1]}\nRequirement: {course[2]}\nPrice: {course[3]}\nOffering University: {course[4]}\n"
        return response
    else:
        return "No courses available."

# Function to log user interactions
def log_interaction(user_input, bot_response):
    # Connect to SQLite database
    conn = sqlite3.connect('education_counseling.db')
    c = conn.cursor()

    # Insert the interaction log
    c.execute('''
    INSERT INTO user_interactions (timestamp, user_input, bot_response) 
    VALUES (?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), user_input, bot_response))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    # Example user input and fetching courses
    user_input = "What courses do you offer?"
    bot_response = fetch_courses()
    print(bot_response)

    # Log the interaction
    log_interaction(user_input, bot_response)
