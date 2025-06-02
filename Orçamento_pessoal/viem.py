# importando SQLite
import sqlite3 as lite

# Criando conexao
con = lite.connect('dados.db')

#------------------------------------- Funções -------------------------------------

# Inserir categoria

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)


# Inserir receitas

def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas(categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Inserir Gastos

def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos(categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# ------------------------------------- Funções para deletar -------------------------------------

# Deletar Receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Recitas WHERE id=?"
        cur.execute(query, i)

# Deletar Gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

# ------------------------------------- Funções para ver dados -------------------------------------

# ver categoria
def ver_categoria():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    
    return lista_itens


# ver Receitas
def ver_recitas():
    lista_itens = []
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    
    return lista_itens

# ver Gastos
def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    
    return lista_itens