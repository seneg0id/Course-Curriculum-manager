from flask import Blueprint, request
import services

course = Blueprint("course", __name__)

@course.route('/addcourses', methods=['POST'])
def process_course_json():
    data = request.get_json()
    services.course_data(data)
    return {"courses":services.get_all_courses(),
    "course_timings":services.get_all_course_timings()}

@course.route('/addstudents', methods=['POST'])
def process_student_json():
    data = request.get_json()
    services.student_data(data)
    return services.get_all_students()

@course.route('/addmapping', methods=['POST'])
def process_mapping_json():
    data = request.get_json()
    return services.course_student_mapping(data)