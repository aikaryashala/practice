# Quick Start Guide

## 30-Second Setup

```bash
# 1. Install Flask
pip install -r requirements.txt

# 2. Run the server
python app.py
```

Server starts at: `http://localhost:5000`

## Quick Test

### Option 1: Use Browser
Open `http://localhost:5000` and click "Load All Students"

### Option 2: Use cURL
```bash
curl http://localhost:5000/api/students
```

### Option 3: Run Test Script
```bash
./test_api.sh
```

## What You'll See

### In Terminal (Backend Debug Output):
```
==================================================
Starting Flask server...
Server will run on http://localhost:5000
Access from network: http://<your-ip>:5000
==================================================
Initializing database...
Inserted 8 students
Database initialization complete!

Route: GET /api/students
Query parameter 'grade': None
Getting all students (no filter)
Found 8 students
Returning JSON: [{'id': 1, 'name': 'Rama Kumar', ...}, ...]
```

### In Browser Console (Frontend Debug Output):
```
app.js loaded successfully
=== loadStudents() called ===
Fetching from URL: /api/students
Response received: Response {status: 200, ok: true}
JSON data received: (8) [{…}, {…}, ...]
Number of students: 8
```

## The 5 Routes at a Glance

| Route | Method | Purpose | Example |
|-------|--------|---------|---------|
| `/` | GET | Home page | Open in browser |
| `/api/students` | GET | Get students (filter with ?grade=A) | `curl http://localhost:5000/api/students` |
| `/api/students` | POST | Add student | `curl -X POST -H "Content-Type: application/json" -d '{"name":"..."}' ...` |
| `/api/students/1` | GET | Get student by ID | `curl http://localhost:5000/api/students/1` |
| `/view/students` | GET | HTML table view | Open in browser |

## Debugging Tips

### Backend (Python)
- Watch terminal for all print() statements
- Every API call logs: route, parameters, query results

### Frontend (JavaScript)
- Open browser DevTools (F12)
- Check Console tab for all console.log() statements
- Check Network tab for API requests/responses

### Database
```bash
sqlite3 students.db "SELECT * FROM students;"
```

## Next Steps

Read the full [README.md](README.md) for:
- Detailed debugging guide
- More cURL examples
- Remote server setup
- Learning exercises
