# Doctor Module

def doctor_section(patients_db):

    print("\n===== DOCTOR SECTION =====")

    patient_id = input("Enter Patient ID: ")

    if patient_id in patients_db:

        patient = patients_db[patient_id]

        print("\nPatient Details")
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Blood Group:", patient["blood_group"])

        diagnosis = input("Enter Diagnosis: ")
        allergy = input("Enter Allergic History: ")

        medicines = []

        n = int(input("How many medicines? "))

        for i in range(n):
            medicine = input(f"Enter Medicine {i+1}: ")
            medicines.append(medicine)

        patient["diagnosis"] = diagnosis
        patient["allergy"] = allergy
        patient["medicines"] = medicines

        print("\nDoctor details saved successfully!")

    else:
        print("\nPatient not found!")
