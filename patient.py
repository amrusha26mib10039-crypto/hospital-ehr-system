# Patient Module
# This module is used to register patients and display their records

def register_patient(patients_db):
    print("\n==== PATIENT REGISTRATION ====")

    patient_id = input("Patient ID : ")
    name = input("Name : ")
    gender = input("Gender : ")
    age = int(input("Age : "))
    contact = input("Contact number : ")
    blood_group = input("Blood group : ")

    patients_db[patient_id] = {
        "name" : name,
        "gender" : gender,
        "age" : age,
        "contact" : contact,
        "blood_group" : blood_group
    }

    print("\nPatient registered successfully!")
    

def view_patient(patients_db):
    print("\n==== VIEW PATIENT RECORD ====")

    patient_id = input("Patient ID : ")

    if patient_id in patients_db:

        patient = patients_db[patient_id]
        
        print("\nPatient ID   :", patient_id)
        print("Name         :", patient["name"])
        print("Gender       :", patient["gender"])
        print("Age          :", patient["age"])
        print("Contact No.  :", patient["contact"])
        print("Blood Group  :", patient["blood_group"])
        print("Diagnosis    :", patient["diagnosis"])
        print("Medicines prescribed  :", patient["medicines"])

    else:
        print("\nPatient not found!")
