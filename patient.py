# Patient Module
# This file handles patient registration and patient records


def register_patient(patients_db):
    print("\n===== PATIENT REGISTRATION =====")

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    contact = input("Enter Contact Number: ")
    blood_group = input("Enter Blood Group: ")

    patients_db[patient_id] = {
        "name": name,
        "gender": gender,
        "age": age,
        "contact": contact,
        "blood_group": blood_group
    }

    print("\nPatient registered successfully!")


def view_patient(patients_db):
    print("\n===== VIEW PATIENT RECORD =====")

    patient_id = input("Enter Patient ID: ")

    if patient_id in patients_db:
        patient = patients_db[patient_id]

        print("\nPatient ID   :", patient_id)
        print("Name         :", patient["name"])
        print("Gender       :", patient["gender"])
        print("Age          :", patient["age"])
        print("Contact No.  :", patient["contact"])
        print("Blood Group  :", patient["blood_group"])

    else:
        print("\nPatient not found!")
