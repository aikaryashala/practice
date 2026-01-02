from flask import Flask, render_template, request, jsonify
import sqlite3
from database import init_db

app = Flask(__name__)

# Initialize database on startup
init_db()

def get_db_connection():
    """Helper function to get database connection"""
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row  # Returns rows as dictionaries
    return conn

# Route 1: Home page (HTML)
@app.route('/')
def home():
    print("Route: GET / - Serving home page")
    return render_template('index.html')

# Route 2: Get all students with optional grade filter (JSON)
@app.route('/api/students', methods=['GET'])
def get_students():
    print("\nRoute: GET /api/students")

    # Get query parameter
    grade_filter = request.args.get('grade')
    print(f"Query parameter 'grade': {grade_filter}")

    conn = get_db_connection()

    if grade_filter:
        print(f"Filtering students by grade: {grade_filter}")
        students = conn.execute(
            'SELECT * FROM students WHERE grade = ?',
            (grade_filter,)
        ).fetchall()
    else:
        print("Getting all students (no filter)")
        students = conn.execute('SELECT * FROM students').fetchall()

    conn.close()

    # Convert to list of dictionaries
    students_list = [dict(student) for student in students]
    print(f"Found {len(students_list)} students")
    print(f"Returning JSON: {students_list}")

    return jsonify(students_list)

# Route 3: Add new student (JSON body)
@app.route('/api/students', methods=['POST'])
def add_student():
    print("\nRoute: POST /api/students")

    # Get JSON data from request body
    data = request.get_json()
    print(f"Received JSON data: {data}")

    # Validate required fields
    required_fields = ['name', 'age', 'grade', 'email']
    for field in required_fields:
        if field not in data:
            error_msg = f"Missing required field: {field}"
            print(f"ERROR: {error_msg}")
            return jsonify({'error': error_msg}), 400

    # Insert into database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)',
        (data['name'], data['age'], data['grade'], data['email'])
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    print(f"Successfully created student with ID: {student_id}")

    return jsonify({
        'message': 'Student added successfully',
        'id': student_id
    }), 201

# Route 4: Get student by ID (JSON)
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    print(f"\nRoute: GET /api/students/{student_id}")

    conn = get_db_connection()
    student = conn.execute(
        'SELECT * FROM students WHERE id = ?',
        (student_id,)
    ).fetchone()
    conn.close()

    if student is None:
        print(f"ERROR: Student with ID {student_id} not found")
        return jsonify({'error': 'Student not found'}), 404

    student_dict = dict(student)
    print(f"Found student: {student_dict}")

    return jsonify(student_dict)

# Route 5: View students page (HTML with server-side rendering)
@app.route('/view/students')
def view_students():
    print("\nRoute: GET /view/students - Rendering HTML table")

    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    print(f"Rendering {len(students)} students in HTML")

    return render_template('students.html', students=students)

if __name__ == '__main__':
    print("=" * 50)
    print("Starting Flask server...")
    print("Server will run on http://localhost:5000")
    print("Access from network: http://<your-ip>:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
