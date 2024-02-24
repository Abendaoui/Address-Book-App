class Contact:
    
    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email
    def __str__(self):
        return f"{self.name}: {self.email}, {self.phone}"
    
