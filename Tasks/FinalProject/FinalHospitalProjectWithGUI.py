from tkinter import *
from tkinter import messagebox, ttk


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


class Department:
    def __init__(self, name: str):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def __str__(self) -> str:
        return f"Department: {self.name}, Patients: {len(self.patients)}, Staff: {len(self.staff)}"


class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department: Department) -> None:
        self.departments.append(department)

    def __str__(self) -> str:
        return f'Hospital: {self.name}, Location: {self.location}, Departments: {len(self.departments)}'


hospital = None


def create_hospital():
    def submit_hospital():
        global hospital
        name = hospital_name_entry.get()
        location = hospital_location_entry.get()
        if name and location:
            hospital = Hospital(name, location)
            messagebox.showinfo("Success", f"Hospital '{name}' created!")
            hospital_frame.configure(text=f"Hospital: {hospital.name}, Location: {hospital.location}")
            hospital_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    hospital_window = Toplevel()
    hospital_window.title("Create Hospital")
    hospital_window.configure(bg="#e3f2fd")
    Label(hospital_window, text="Hospital Name:", bg="#e3f2fd", fg="#0d47a1").grid(row=0, column=0, padx=10, pady=10)
    hospital_name_entry = Entry(hospital_window, width=30)
    hospital_name_entry.grid(row=0, column=1)

    Label(hospital_window, text="Location:", bg="#e3f2fd", fg="#0d47a1").grid(row=1, column=0, padx=10, pady=10)
    hospital_location_entry = Entry(hospital_window, width=30)
    hospital_location_entry.grid(row=1, column=1)

    Button(hospital_window, text="Submit", command=submit_hospital, bg="#0d47a1", fg="white").grid(
        row=2, column=0, columnspan=2, pady=10)


def add_department():
    def submit_department():
        if hospital is None:
            messagebox.showerror("Error", "Create a hospital first.")
            return

        name = dept_name_entry.get()
        if name:
            department = Department(name)
            hospital.add_department(department)
            department_list.insert("", "end", values=(name, len(department.patients), len(department.staff)))
            dept_window.destroy()
        else:
            messagebox.showerror("Error", "Department name is required.")

    dept_window = Toplevel()
    dept_window.title("Add Department")
    dept_window.configure(bg="#f3e5f5")
    Label(dept_window, text="Department Name:", bg="#f3e5f5", fg="#6a1b9a").grid(row=0, column=0, padx=10, pady=10)
    dept_name_entry = Entry(dept_window, width=30)
    dept_name_entry.grid(row=0, column=1)

    Button(dept_window, text="Submit", command=submit_department, bg="#6a1b9a", fg="white").grid(
        row=1, column=0, columnspan=2, pady=10)


def add_patient():
    def submit_patient():
        if hospital is None:
            messagebox.showerror("Error", "Create a hospital first.")
            return

        name = patient_name_entry.get()
        age = patient_age_entry.get()
        record = patient_record_entry.get()
        dept_name = patient_dept_entry.get()

        if name and age.isdigit() and record and dept_name:
            for dept in hospital.departments:
                if dept.name == dept_name:
                    patient = Patient(name, int(age), record)
                    dept.add_patient(patient)
                    patient_list.insert("", "end", values=(name, age, record, dept_name))
                    patient_window.destroy()
                    return
            messagebox.showerror("Error", f"Department '{dept_name}' not found.")
        else:
            messagebox.showerror("Error", "All fields are required and age must be a number.")

    patient_window = Toplevel()
    patient_window.title("Add Patient")
    patient_window.configure(bg="#fffde7")
    Label(patient_window, text="Name:", bg="#fffde7", fg="#f57f17").grid(row=0, column=0, padx=10, pady=10)
    patient_name_entry = Entry(patient_window, width=30)
    patient_name_entry.grid(row=0, column=1)

    Label(patient_window, text="Age:", bg="#fffde7", fg="#f57f17").grid(row=1, column=0, padx=10, pady=10)
    patient_age_entry = Entry(patient_window, width=30)
    patient_age_entry.grid(row=1, column=1)

    Label(patient_window, text="Medical Record:", bg="#fffde7", fg="#f57f17").grid(row=2, column=0, padx=10, pady=10)
    patient_record_entry = Entry(patient_window, width=30)
    patient_record_entry.grid(row=2, column=1)

    Label(patient_window, text="Department:", bg="#fffde7", fg="#f57f17").grid(row=3, column=0, padx=10, pady=10)
    patient_dept_entry = Entry(patient_window, width=30)
    patient_dept_entry.grid(row=3, column=1)

    Button(patient_window, text="Submit", command=submit_patient, bg="#f57f17", fg="white").grid(
        row=4, column=0, columnspan=2, pady=10)


# Main GUI
root = Tk()
root.title("Hospital Management System")
root.configure(bg="#e8f5e9")

hospital_frame = LabelFrame(root, text="Hospital Information", bg="#e8f5e9", fg="#1b5e20", font=("Arial", 14, "bold"))
hospital_frame.pack(fill="both", padx=20, pady=10)

Button(root, text="Create Hospital", command=create_hospital, bg="#1b5e20", fg="white", width=20).pack(pady=10)
Button(root, text="Add Department", command=add_department, bg="#43a047", fg="white", width=20).pack(pady=10)
Button(root, text="Add Patient", command=add_patient, bg="#66bb6a", fg="white", width=20).pack(pady=10)

# TreeView for Departments
Label(root, text="Departments", bg="#e8f5e9", fg="#1b5e20", font=("Arial", 12, "bold")).pack(pady=5)
department_list = ttk.Treeview(root, columns=("Name", "Patients", "Staff"), show="headings")
department_list.heading("Name", text="Name")
department_list.heading("Patients", text="Patients")
department_list.heading("Staff", text="Staff")
department_list.pack(padx=20, pady=5)

# TreeView for Patients
Label(root, text="Patients", bg="#e8f5e9", fg="#1b5e20", font=("Arial", 12, "bold")).pack(pady=5)
patient_list = ttk.Treeview(root, columns=("Name", "Age", "Record", "Department"), show="headings")
patient_list.heading("Name", text="Name")
patient_list.heading("Age", text="Age")
patient_list.heading("Record", text="Record")
patient_list.heading("Department", text="Department")
patient_list.pack(padx=20, pady=5)

root.mainloop()
