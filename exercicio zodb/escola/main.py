from model import Escola, Turma, Aluno
from ZODB import DB, FileStorage
import transaction

print("--- Sistema de Gerenciamento Escolar ---\n1. Matricular novo aluno\n2. Cadastrar nova turma\n3. Registrar aluno em turma\n4. Adicionar aula a turma\n5. Calcular frequência de aluno em turma\n6. Listar alunos de uma turma\n7. Buscar turma\n8. Listar turmas\n0. Sair")
requisito = int(input("Escolha uma opção: "))
storage = FileStorage.FileStorage('escola.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

if 'escola' not in root:
    root.escola = Escola()
escola = root.escola

while requisito != 0:
    if requisito == 1:
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")

        try:
            escola.matricular_aluno(nome, matricula)
            transaction.commit()
            print("Aluno matriculado com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 2:
        nome = input("Digite o nome da turma: ")
        codigo = input("Digite o código da turma: ")

        try:
            escola.cadastrar_turma(nome, codigo)
            transaction.commit()
            print("Turma cadastrada com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 3:
        codigo_turma = input("Digite o código da turma: ")
        matricula_aluno = input("Digite a matrícula do aluno: ")

        try:
            turma_encontrada = None
            aluno_encontrado = None
            
            for turma in escola.turmas:
                if turma.codigo == codigo_turma:
                    turma_encontrada = turma
                    break
            if not turma_encontrada:
                raise ValueError("Turma não encontrada.")
            
            for aluno in escola.alunos:
                if aluno.matricula == matricula_aluno:
                    aluno_encontrado = aluno
                    break
            
            if not aluno_encontrado:
                raise ValueError("Aluno não encontrado na escola.")
            
            turma_encontrada.registar_aluno(aluno_encontrado.nome, matricula_aluno)
            transaction.commit()
            print("Aluno registrado na turma com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 4:
        codigo_turma = input("Digite o código da turma: ")

        try:
            turma_encontrada = None
            for turma in escola.turmas:
                if turma.codigo == codigo_turma:
                    turma_encontrada = turma
                    break
            if not turma_encontrada:
                raise ValueError("Turma não encontrada.")

            turma_encontrada.adicionar_aula()
            transaction.commit()
            print("Aula adicionada com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")
    
    elif requisito == 5:
        codigo_turma = input("Digite o código da turma: ")
        matricula_aluno = input("Digite a matrícula do aluno: ")

        try:
            turma_encontrada = None
            for turma in escola.turmas:
                if turma.codigo == codigo_turma:
                    turma_encontrada = turma
                    break
            if not turma_encontrada:
                raise ValueError("Turma não encontrada.")

            frequencia = turma_encontrada.calcular_frequencia_aluno(matricula_aluno)
            print(f"A frequência do aluno na turma é: {frequencia:.2f}%")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")
    
    elif requisito == 6:
        codigo_turma = input("Digite o código da turma: ")

        try:
            turma_encontrada = None
            for turma in escola.turmas:
                if turma.codigo == codigo_turma:
                    turma_encontrada = turma
                    break
            if not turma_encontrada:
                raise ValueError("Turma não encontrada.")

            turma_encontrada.listar_alunos()
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 7:
        codigo_turma = input("Digite o código da turma: ")

        try:
            turma = escola.buscar_turma(codigo_turma)
            print(f"Turma encontrada: {turma.nome} ({turma.codigo})")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 8:
        if not escola.turmas:
            print("Nenhuma turma cadastrada na escola.")
        else:
            print("Lista de turmas na escola:")
            for turma in escola.turmas:
                print(f"Código: {turma.codigo}, Nome: {turma.nome}")
        input("Pressione Enter para continuar...")
    
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...")
    
    print("\n--- Sistema de Gerenciamento Escolar ---\n1. Matricular novo aluno\n2. Cadastrar nova turma\n3. Registrar aluno em turma\n4. Adicionar aula a turma\n5. Calcular frequência de aluno em turma\n6. Listar alunos de uma turma\n7. Buscar turma\n8. Listar turmas\n0. Sair")
    requisito = int(input("Escolha uma opção: "))