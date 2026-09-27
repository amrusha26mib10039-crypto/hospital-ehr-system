# Chemist Module

def chemist_section(patients_db):
    
    print("\n====== CHEMIST SECTION ======")

    patient_id = input("Enter Patient ID: ")

    if patient_id in patients_db:

        patient = patients_db[patient_id]

        print("\n==== PRESCRIPTION ====")
        print("Patient Name:", patient["name"])
        print("Patient ID:", patient_id)
        print("Diagnosis:", patient.get("diagnosis", "Not available"))
        print("Allergic History:", patient.get("allergy", "Not available"))

        medicines = patient.get("medicines", [])

        if len(medicines) == 0:
            print("\nNo medicines prescribed.")
            return

        print("\n==== BILL GENERATION ====")

        total = 0

        for medicine in medicines:
            price = float(input(f"Enter price for {medicine}: ₹"))
            total += price

        print("\n=========== BILL ===========")
        print("Patient Name:", patient["name"])
        print("Patient ID:", patient_id)

        print("\nMedicines:")
        for medicine in medicines:
            print("-", medicine)

        print("\nTotal Amount: ₹", total)
        print("==========================")

        print("\nBill generated successfully!")

    else:
        print("\nPatient not found!")
