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
        query = "DELETE FROM Receitas WHERE id=?"
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
def ver_receitas():
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

# funcao para dados da tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []
    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)
    
    return tabela_lista


def bar_valores():
    # Receita Total ------------------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total ------------------------
    gastos = ver_gastos()
    gastos_lista = []

    for i in gastos:
        gastos_lista.append(i[3])

    gastos_total = sum(gastos_lista)

    # Despesas Total ------------------------
    saldo_total = receita_total - gastos_total

    return[receita_total,gastos_total,saldo_total]

def percentagem_valor():
    # Receita Total ------------------------
    receitas = ver_Receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total ------------------------
    receitas = ver_gastos()
    despesas_lista = []

    for i in receitas:
        despesas_lista.append(i[3])

    despesas_total = sum(despesas_lista)

    # Despesas Total ------------------------
    total =  ((receita_total - despesas_total) / receita_total) * 100

    return[total]

def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista,columns = ['id', 'Categoria', 'Data', 'valor'])

    # Get the sum of the durations per month
    dataframe = dataframe.groupby('Categoria')['valor'].sum()
   
    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias,lista_quantias])