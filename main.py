


class Menu:

    def main():
                     
        from facilities import Facility
        from doctor import Doctor
        from laboratory import Laboratory
        from patients import patients
        
    
        while (True):
                
            menu_choice = int((input("""Welcome to Alberta Hospital (AH) Managment system 
            Select from the following options, or select 0 to stop: 
            1 - 	Doctors
            2 - 	Facilities
            3 - 	Laboratories
            4 - 	Patients 
            """)))


            
            if (menu_choice == 0):
                break
            

            elif (menu_choice == 1):
                Doctor.menu()
                continue
                

            elif (menu_choice == 2):
                Facility.menu()
                continue 
                


            elif (menu_choice == 3):
                
                Laboratory.menu()
                continue
               
            
            elif (menu_choice == 4):
                patients.menu()
                continue
                

            break


Menu.main()
