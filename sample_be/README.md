# Simple Python Backend Server - Student Management System

A beginner-friendly Flask application for learning backend concepts.

## Setup and Run

### 1. Install Flask
```bash
pip install flask
```

### 2. Run the Application
```bash
cd sample_be
python app.py
```

The server will start at `http://localhost:5000`

### 3. Running in Ubuntu VM (Recommended for Students)

This setup allows you to run the backend in an Ubuntu VM and access it from your host machine's browser.

#### Step 1: Setup Ubuntu VM
```bash
# In your Ubuntu VM terminal

# Update system
sudo apt update

# Install Python and pip (if not installed)
sudo apt install python3 python3-pip -y

# Install Flask
pip3 install flask

# Navigate to the project
cd /path/to/sample_be

# Run the server (binds to all interfaces)
python3 app.py
```

The server is already configured to bind to `0.0.0.0`, so it will be accessible from your host machine.

#### Step 2: Find Your VM's IP Address
```bash
# In Ubuntu VM
ip addr show
# Or
hostname -I
```

Look for an IP like `192.168.x.x` or `10.0.x.x`

#### Step 3: Access from Host Machine

**From your host machine's browser:**
```
http://VM_IP_ADDRESS:5000
```
Example: `http://192.168.56.101:5000`

**Test from host machine terminal:**
```bash
curl http://VM_IP_ADDRESS:5000/api/students
```

#### Step 4: Debugging in VM

**Terminal 1: Run server with visible logs**
```bash
cd sample_be
python3 app.py
```

**Terminal 2: Test from within VM**
```bash
# Test locally
curl http://localhost:5000/api/students

# Run test script
./test_api.sh
```

**Terminal 3: Monitor logs**
```bash
# If running in background
tail -f app.log
```

#### Common VM Issues

**Issue 1: Cannot access from host machine**
```bash
# Check if VM network is in bridged or NAT mode
# NAT with port forwarding works best

# Test if server is running
curl http://localhost:5000/api/students

# Check firewall
sudo ufw status
sudo ufw allow 5000
```

**Issue 2: Different Python version**
```bash
# Use python3 explicitly
python3 app.py

# Or create alias
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc
```

**Issue 3: Permission denied on test script**
```bash
chmod +x test_api.sh
./test_api.sh
```

#### VM Network Configuration Options

**Option A: NAT with Port Forwarding (Easiest)**
- In VirtualBox/VMware: Settings → Network → Advanced → Port Forwarding
- Host Port: 5000 → Guest Port: 5000
- Access from host: `http://localhost:5000`

**Option B: Bridged Network**
- VM gets its own IP on your network
- Access from host: `http://VM_IP:5000`

**Option C: Host-Only Network**
- VM accessible only from host machine
- Access from host: `http://192.168.56.101:5000` (example)

### 4. Run on Remote Ubuntu Server
```bash
# For deployment on remote server
python3 app.py

# The app is already configured with host='0.0.0.0'
```

## File Structure
```
sample_be/
├── app.py              # Main Flask application (5 routes)
├── database.py         # Database initialization
├── students.db         # SQLite database (auto-created)
├── static/
│   └── app.js         # Frontend JavaScript
└── templates/
    ├── index.html     # Home page
    └── students.html  # Server-rendered students page
```

## The 5 Routes

### 1. GET `/` - Home Page (HTML)
- Open: `http://localhost:5000/`
- Interactive page with buttons and forms

### 2. GET `/api/students` - Get Students (JSON)
- Get all: `http://localhost:5000/api/students`
- Filter by grade: `http://localhost:5000/api/students?grade=A`

### 3. POST `/api/students` - Add Student (JSON)
- Use the form on home page, OR
- Command line:
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Radha Krishnan","age":21,"grade":"A","email":"radha@example.com"}'
```

### 4. GET `/api/students/<id>` - Get Student by ID (JSON)
- Example: `http://localhost:5000/api/students/1`

### 5. GET `/view/students` - Server-Rendered HTML
- Open: `http://localhost:5000/view/students`
- Shows students in HTML table (server-side rendering)

## Testing with cURL Commands

### Test 1: Get All Students (JSON)
```bash
curl http://localhost:5000/api/students
```
**Expected**: JSON array with all 8 students

### Test 2: Filter by Grade (Query Parameter)
```bash
curl "http://localhost:5000/api/students?grade=A"
```
**Expected**: JSON array with only grade A students
**Note**: Use quotes around URL with query parameters

### Test 3: Get Student by ID
```bash
curl http://localhost:5000/api/students/1
```
**Expected**: JSON object for student with ID 1

```bash
curl http://localhost:5000/api/students/999
```
**Expected**: 404 error, student not found

### Test 4: Add New Student (POST with JSON)
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Radha Sharma","age":20,"grade":"A","email":"radha@example.com"}'
```
**Expected**: `{"message": "Student added successfully", "id": 9}`

### Test 5: Invalid POST (Missing Fields)
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Incomplete"}'
```
**Expected**: 400 error with message about missing fields

### Test 6: Get HTML Page
```bash
curl http://localhost:5000/ | head -20
```
**Expected**: HTML content (first 20 lines)

