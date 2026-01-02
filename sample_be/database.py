import sqlite3

def init_db():
    """Initialize database and insert sample data"""
    print("Initializing database...")

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM students')
    count = cursor.fetchone()[0]

    if count == 0:
        print("Inserting sample data...")
        # Insert sample data with Indian names
        students = [
            ('Rama Kumar', 20, 'A', 'rama@example.com'),
            ('Sita Sharma', 22, 'A', 'sita@example.com'),
            ('Bharat Singh', 21, 'B', 'bharat@example.com'),
            ('Lakshman Reddy', 19, 'A', 'lakshman@example.com'),
            ('Hanuman Patel', 23, 'C', 'hanuman@example.com'),
            ('Arjun Gupta', 20, 'B', 'arjun@example.com'),
            ('Draupadi Iyer', 21, 'A', 'draupadi@example.com'),
            ('Krishna Rao', 22, 'B', 'krishna@example.com'),
        ]

        cursor.executemany(
            'INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)',
            students
        )
        print(f"Inserted {len(students)} students")
    else:
        print(f"Database already has {count} students")

    conn.commit()
    conn.close()
    print("Database initialization complete!")

if __name__ == '__main__':
    init_db()
