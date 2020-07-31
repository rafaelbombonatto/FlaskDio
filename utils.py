from models import Pessoas, db_session, Usuarios

def insere_pessoa():
    pessoa = Pessoas(nome='João', idade=39)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
       

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()        
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuario():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    #insere_pessoa()
    #consulta_pessoa()
    insere_usuario('rafael','123')
    consulta_usuario()
