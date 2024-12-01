class Person:
    def __init__(self, name: str, age: int):
        self.name = name  
        self.age = age    

    def view_info(self) -> str:
        return f'Name: {self.name}, Age: {self.age}'


class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position  

    def view_info(self) -> str:
        return f'{super().view_info()}, Position: {self.position}'


class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str):
        super().__init__(name, age)
        self.medical_record = medical_record  

    def view_record(self) -> str:
        return f'Medical Record: {self.medical_record}'


class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name  
        self.location = location  
        self.departments = []  

    def add_department(self, department: 'Department') -> None:
        self.departments.append(department)

    def __str__(self) -> str:
        return f'Hospital Name: {self.name}, Location: {self.location}'


class Department:
    def __init__(self, name: str):
        self.name = name  
        self.patients = [] 
        self.staff = []  

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        self.staff.append(staff_member)

    def __str__(self) -> str:
        return f'Department Name: {self.name}'


def main():
    hospital_name = input("Enter hospital name: ")
    hospital_location = input("Enter hospital location: ")
    hospital = Hospital(hospital_name, hospital_location)

    dept_name = input("Enter department name: ")
    department = Department(dept_name)
    hospital.add_department(department)

    patient_name = input("Enter patient name: ")
    patient_age = int(input("Enter patient age: "))
    medical_record = input("Enter patient medical record: ")
    patient = Patient(patient_name, patient_age, medical_record)
    department.add_patient(patient)

    staff_name = input("Enter staff member name: ")
    staff_age = int(input("Enter staff member age: "))
    position = input("Enter staff member position: ")
    staff = Staff(staff_name, staff_age, position)
    department.add_staff(staff)

    print("\n--- Hospital Information ---")
    print(hospital)

    print("\n--- Department Information ---")
    print(department)

    print("\n--- Patient Information ---")
    print(patient.view_info())
    print(patient.view_record())

    print("\n--- Staff Information ---")
    print(staff.view_info())


if __name__ == "__main__":
    main()