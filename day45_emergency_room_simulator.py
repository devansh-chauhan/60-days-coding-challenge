import heapq

class EmergencyRoom:
    def __init__(self):
        self.patients = []

    def add_patient(self, name, severity):
        heapq.heappush(
            self.patients,
            (-severity, name)
        )
        print(f"{name} added with severity {severity}")

    def treat_patient(self):
        if not self.patients:
            print("No patients waiting.")
            return
        
        severity, name = heapq.heappop(self.patients)

        print(
            f"Treating {name} "
            f"(Severity: {-severity})"
        )

er = EmergencyRoom()
er.add_patient("John", 3)
er.add_patient("Emma", 8)
er.add_patient("David", 5)
er.add_patient("Sophia", 10)

print("\nProcessing Patients...\n")

er.treat_patient()
er.treat_patient()
er.treat_patient()
er.treat_patient()