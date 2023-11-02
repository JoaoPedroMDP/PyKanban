

class User:
    def __init__(self, id, name, password, login):
    # Para quando pegar do banco de dados
        self.id = id
        self.name = name
        self.password = password
        self.login = login

    def __init__(self, name, password, login):
    # Para quando criar novo usuário
        self.name = name
        self.password = password
        self.login = login

    # GETTERS
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getLogin(self):
        return self.login

    # SETTERS
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def setLogin(self, login):
        self.login = login