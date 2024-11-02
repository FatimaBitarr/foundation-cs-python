import json

class Course:
    def __init__(self,code,name,credit_hours,course_type):
        self.code=code
        self.name=name
        self.credit_hours=credit_hours
        self.course_type=course_type

    def get_info(self):
        return (f"Course Code: {self.code}, Name: {self.name}, " f"Credit Hours: {self.credit_hours}, Type: {self.course_type}")

class Catalogue:   
    def __init__(self):
        self.courses= {}

    def add_course(self,course):
        self.courses[course.code]=course

class Student:
    def __init__(self,id,student_name,enrolled_courses):
        self.id=id
        self.student_name=student_name
        self.enrolled_courses= {}

    def enroll(self,course):
        if course.code in self.enrolled_courses:
            raise Exception("You are already enrolled in this course")
        
        self.enrolled_courses[course.code]=course

    def drop(self,course_code):
        if course_code not in self.enrolled_courses:
            raise Exception("Cannot drop, you are not enrolled in this course")
        del self.enrolled_courses[course_code]
        print("Dropped course succesfully")

    def list_courses(self):
        return [course.get_info() for course in self.enrolled_courses.values()]
    
    def save_to_file(self, filename):
        catalog_data = {code: {
            "name": course.name,
            "credit_hours": course.credit_hours,
            "course_type": course.course_type
        } for code, course in self.courses.items()}

        with open(filename, 'w') as file:
            json.dump(catalog_data, file, indent=4)

        print(f"Catalog saved to {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                course_data = json.load(file)
                self.courses = [Course(**data) for data in course_data]
            print(f"Catalog loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} does not exist.")
        except json.JSONDecodeError:
            print("Error: The file is not in the correct JSON format.")

        user_input = input("Type 'exit' to exit the program: ")
    
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            exit()