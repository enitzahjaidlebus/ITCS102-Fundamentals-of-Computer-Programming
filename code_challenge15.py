import os 
import json
os.system('cls')
print("Student Information System")
print("=============================")

student_record = {}#Empty Dictionary
while True:
    print("A - Add Student Record\nB - Print All student Record\nC - Search Student Record\nD - Delete Student Record\nE - Edit Student Record\nF - Export Student Record\nG - Import Student Record\nX - Exit System")
    choice = input("Select From the action above -->").lower()
    if choice == 'a' :
        os.system('cls')
        print("\nAdding new student record")

        id_no = input("Please Input Student ID number:")
        first_name = input("Please input first name:").upper()
        last_name = input('Please input last name:').upper()
        age = eval(input('Please input age:'))
        section = input('Please input section:').upper()
        course = input('Please input course:').upper()
        student_record[id_no] = [first_name, last_name, age, course, section]
        print('Data Saved Successfully')
        continue 
    elif choice == 'b':
        os.system('cls')
        print('Printing Student Record')
        
        for x, i in student_record.items():#key - values 
            print(f'student - {x}, Information - {i}')
        continue
    elif choice == 'c':
        os.system('cls')
        print('Search Student Record')
        search_id = input('Input Student Id Number to Search: ').upper()
        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print('++++++++++++++++++++++++++++++++')
                print(f'Record Found for ID {search_id}')
                for x in student_record[search_id]:
                    print(f'--- {x}')
                print('++++++++++++++++++++++++++++++++')
            else:
                print('Record Not Found')
            break   
        continue
    elif choice == 'd':
        os.system('cls')
        print('Delete Student Record')
        delete_id = input('Input Student Id Number to be Delete: ').upper()
        for each_id in student_record.keys():
            if delete_id in student_record.keys():
                print('++++++++++++++++++++++++')
                print(f'Record Found for ID {delete_id}')
                for x in student_record[delete_id]:
                    print(f'--- {x}')
                print('++++++++++++++++++++++++')

                student_record.pop(delete_id)
                print('\nRecord Deleted')
            else:
                print('Record Not Found')
            break   
        continue
    elif choice == 'e':
        print('Edit Student Record')
        edit_it = input('Input Student Id Number to Edit: ').upper()
        for each_id in student_record.keys():
            if edit_it in student_record.keys():
                print('++++++++++++++++++++++++++++++++')
                print(f'Record Found for ID {edit_it}')
                for x in student_record[edit_it]:
                    print(f'--- {x}')
                print('++++++++++++++++++++++++++++++++')
                
                first_name = input("Please input first name:").upper()
                last_name = input('Please input last name:').upper()
                age = eval(input('Please input age:'))
                section = input('Please input section:').upper()
                course = input('Please input course:').upper()

                student_record[edit_it][0] = first_name
                student_record[edit_it][1] = last_name
                student_record[edit_it][2] = age
                student_record[edit_it][3] = section
                student_record[edit_it][4] = course

                print('\nRecord Edited')
            else:
                print('Record Not Found')
            break   
        continue
    elif choice == 'f':
        os.system('cls')
        print('Export Student Data')
        #json Javascript Object Notation
                #w - write
        with open ('student_record','w') as new_file:
            json.dump(student_record,new_file, indent=4)
        
        print('\nExport Sucessfull')
        continue
    elif choice == 'g':
        os.system('cls')
        print('Import Student Data')
        #json Javascript Object Notation
                #r - Rite
        with open ('student_record','r') as new_file:
            import_student = json.load(new_file)

        student_record = import_student
        print('\nImport Sucessfull')
        continue
    elif choice == 'x':
        print("Exit System")
        break
    else:
        print('Invalid Input')
        continue