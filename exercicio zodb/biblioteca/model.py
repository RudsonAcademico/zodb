import persistent

class Usuario(persistent.Persistent):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Livro(persistent.Persistent):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

class Biblioteca(persistent.Persistent):
    def __init__(self):
        self.usuarios = []
        self.livros = []

    def cadastrar_livro(self, titulo, autor):
        for livro in self.livros:
            if livro.titulo == titulo:
                raise ValueError("Livro com este título já está cadastrado.")
        novo_livro = Livro(titulo, autor)
        self.livros.append(novo_livro)

    def cadastrar_usuario(self, nome, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                raise ValueError("Usuário com este email já está cadastrado.")
        novo_usuario = Usuario(nome, email)
        self.usuarios.append(novo_usuario)

    def registrar_emprestimo(self, titulo, email):
        livro_encontrado = None
        for livro in self.livros:
            if livro.titulo == titulo:
                livro_encontrado = livro
                break
        if not livro_encontrado:
            raise ValueError("Livro não encontrado.")

        if livro_encontrado.emprestado:
            raise ValueError("Livro já está emprestado.")

        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.email == email:
                usuario_encontrado = usuario
                break
        if not usuario_encontrado:
            raise ValueError("Usuário não encontrado.")

        livro_encontrado.emprestado = f"Emprestado para: {usuario_encontrado.nome}"
        print(f"Empréstimo registrado: {usuario_encontrado.nome} pegou o livro '{livro_encontrado.titulo}'.")

    def registrar_devolucao(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.emprestado:
                    raise ValueError("Livro não está emprestado.")
                livro.emprestado = False
                print(f"Devolução registrada: O livro '{livro.titulo}' foi devolvido.")
                return
        raise ValueError("Livro não encontrado.")
    
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("Lista de todos os livros:")
        for livro in self.livros:
            status = livro.emprestado if livro.emprestado else "Disponível"
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Status: {status}")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("Lista de todos os usuários e seus livros emprestados:")
        for usuario in self.usuarios:
            livros_emprestados = [livro.titulo for livro in self.livros if livro.emprestado and usuario.nome in livro.emprestado]
            livros_str = ', '.join(livros_emprestados) if livros_emprestados else "Nenhum livro emprestado"
            print(f"Usuário: {usuario.nome}, Livros emprestados: {livros_str}")