
class Table:
    def __init__(self, id, name, description, columns, user):
       #  Para quando pegar do banco de dados
        self.id = id
        self.name = name
        self.description = description
        self.columns = columns
        self.user = user

    def __init__(self, name, description, columns, user):
       #  Para quando pegar do banco de dados
        self.name = name
        self.description = description
        self.columns = columns
        self.user = user

    # GETTERS
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getColumns(self):
        return self.columns

    def getUser(self):
        return self.user

    # SETTERS
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setColumns(self, columns):
        self.columns = columns

    def setUser(self, user):
        self.user = user

    # METHODS
    def addColumn(self, column):
        self.columns.append(column)

    def removeColumn(self, column):
        self.columns.remove(column)