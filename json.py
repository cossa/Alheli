import json

def load_data(filename):
    students = {}
    with open(filename, "r") as file:
        reader = json.load(file)
        
    for student_id, student_info in reader.items():
        student = student_info[0]
        name = student['name']
        grade = student['grade']
        group = student['group']
            
        students[student_id] = [name, grade, group]
    return students

def main():
    filename = "data.json" 
    
    student_data = load_data(filename)
    print(student_data)
    
    for student in student_data:
        print(f'Student ID: {student}')
        print(f'Name: {student_data [student][0]}')
        print(f'Grade: {student_data[student][1]}')
        print(f'Group: {student_data[student][2]}')
        print()   
        
main()
