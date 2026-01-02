// Load all students from API
function loadStudents() {
    console.log('=== loadStudents() called ===');

    const url = '/api/students';
    console.log('Fetching from URL:', url);

    fetch(url)
        .then(response => {
            console.log('Response received:', response);
            console.log('Response status:', response.status);
            console.log('Response OK:', response.ok);
            return response.json();
        })
        .then(data => {
            console.log('JSON data received:', data);
            console.log('Number of students:', data.length);
            displayStudents(data);
        })
        .catch(error => {
            console.error('ERROR in fetch:', error);
            showMessage('Error loading students: ' + error.message, 'error');
        });
}

// Load students filtered by grade A
function loadStudentsByGrade() {
    console.log('=== loadStudentsByGrade() called ===');

    const grade = 'A';
    const url = '/api/students?grade=' + grade;
    console.log('Fetching from URL:', url);
    console.log('Query parameter grade:', grade);

    fetch(url)
        .then(response => {
            console.log('Response received:', response);
            return response.json();
        })
        .then(data => {
            console.log('Filtered JSON data:', data);
            console.log('Number of Grade A students:', data.length);
            displayStudents(data);
        })
        .catch(error => {
            console.error('ERROR in fetch:', error);
            showMessage('Error loading students: ' + error.message, 'error');
        });
}

// Display students in table
function displayStudents(students) {
    console.log('=== displayStudents() called ===');
    console.log('Students to display:', students);

    const tableBody = document.getElementById('tableBody');
    console.log('Table body element:', tableBody);

    // Clear existing rows
    tableBody.innerHTML = '';
    console.log('Cleared existing table rows');

    // Add new rows
    students.forEach((student, index) => {
        console.log(`Adding row ${index + 1}:`, student);

        const row = document.createElement('tr');
        row.innerHTML = '<td>' + student.id + '</td>' +
                       '<td>' + student.name + '</td>' +
                       '<td>' + student.age + '</td>' +
                       '<td>' + student.grade + '</td>' +
                       '<td>' + student.email + '</td>';
        tableBody.appendChild(row);
    });

    console.log('Table populated with', students.length, 'rows');
    showMessage('Loaded ' + students.length + ' students', 'success');
}

// Add new student
function addStudent() {
    console.log('=== addStudent() called ===');

    // Get form values
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const grade = document.getElementById('grade').value;
    const email = document.getElementById('email').value;

    console.log('Form values:');
    console.log('  name:', name);
    console.log('  age:', age);
    console.log('  grade:', grade);
    console.log('  email:', email);

    // Validate
    if (!name || !age || !grade || !email) {
        console.error('Validation failed: missing fields');
        showAddMessage('Please fill all fields', 'error');
        return;
    }

    // Create request body
    const studentData = {
        name: name,
        age: parseInt(age),
        grade: grade,
        email: email
    };
    console.log('Request body (JSON):', studentData);

    // Send POST request
    const url = '/api/students';
    console.log('POSTing to URL:', url);

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
    .then(response => {
        console.log('POST response:', response);
        console.log('Response status:', response.status);
        return response.json();
    })
    .then(data => {
        console.log('Response JSON:', data);
        showAddMessage('Student added! ID: ' + data.id, 'success');

        // Clear form
        document.getElementById('name').value = '';
        document.getElementById('age').value = '';
        document.getElementById('grade').value = '';
        document.getElementById('email').value = '';
        console.log('Form cleared');

        // Reload table
        console.log('Reloading students table...');
        loadStudents();
    })
    .catch(error => {
        console.error('ERROR in POST request:', error);
        showAddMessage('Error adding student: ' + error.message, 'error');
    });
}

// Helper function to show messages
function showMessage(msg, type) {
    console.log('showMessage:', msg, 'type:', type);
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = msg;
    messageDiv.className = type;
}

function showAddMessage(msg, type) {
    console.log('showAddMessage:', msg, 'type:', type);
    const messageDiv = document.getElementById('addMessage');
    messageDiv.textContent = msg;
    messageDiv.className = type;
}

console.log('app.js loaded successfully');
