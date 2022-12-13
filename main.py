from doctor import Doctor
from facilities import Facility
from laboratory import Laboratory
from patients import patients

def menu():

    while True:
        try:
            option = int(input('\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n\n'))
            
            if option == 1:
                print('\n')
                Doctor.menu()
                continue

            elif option == 2:
                print('\n')
                Facility.menu()
                continue

            elif option == 3:
                print('\n')
                Laboratory.menu()

            elif option == 4:
                print('\n')
                patients.menu()
        except:
            continue

menu()