class Usuario:
    def __init__(self, nombre, email, password_hash):
        self.id = None
        self.nombre = nombre
        self.email = email
        self.password_hash = password_hash