class TicketModel:
    def __init__(self):
        # Define the users ID, Password 
        self.users = {
            'MIT242543@stud.mit.edu.au': 'Abc12345!@#',
            'test': 'test',
        }

    # validate user and password
    def validate_user(self, username, password):
        return self.users.get(username) == password

