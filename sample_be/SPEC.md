# Simple Python Backend Server - Specification

## Purpose
A beginner-friendly Python web application demonstrating basic backend concepts including routing, database operations, query parameters, JSON requests/responses, and HTML rendering.

## Tech Stack
- **Backend Framework**: Flask (lightweight and easy to understand)
- **Database**: SQLite3 (no setup required, file-based)
- **Frontend**: Vanilla HTML + JavaScript (no build tools needed)

## Database Schema

### Table: `students`
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    email TEXT NOT NULL
);
```

**Sample Data**: 5-10 student records for testing

## API Routes (5 total)

### 1. GET `/` - Home Page (HTML Response)
- **Type**: HTML page
- **Purpose**: Landing page with links to all endpoints and a table display area
- **Response**: HTML page with navigation and dynamic content area

### 2. GET `/api/students` - Get All Students (JSON Response)
- **Type**: JSON API
- **Method**: GET
- **Query Parameters**:
  - `grade` (optional) - Filter by grade (e.g., "A", "B", "C")
- **Response**: JSON array of student objects
- **Example**:
  - `/api/students` → All students
  - `/api/students?grade=A` → Only students with grade A

### 3. POST `/api/students` - Add New Student (JSON Request/Response)
- **Type**: JSON API
- **Method**: POST
- **Request Body** (JSON):
  ```json
  {
    "name": "Rama Kumar",
    "age": 20,
    "grade": "A",
    "email": "rama@example.com"
  }
  ```
- **Response**: Success message with created student ID

### 4. GET `/api/students/<id>` - Get Student by ID (JSON Response)
- **Type**: JSON API
- **Method**: GET
- **Path Parameter**: `id` - Student ID
- **Response**: Single student object or 404 if not found

### 5. GET `/view/students` - View Students Page (HTML Response)
- **Type**: HTML page
- **Purpose**: Display all students in an HTML table
- **Response**: Rendered HTML with student data in a table
- **Features**: Server-side rendering of student list

## Frontend Features

### HTML (`index.html`)
- Navigation menu with links to all endpoints
- Button to "Load Students into Table"
- Empty `<table>` element with id="studentsTable"
- Form to add new students

### JavaScript (`app.js`)
- Function to fetch `/api/students`
- Function to parse JSON and populate HTML table
- Function to handle form submission for adding students
- Basic error handling and loading states

## File Structure
```
sample_be/
├── SPEC.md                 # This specification
├── app.py                  # Main Flask application
├── database.py             # Database initialization and sample data
├── students.db             # SQLite database (auto-generated)
├── static/
│   └── app.js             # Frontend JavaScript
└── templates/
    ├── index.html         # Home page
    └── students.html      # Students view page
```

## Learning Objectives
Students will learn:
1. **Query Parameters**: How to pass and handle URL parameters (`/api/students?grade=A`)
2. **JSON Request/Response**: How to send/receive JSON data
3. **Path Parameters**: Dynamic routes with variables (`/api/students/<id>`)
4. **HTML Responses**: Server-side rendering vs API responses
5. **Database Operations**: Basic CRUD with SQLite
6. **Frontend-Backend Communication**: Fetch API and DOM manipulation
7. **HTTP Methods**: GET vs POST

## How to Run
```bash
cd sample_be
python app.py
# Server runs on http://localhost:5000
```

## Testing Examples

### Test Query Parameters
```bash
curl "http://localhost:5000/api/students?grade=A"
```

### Test JSON Body
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Sita Sharma","age":22,"grade":"B","email":"sita@example.com"}'
```

### Test HTML Response
- Open browser: `http://localhost:5000/`
- Open browser: `http://localhost:5000/view/students`

### Test JSON Response with Frontend
- Click "Load Students into Table" button on home page
- Watch JavaScript fetch data and populate table dynamically
