class Customer:
    def __init__(self, name, email, phone, status="Active"):
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def get_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "status": self.status
        }
