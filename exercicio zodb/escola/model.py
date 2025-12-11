import persistent

class Aluno(persistent.Persistent):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.frequencia = 0

class Turma(persistent.Persistent):
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []
        self.aulas_ministradas = 0

    def registar_aluno(self, nome, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                raise ValueError("Aluno com esta matrícula já está registrado nesta turma.")
        novo_aluno = Aluno(nome, matricula)
        self.alunos.append(novo_aluno)
        

    def adicionar_aula(self):
        self.aulas_ministradas += 1
        for aluno in self.alunos:
            aluno_presente = input(f"O aluno {aluno.nome} (Matrícula: {aluno.matricula}) está presente? (s/n): ").strip().lower()
            if aluno_presente == 's':
                aluno.frequencia += 1


    def calcular_frequencia_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                if self.aulas_ministradas == 0:
                    return 0.0
                return (aluno.frequencia / self.aulas_ministradas) * 100
        raise ValueError("Aluno não encontrado nesta turma.")
    
    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado nesta turma.")
            return
        print(f"Lista de alunos na turma {self.nome} ({self.codigo}):")
        for aluno in self.alunos:
            freq = self.calcular_frequencia_aluno(aluno.matricula)
            print(f"Matrícula: {aluno.matricula}, Nome: {aluno.nome}, Frequência: {freq:.2f}%")
    


class Escola(persistent.Persistent):
    def __init__(self):
        self.turmas = []
        self.alunos = []

    def matricular_aluno(self, nome, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                raise ValueError("Aluno com esta matrícula já está cadastrado na escola.")
        novo_aluno = Aluno(nome, matricula)
        self.alunos.append(novo_aluno)

    def cadastrar_turma(self, nome, codigo):
        for turma in self.turmas:
            if turma.codigo == codigo:
                raise ValueError("Turma com este código já está cadastrada.")
        nova_turma = Turma(nome, codigo)
        self.turmas.append(nova_turma)

    def buscar_turma(self, codigo):
        for turma in self.turmas:
            if turma.codigo == codigo:
                return turma
        raise ValueError("Turma não encontrada.")
    
    def listar_turmas(self):
        if not self.turmas:
            print("Nenhuma turma cadastrada.")
            return
        print("Lista de todas as turmas:")
        for turma in self.turmas:
            print(f"Código: {turma.codigo}, Nome: {turma.nome}, Alunos: {len(turma.alunos)}, Aulas Ministradas: {turma.aulas_ministradas}")
        
