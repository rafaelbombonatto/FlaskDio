from models import Pessoas, db_session

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

if __name__ == '__main__':
    #insere_pessoa()
    #consulta_pessoa()
    exclui_pessoa()
    consulta_pessoa()
