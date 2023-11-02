import datetime

class Column:
    def __init__(self, id, name, tasks, table):
        self.id = id
        self.name = name
        self.tasks = tasks
        self.table = table

    def __init__(self, name, tasks, table):
        self.name = name
        self.tasks = tasks
        self.table = table

    # GETTERS
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getTasks(self):
        return self.tasks

    def getTable(self):
        return self.table

    # SETTERS
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setTasks(self, tasks):
        self.tasks = tasks

    def setTable(self, table):
        self.table = table

    # METHODS
    def addTask(self, task):
        self.tasks.append(task)
        task.move(self)

    def sendTask(self, task, column):
        self.tasks.remove(task)
        column.addTask(task)

    def getStaleTasks(self, days):
        # Retorna todas as tasks que já estão numa mesma coluna há mais de 'days' dias
        now = datetime.datetime.now()
        stale_tasks = [task for task in self.tasks if (task.getMoved() + datetime.timedelta(days=days) < now)]
        return stale_tasks