```bash
curl http://localhost:5000/view/students | grep "<tr>"
```
**Expected**: HTML table rows

### Test 7: Different Filters
```bash
# Grade B students
curl "http://localhost:5000/api/students?grade=B"

# Grade C students
curl "http://localhost:5000/api/students?grade=C"
```

### Test 8: Pretty Print JSON (with jq)
```bash
# Install jq first: sudo apt install jq
curl http://localhost:5000/api/students | jq

# Get only names
curl http://localhost:5000/api/students | jq '.[].name'

# Count students
curl http://localhost:5000/api/students | jq 'length'

# Filter grade A using jq
curl http://localhost:5000/api/students | jq '.[] | select(.grade=="A")'
```

## Debugging on Remote Ubuntu Machine (Shell-Only)

### Backend Debugging (Python)

The Flask app runs in **debug mode** with extensive print statements:

1. **Watch Terminal Output**: All requests are logged
```
Route: GET /api/students
Query parameter 'grade': A
Filtering students by grade: A
Found 4 students
Returning JSON: [...]
```

2. **Run in Foreground** (see all output):
```bash
python app.py
```

3. **Run in Background** and tail logs:
```bash
# Redirect output to log file
python app.py > app.log 2>&1 &

# Watch logs in real-time
tail -f app.log
```

4. **Filter Logs**:
```bash
# See only route access
tail -f app.log | grep "Route:"

# See only errors
tail -f app.log | grep "ERROR"

# See specific route
tail -f app.log | grep "/api/students"
```

5. **Debug Database**:
```bash
# Install sqlite3
sudo apt install sqlite3

# Open database
sqlite3 students.db

# Run queries
sqlite> SELECT * FROM students;
sqlite> SELECT * FROM students WHERE grade='A';
sqlite> SELECT COUNT(*) FROM students;
sqlite> .schema students
sqlite> .quit
```

6. **Add Your Own Debug Prints**:
```python
print("DEBUG: My variable =", my_variable)
```

### Frontend Debugging (No Browser)

When running on remote server without browser:

1. **Test with cURL** (see above commands)

2. **Test JavaScript Load**:
```bash
# Check if JS file is accessible
curl http://localhost:5000/static/app.js | head -20
```

3. **Simulate JavaScript Fetch**:
```bash
# Same as JavaScript fetch()
curl http://localhost:5000/api/students

# Same as JavaScript POST
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","age":20,"grade":"A","email":"test@example.com"}'
```

4. **Check Response Headers**:
```bash
curl -i http://localhost:5000/api/students
```
Shows HTTP status code, content-type, etc.

5. **Verbose Mode**:
```bash
curl -v http://localhost:5000/api/students
```
Shows complete request and response details

### Network Debugging

1. **Check if Server is Running**:
```bash
# Check port 5000
netstat -tuln | grep 5000

# Or
lsof -i :5000
```

2. **Test from Local Machine**:
```bash
curl http://localhost:5000/api/students
```

3. **Test from Remote Machine** (replace IP):
```bash
curl http://YOUR_SERVER_IP:5000/api/students
```

4. **Check Firewall**:
```bash
# Ubuntu firewall status
sudo ufw status

# Allow port 5000 if needed
sudo ufw allow 5000
```

### Complete Debug Session Example

```bash
# Terminal 1: Run server with logs
cd sample_be
python app.py 2>&1 | tee app.log

# Terminal 2: Test API and watch responses
curl http://localhost:5000/api/students | jq

# Terminal 3: Watch logs
tail -f app.log | grep "Route:"

# Terminal 4: Check database
sqlite3 students.db "SELECT * FROM students;"
```

## Common Issues

### Port 5000 Already in Use
```bash
# Find process
lsof -i :5000

# Kill process
lsof -ti:5000 | xargs kill -9

# Or use different port
# In app.py change: app.run(debug=True, port=5001)
```

### Database Issues
```bash
# Delete and recreate
rm students.db
python database.py
```

### Flask Not Installed
```bash
pip install flask
```

### Cannot Connect from Outside
```bash
# Make sure server binds to 0.0.0.0
# In app.py last line:
# app.run(debug=True, host='0.0.0.0', port=5000)
```

### Permission Denied
```bash
# Use port above 1024, or run with sudo (not recommended)
# Better: use port 5000 or 8000
```

## Learning Exercises

1. **Add a new route** to delete a student by ID
2. **Add a filter** for age in addition to grade
3. **Add validation** to reject students under 18
4. **Add error handling** for duplicate emails
5. **Add a search feature** to find students by name
6. **Add logging** to a file for all API calls
7. **Add timestamp** to each student record

## Key Concepts Demonstrated

- **Query Parameters**: `?grade=A` in URL
- **JSON Request/Response**: POST with JSON body, GET returns JSON
- **Path Parameters**: `/api/students/<id>` dynamic routing
- **HTML Rendering**: Server-side vs client-side rendering
- **Database Operations**: SQLite with Python
- **Fetch API**: JavaScript making HTTP requests
- **DOM Manipulation**: JavaScript updating HTML dynamically
- **Debugging**: Console logs and print statements
- **Shell Testing**: cURL for API testing without browser
