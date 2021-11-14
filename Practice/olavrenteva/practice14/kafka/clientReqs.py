class ClientReqs:
    def __init__(self, surname, request_type, request_body):
        self.surname = surname
        self.request_type = request_type
        self.request_body = request_body

    def __str__(self):
        return f'Client {self.surname}: {self.request_body}'
