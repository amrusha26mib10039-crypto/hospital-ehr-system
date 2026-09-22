# Chemist Module

def chemist_section(patients_db):

    print("\n===== CHEMIST SECTION =====")

    patient_id = input("Enter Patient ID: ")

    if patient_id in patients_db:

        patient = patients_db[patient_id]

        print("\n===== PRESCRIPTION =====")
        print("Patient Name:", patient["name"])
        print("Patient ID:", patient_id)
        print("Diagnosis:", patient.get("diagnosis", "Not available"))
        print("Allergic History:", patient.get("allergy", "Not available"))

        medicines = patient.get("medicines", [])

        if len(medicines) == 0:
            print("\nNo medicines prescribed.")
            return

        print("\nMedicines:")

        for i, medicine in enumerate(medicines, start=1):
            print(i, ".", medicine)

        print("\n===== MEDICINE STATUS =====")

        medicine_status = []

        for medicine in medicines:

            answer = input(
                f"Has {medicine} been given? (yes/no): "
            )

            if answer.lower() == "yes":
                medicine_status.append("Given")
            else:
                medicine_status.append("Not Given")

        patient["medicine_status"] = medicine_status

        print("\nPrescription updated successfully!")

    else:
        print("\nPatient not found!")
