import models

def course_data(data):
    models.add_course(data)


def student_data(data):
    models.add_student(data)

def course_student_mapping(data):
    records = models.add_course_student_mapping(data)
    return records

def get_all_courses():
    records = models.all_courses()
    return records

def get_all_course_timings():
    records = models.all_course_timings()
    return records

def get_all_students():
    records = models.all_students()
    return records

def get_all_students_mapping():
    records = models.all_students_mapping()
    return records
# {"courseId":"cs245", "courseName": "dbms", "lectureCredits":3, "TutorialCredits": 0, "practicalCredits": 0, "totalCredits": 6, "prefessorName": "saradhi"}
# {"courseId":"cs245", "courseName": "dbms", "lectureCredits":3, "TutorialCredits": 0, "practicalCredits": 0, "totalCredits": 6, "professorName": "saradhi", "timings": [{"dayOfWeek":"Monday", "time":"9 am to 10 am"}, {"dayOfWeek":"Tuesday", "time":"10 am to 11 am"}, {"dayOfWeek":"Wednesday", "time":"10 am to 11 am"}]
# }
# {"rollNumber":200101047, "studentName":"manideep", "dept":"B.Tech", "branch":"CSE"}
# {"courseId":"cs245", "courseName": "dbms", "lectureCredits":3, "TutorialCredits": 0, "practicalCredits": 0, "totalCredits": 6, "professorName": "saradhi", "timings": [{"dayOfWeek":"Monday", "time":"9 am to 10 am"}, {"dayOfWeek":"Tuesday", "time":"10 am to 11 am"}, {"dayOfWeek":"Wednesday", "time":"10 am to 11 am"}]
# }
# {"rollNumber": 200101051, "courseId":"cs245"}