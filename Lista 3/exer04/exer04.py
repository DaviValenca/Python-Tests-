class Avaliador:
    def __init__(self, codigo, nome, listaavaliadorprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.listaavaliadorprojeto = listaavaliadorprojeto

    def inserirAvaliadoProjeto(self,avaliadorprojeto):
        self.listaavaliadorprojeto.append(avaliadorprojeto)
    
    def verificaAvaliadoProjeto(self,avaliadorprojeto):
        return avaliadorprojeto in self.listaavaliadorprojeto
        
class Bolsista:
    def __init__(self, codigo, nome, matricula, cpf, curso, periodo, datadenascimento, endereco, listabolsistaprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.curso = curso
        self.periodo = periodo
        self.datadenascimento = datadenascimento 
        self.endereco = endereco
        self.listabolsistaprojeto = listabolsistaprojeto

    def inserirBolsistaProjeto(self,bolsistaprojeto):
        self.listabolsistaprojeto.append(bolsistaprojeto)
    
    def verificaBolsistaProjeto(self,bolsistaprojeto):
        return bolsistaprojeto in self.listabolsistaprojeto    

class Integrante:
    def __init__(self, codigo, nome, cpf, telefone, endereco, email, listaintegranteprojeto=[]):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.listaintegranteprojeto = listaintegranteprojeto

    def inserirIntegranteProjeto(self,integranteprojeto):
        self.listaintegranteprojeto.append(integranteprojeto)
    
    def verificarIntegranteProjeto(self,integranteprojeto):
        return integranteprojeto in self.listaintegranteprojeto    


class Projeto:
    def __init__(self, codigo, titulo, relatorio, datadesubmissao, resumo, situacao, listadeavaliadorprojeto=[], listadebolsistaprojeto=[],listadeintegranteprojeto=[],listadepesquisador=[]):
        self.codigo = codigo
        self.titulo = titulo
        self.relatorio = relatorio
        self.datadesubmissao = datadesubmissao
        self.resumo = resumo
        self.situacao = situacao
        self.listadeavaliadorprojeto = listadeavaliadorprojeto
        self.listadebolsistaprojeto = listadebolsistaprojeto
        self.listadeintegranteprojeto = listadeintegranteprojeto
        self.listadepesquisador = listadepesquisador

    def inserirAvaliadoProjeto(self,avaliadorprojeto):
        self.listadeavaliadorprojeto.append(avaliadorprojeto)
    
    def verificaAvaliadoProjeto(self,avaliadorprojeto):
        return avaliadorprojeto in self.listadeavaliadorprojeto

    def inserirIntegranteProjeto(self,integranteprojeto):
        self.listadeintegranteprojeto.append(integranteprojeto)
    
    def verificarIntegranteProjeto(self,integranteprojeto):
        return integranteprojeto in self.listadeintegranteprojeto

    def inserirBolsistaProjeto(self,bolsistaprojeto):
        self.listadebolsistaprojeto.append(bolsistaprojeto)
    
    def verificaBolsistasProjeto(self,bolsistaprojeto):
        return bolsistaprojeto in self.listadebolsistaprojeto   

    def inserirPesquisador(self,pesquisador):
        self.listadepesquisador.append(pesquisador)
    
    def verificarPesquisador(self,pesquisador):
        return pesquisador in self.listadepesquisador


class Edital:
    def __init__(self, codigo, nome, datadeinicio, datadetermino, projeto):
        self.codigo = codigo
        self.nome = nome
        self.datadeinicio = datadeinicio
        self.datadetermino = datadetermino
        self.projeto = projeto

class Pesquisador:
    def __init__(self, codigo, nome, cpf, telefone, endereco, email, projeto):

        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.projeto = projeto
        

class AvaliadorProjeto:
    def __init__(self, datacomeco, dataentrega, parecer, nota, avaliador, projeto):
        self.datacomeco = datacomeco
        self.dataentrega = dataentrega
        self.parecer = parecer
        self.nota = nota
        self.avaliador = avaliador
        self.projeto = projeto

class IntegranteProjeto:
    def __init__(self,datainicio, datafim, cargo, setor, projeto, integrante):

        self.datainicio = datainicio
        self.datafim = datafim
        self.cargo = cargo
        self.setor = setor
        self.projeto = projeto
        self.integrante = integrante


class BolsistaProjeto:

    def __init__(self, datainicio, datafim, cargo, setor, bolsista, projeto):
        self.datainicio = datainicio   
        self.datafim = datafim
        self.cargo = cargo
        self.setor = setor
        self.bolsista = bolsista
        self.projeto = projeto

    

   
 
