class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        disease = input("Enter disease: ")

        patient = {"Name": name, "Age": age, "Disease": disease}
        self.patients.append(patient)

        print("Patient added successfully!\n")

    def view_patients(self):
        if not self.patients:
            print("No patient records found.\n")
            return

        print("\n--- Patient List ---")
        for i, p in enumerate(self.patients, start=1):
            print(f"{i}. Name: {p['Name']}, Age: {p['Age']}, Disease: {p['Disease']}")
        print()

    def search_patient(self):
        name = input("Enter patient name to search: ")
        found = False

        for p in self.patients:
            if p["Name"].lower() == name.lower():
                print(f"Found: Name: {p['Name']}, Age: {p['Age']}, Disease: {p['Disease']}\n")
                found = True

        if not found:
            print("Patient not found!\n")


# Main Program
hospital = Hospital()

while True:
    print("=== Hospital Management System ===")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        hospital.add_patient()
    elif choice == '2':
        hospital.view_patients()
    elif choice == '3':
        hospital.search_patient()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
