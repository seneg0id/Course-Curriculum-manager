import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def add_course(data):
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    courseId = data['courseId']
    courseName = data['courseName']
    lectureCredits = data['lectureCredits']
    TutorialCredits = data['TutorialCredits']
    practicalCredits = data['practicalCredits']
    totalCredits = data['totalCredits']
    professorName = data['professorName']
    cursor.execute("INSERT INTO courses (courseId, courseName, lectureCredits, TutorialCredits, practicalCredits, totalCredits, professorName) VALUES (?, ?, ?, ?, ?, ?, ?)", (courseId, courseName, lectureCredits, TutorialCredits, practicalCredits, totalCredits, professorName))
    for entry in data['timings']:
        dayOfWeek = entry['dayOfWeek']
        timings = entry['time']
        cursor.execute("INSERT INTO course_timings (courseId, dayOfWeek, timings) VALUES (?, ?, ?)", (courseId, dayOfWeek, timings))
    conn.commit()

def add_student(data):
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    rollNumber = data['rollNumber']
    studentName = data['studentName']
    dept = data['dept']
    branch = data['branch']
    cursor.execute("INSERT INTO students (rollNumber, studentName, dept, branch) values(?, ?, ?, ?)", (rollNumber, studentName, dept, branch))
    conn.commit()

def add_course_student_mapping(data):
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    rollNumber = data['rollNumber']
    courseId = data['courseId']
    cursor.execute("SELECT dayOfWeek, timings FROM course_timings WHERE courseId = ?", (courseId,))
    timings = dict(timingsOfCourses=[dict(r) for r in cursor.fetchall()])
    cursor.execute("SELECT courseId FROM course_student_mapping WHERE rollNumber = ?", (rollNumber,))
    courses_registered = dict(courses=[dict(r) for r in cursor.fetchall()])
    cursor.execute("SELECT rollNumber FROM students WHERE rollNumber = ?", (rollNumber,))
    student_registered = dict(students=[dict(r) for r in cursor.fetchall()])
    cursor.execute("SELECT courseId FROM courses WHERE courseId = ?", (courseId,))
    courses_present = dict(courses=[dict(r) for r in cursor.fetchall()])
    if student_registered['students'] and courses_present['courses']:
        existing_timings = []
        for c in courses_registered['courses']:
            cursor.execute("SELECT dayOfWeek, timings FROM course_timings WHERE courseId = ?", (c['courseId'],))
            existing_timings = existing_timings + [dict(r) for r in cursor.fetchall()]
        common = 0
        for value in existing_timings:
            if value in timings['timingsOfCourses']:
                cursor.execute("SELECT courseId FROM course_timings WHERE dayOfWeek = ? AND timings = ?", (value['dayOfWeek'], value['timings']))
                courses_with_same_time = dict(courses=[dict(r) for r in cursor.fetchall()])
                common = 1
        courses_conflicted = {}
        courses_conflicted['courses'] = []
        if (common):
            for val in courses_with_same_time['courses']:
                if val in courses_registered['courses']:
                    courses_conflicted['courses'] = courses_conflicted['courses'] + [val]
            courses_conflicted['courses'] = courses_conflicted['courses'] + [{"courseId": courseId}]
            return courses_conflicted
        else:
            cursor.execute("INSERT INTO course_student_mapping (rollNumber, courseId) VALUES(?, ?)", (rollNumber, courseId))
            conn.commit()
            return all_students_mapping()
    else:
        return "student or course doesnt exist"

def all_courses():
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    records = dict(result=[dict(r) for r in cursor.fetchall()])
    return records

def all_course_timings():
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course_timings")
    records_timings = dict(resultt=[dict(r) for r in cursor.fetchall()])
    return records_timings

def all_students():
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = dict(result=[dict(r) for r in cursor.fetchall()])
    return records

def all_students_mapping():
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course_student_mapping")
    records = dict(result=[dict(r) for r in cursor.fetchall()])
    return records
