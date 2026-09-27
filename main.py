# Hospital EHR System

from patient import register_patient, view_patient
from doctor import doctor_section
from chemist import chemist_section

# Patients record database
patients_db = {}

# Show menu
while True:
    print("\n================================")
    print("       HOSPITAL EHR SYSTEM")
    print("================================")
    print("1. Register New Patient")
    print("2. Doctor Section")
    print("3. Chemist Section")
    print("4. View Patient Record")
    print("5. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        register_patient(patients_db)

    elif user_choice == "2":
        doctor_section(patients_db)

    elif user_choice == "3":
        chemist_section(patients_db)

    elif user_choice == "4":
        view_patient(patients_db)

    elif user_choice == "5":
        print("Thank you for using Hospital EHR System!")
        break

    else:
        print("Invalid choice. Please try again.")
