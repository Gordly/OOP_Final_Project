#frankenstein code

class Doctor:

    def __init__(self, id, name, specialization, schedule, qualification, room):

        self.id = id
        self.name = name
        self.specialization = specialization
        self.schedule = schedule
        self.qualification = qualification
        self.room = room


    def format_data_print():

        with open('doctors.txt') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip().split('_')
                print(line[0] + '    ' + line[1] + '    ' + line[2] + '    ' + line[3] + '    ' + line[4] + '    ' + line[5])


    def check_id():
        id = (input("Enter the doctor ID:\n"))

        with open('doctors.txt') as f:
            lines = f.readlines()

            line_number_total = 0
            for line in lines:
                line = line.strip().split("_")
                line_number_total += 1
                line_number_check = 0

                for line[0] in line:
                    
                    while line_number_check != line_number_total:
                        try:
                            if line[0] == id:
                                print('\n'+line[0]+'\t'+line[1]+'\t'+line[2]+'\t\t'+line[3]+'\t'+line[4]+'\t\t'+line[5])
                                return

                            elif line[0] != id:
                                line_number_check += 1

                        except:
                            continue

            if line_number_check == line_number_total:
                print("Can't find the doctor with the same ID on the system")


    def check_name():
        name = (input("Enter the doctor name:\n"))

        with open('doctors.txt') as f:
            lines = f.readlines()

            line_number_total = 0
            for line in lines:
                line = line.strip().split("_")
                line_number_total += 1
                line_number_check = 0

                for line[0] in line:
                    
                    while line_number_check != line_number_total:
                        try:
                            if line[1] == name:
                                print('\n'+line[0]+'\t'+line[1]+'\t'+line[2]+'\t\t'+line[3]+'\t'+line[4]+'\t\t'+line[5])
                                return

                            elif line[1] != name:
                                line_number_check += 1

                        except:
                            continue

            if line_number_check == line_number_total:
                print("Can't find the doctor with the same name on the system")


    def append_text_data(self):
        text_data = object.id + '_' + object.name + '_' + object.specialization + '_' + object.schedule + '_' + object.qualification + '_' + object.room
        with open('doctors.txt', 'a') as f:
            f.write('\n' + text_data)


    def edit_id():
        id = input("Please enter the id of the doctor that you want to edit their information:\n")

        with open('doctors.txt','r+') as f:
            lines = f.readlines()

            global line_number_total
            line_number_total = 0
            for line in lines:
                line = line.strip().split("_")
                line_number_total += 1
                line_number_check = 0
                

                for line[0] in line:
                    
                    while line_number_check != line_number_total:
                        try:
                            if line[0] == id:
                                line[1] = input('Enter new name:\n')
                                line[2] = input('Enter new specialization:\n')
                                line[3] = input('Enter new schedule:\n')
                                line[4] = input('Enter new qualification:\n')
                                line[5] = input('Enter new room number:\n')
                                global edited_text
                                edited_text = (line[0] + '_' + line[1] + '_' + line[2] + '_' + line[3] + '_' + line[4] + '_' + line[5])
                                return

                            elif line[0] != id:
                                line_number_check += 1

                        except:
                            continue
                
            if line_number_check == line_number_total:
                print("Can't find the Patient with the same id on the system")


    def menu():
        while True:
            try:
                option = int(input('\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\n'))
                
                if option == 1:
                    print('\n')
                    Doctor.format_data_print()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 2:
                    print('\n')
                    Doctor.check_id()
                    continue

                elif option == 3:
                    print('\n')
                    Doctor.check_name()
                    continue

                elif option == 4:
                    print('\n')
                    Doctor.append_text_data()
                    continue

                elif option == 5:
                    print('\n')
                    global object
                    object = Doctor(input("Enter the doctor's ID: \n"), input("Enter the doctor's name (Dr.name): \n"), input("Enter the doctor's specialty: \n"), input("Enter the doctor's schedule (e.g. 7AM-10PM): \n"), input("Enter the doctor's qualification: \n"), input("Enter the doctor's room number: \n"))
                    object.edit_id()
                    Doctor.format_data_print()
                    print('\nBack to the previous Menu')
                    continue

                elif option == 6:
                    #return to main menu of classes
                    break
            except:
                continue