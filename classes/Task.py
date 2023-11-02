
import datetime

class Task:
    def __init__(self, id , name, description, created, updated, moved, column):
    #  Para quando pegar do banco de dados
        self.id = id
        self.name = name
        self.description = description
        self.column = column

        self.created = created
        self.updated = updated
        self.moved = moved

    def __init__(self, name, description, column):
        #  Para quando criar nova task
        self.name = name
        self.description = description
        self.column = column

        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        self.moved = datetime.datetime.now()

    def __init__(self, name, column):
        #  Para quando criar nova task sem descrição
        self.name = name
        self.description = ''
        self.column = column

        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        self.moved = datetime.datetime.now()

    # GETTERS
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getCreated(self):
        return self.created

    def getUpdated(self):
        return self.updated

    def getMoved(self):
        return self.moved

    def getColumn(self):
        return self.column

    # SETTERS
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.touch()
        self.name = name

    def setDescription(self, description):
        self.touch()
        self.description = description

    def setCreated(self, created):
        self.created = created

    def setUpdated(self, updated):
        self.updated = updated

    def setMoved(self, moved):
        self.moved = moved

    def setColumn(self, column):
        self.column = column

    # METHODS
    def touch(self):
        self.updated = datetime.datetime.now()

    def move(self, column):
        self.column = column
        self.touch()
        self.moved = datetime.datetime.now()