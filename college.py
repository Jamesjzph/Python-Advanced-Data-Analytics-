class Founder:
    def __init__(self):
        # The ultimate data source
        self._student_records = {"Alice": "Grade: A, Attendance: 95%", "Bob": "Grade: B, Attendance: 88%"}

    def get_data_from_vault(self, student_name):
        # This is the hidden 'deep' logic
        return self._student_records.get(student_name, "Record not found.")

class Management:
    def __init__(self):
        self.founder = Founder()

    def process_request(self, student_name):
        # Management abstracts the Founder
        return self.founder.get_data_from_vault(student_name)

class Mentor:
    def __init__(self):
        self.management = Management()

    def get_student_details(self, student_name):
        # The Mentor is the only one the Parent talks to
        print(f"[Mentor]: Checking with Management for {student_name}...")
        return self.management.process_request(student_name)

# --- The User Interaction (The Parent) ---
class Parent:
    def ask_about_child(self, name):
        mentor = Mentor()
        # The parent ONLY interacts with the Mentor's simple method
        result = mentor.get_student_details(name)
        print(f"[Parent Received]: {result}")

# Execution
p = Parent()
p.ask_about_child("alan")