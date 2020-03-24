class Voluntário:
    def __init__(self, nome, tarefa):
        self.nome = nome
        self.tarefa = tarefa

    def setNome(self, nome):
        self.nome = nome

    def setTarefa(self, tarefa):
        self.tarefa = tarefa

    def getNome(self):
        return self.nome

    def getTarefa(self):
        return self.tarefa


