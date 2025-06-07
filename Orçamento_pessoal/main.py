from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# Importando barra de progresso do tlinter
from tkinter.ttk import Progressbar

# Importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando funcoes da view
from view import inserir_categoria, inserir_receita, inserir_gastos, ver_categoria, tabela, bar_valores, percentagem_valor, pie_valores, deletar_gastos, deletar_receitas
# ----------------------------------- Cores -----------------------------------------------

co0 = "#000000"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#42535e"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

#----------------------------------- Criando janela ---------------------------------------
janele = Tk()
janele.title()
janele.geometry('900x650')
janele.config(background=co0)
janele.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janele)
style.theme_use("clam")

# criando Frame para diviaso da tela
frameCima = Frame(janele,width=1043, height=50, bg=co3, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janele,width=1043, height=361, bg=co3, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janele,width=1043, height=300, bg=co3, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415,y=5)

# Criando frames dentro do Frame Baixo

frame_renda = Frame(frameBaixo,width=300, height=250, bg=co3, relief="flat")
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBaixo,width=220, height=250, bg=co3)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_configuracao = Frame(frameBaixo,width=220, height=250, bg=co3)
frame_configuracao.grid(row=0, column=2, padx=5)

# Trabalhando no frame cima
# Acessando a imagem
app_img = Image.open('log.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento Pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co3, fg=co1)
app_logo.place(x=0, y=0)

# definindo tree como global
global tree

# funcao inserir categoria
def inserir_categoria_b():
    nome = e_categoria.get()
    lista_inserir = [nome]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # passamdo para a funcoes inserir gastos presente na view    
    inserir_categoria(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')


    e_categoria.delete(0,'end')

    # Pegandos os valores da categoria
    categorias_funcoes = ver_categoria()
    categoria = []

    for i in categorias_funcoes:
        categoria.append(i[1])
    
    # atualizando a lista de categorias
    combo_categoria_despesas['values'] = (categoria)


# funcao inserir receitas
def inserir_receita_b():
    nome = 'Receita'
    data = e_cal_receitas.get()
    quantia = e_valor_receitas.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    # Chamando a funcao inserir Receitas presente na view
    inserir_receita(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_cal_receitas.delete(0,'end')
    e_valor_receitas.delete(0,'end')

    # atualizando dados
    mostrar_renda()
    porcentagem()
    grafico_bar
    resumo()
    grafico_pie()


# funcao inserir despesas
def inserir_receita_b():
    nome = combo_categoria_despesas.get()
    data = e_cal_despesas.get()
    quantia = e_valor_despesas.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    # Chamando a funcao inserir despesas presente na view
    inserir_gastos(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    combo_categoria_despesas.delete(0, 'end')
    e_cal_despesas.delete(0,'end')
    e_valor_despesas.delete(0,'end')

    # atualizando dados
    mostrar_renda()
    porcentagem()
    grafico_bar
    resumo()
    grafico_pie()


# funcao deletar 
def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]

        if nome == 'Receita':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            # atualizando dados
            mostrar_renda()
            porcentagem()
            grafico_bar
            resumo()
            grafico_pie()
        
        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            # atualizando dados
            mostrar_renda()
            porcentagem()
            grafico_bar
            resumo()
            grafico_pie()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

#---------------------------------- porcentagem ---------------------------------------------

def porcentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gasta", height=1, anchor=NW, font=('Verdana 12'), bg=co3, fg=co1)
    l_nome.place(x=7, y=5)

    style =ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)
    
    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = 50
    valor = 50

    l_porcentagem = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co3, fg=co1)
    l_porcentagem.place(x=200, y=35)


#--------------------------- função para gráficos bars ----------------------------------
def grafico_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6540]

    figura = plt.figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    for c, i in enumerate(ax.patches):
        ax.text(i.get_x() - .001, i.get_height() + .5,
                str("{:,.0f}".format(lista_valores[c])), 
                fontsize=17, fontstyle='italic', 
                verticalalignment='bottom', color='dimgrey')

    ax.set_xticks(range(len(lista_categorias)))
    ax.set_xticklabels(lista_categorias, fontsize=16)

    ax.patch.set_facecolor(co1)
    ax.spines['bottom'].set_color("#1A44CE")
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color("#F50C0C")
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=co3)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

# Função de resumo total
def resumo():
    valor = [500, 600, 420]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg="#000000")
    l_linha.place(x=309, y=52)
    
    l_sumario = Label(frameMeio, text="Renda Mensal               ".upper(), anchor=NW, font=('Verdana 12'), bg=co3, fg='#83a9e6')
    l_sumario.place(x=309, y=35)

    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co3, fg='#83a9e6')
    l_sumario.place(x=309, y=70)


    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg="#000000")
    l_linha.place(x=309, y=132)
    
    l_sumario = Label(frameMeio, text="Despesas Mensais         ".upper(), anchor=NW, font=('Verdana 12'), bg=co3, fg='#83a9e6')
    l_sumario.place(x=309, y=115)

    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co3, fg='#83a9e6')
    l_sumario.place(x=309, y=150)


    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg="#000000")
    l_linha.place(x=309, y=207)
    
    l_sumario = Label(frameMeio, text="Total do Saldo            ".upper(), anchor=NW, font=('Verdana 12'), bg=co3, fg='#83a9e6')
    l_sumario.place(x=309, y=190)

    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co3, fg='#83a9e6')
    l_sumario.place(x=309, y=220)


# funcao grafico pie
def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90, facecolor=co3)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    # only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)

# ----------------------------- Tabela Renda mensal -------------------------------------
app_tabela = Label(frameMeio, text="Tabela Receita e Despesas", anchor=NW, font=('Verdana 12'), bg=co3, fg=co1)
app_tabela.place(x=5, y=309)

####### Codigo usado para o a tabela:

# funcao para mostrar_renda
def mostrar_renda():

    # Criando um estilo personalizado para a Treeview
    style = ttk.Style()
    style.configure("Treeview",
        background=co3,       # Cor de fundo das células
        foreground=co1,       # Cor do texto
        fieldbackground=co3)  # Cor de fundo ao editar a célula
    style.map("Treeview", background=[("selected", co6)])  # Cor ao selecionar linha
    
    # creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

# configuracoes Despesas
l_info = Label(frame_operacoes, text='Insira novas despesas', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co3, fg=co1)
l_info.place(x=10, y=10)

# ------------------------------- categoria -------------------------------
l_categoria = Label(frame_operacoes, text='Categoria', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_categoria.place(x=10, y=40)

# Pegando categoria

categoria_funcao = ver_categoria()
categoria = []
for i in categoria_funcao:
    categoria.append(i[1])

combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10, font='Ivy 10')
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=110, y=41)

# Despesas
l_cal_despesas = Label(frame_operacoes, text='Data', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_cal_despesas.place(x=10, y=70)
e_cal_despesas = DateEntry(frame_operacoes, width=12, background='darkblue', foreground='white', borderwidth=2, year=2025)
e_cal_despesas.place(x=110, y=71)

# Valor
l_valor_despesas = Label(frame_operacoes, text='Quantia Total', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_valor_despesas.place(x=10, y=100)
e_valor_despesas = Entry(frame_operacoes,width=14, justify='left', relief='solid')
e_valor_despesas.place(x=110, y=101)

# Botao Inserir
img_add_despesas = Image.open('add.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes, command=inserir_receita_b, image=img_add_despesas, text=" Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co3, fg=co1, overrelief=RIDGE)
botao_inserir_despesas.place(x=110, y=131)

# Botao Excluir
l_excluir = Label(frame_operacoes, text='Excluir ação', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
l_excluir.place(x=10, y=190)
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((17,17))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button(frame_operacoes,command=deletar_dados, image=img_delete, text=" Deletar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co3, fg=co1, overrelief=RIDGE)
botao_delete.place(x=110, y=190)

#------------------------------- configuracoes Receitas -------------------------------

l_info = Label(frame_configuracao, text='Insira novas receitas', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co3, fg=co1)
l_info.place(x=10, y=10)

# calendario 
l_cal_receitas = Label(frame_configuracao, text='Data', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_cal_receitas.place(x=10, y=40)
e_cal_receitas = DateEntry(frame_configuracao, width=12, background='darkblue', foreground='white', borderwidth=2, year=2025)
e_cal_receitas.place(x=110, y=41)

# Valor
l_valor_receitas = Label(frame_configuracao, text='Quantia Total', height=1, anchor=NW, font=('Ivy 10'), bg=co3, fg=co1)
l_valor_receitas.place(x=10, y=70)
e_valor_receitas = Entry(frame_configuracao,width=14, justify='left', relief='solid')
e_valor_receitas.place(x=110, y=71)

# Botao Inserir
img_add_receitas = Image.open('add.png')
img_add_receitas = img_add_receitas.resize((17,17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas)
botao_inserir_receitas = Button(frame_configuracao, command=inserir_receita_b, image=img_add_receitas, text=" Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co3, fg=co1, overrelief=RIDGE)
botao_inserir_receitas.place(x=110, y=111)

#------------------------------- Operacao Nova catetoria -------------------------------
l_info = Label(frame_configuracao, text='Insira Categoria', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co1)
l_info.place(x=5, y=160)
e_categoria = Entry(frame_configuracao,width=14, justify='left', relief='solid')
e_categoria.place(x=110, y=160)

# Botao Inserir
img_add_categoria = Image.open('add.png')
img_add_categoria = img_add_categoria.resize((17,17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)
botao_inserir_categoriaimg_add_categoria = Button(frame_configuracao,command=inserir_categoria_b, image=img_add_categoria, text=" Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co3, fg=co1, overrelief=RIDGE)
botao_inserir_categoriaimg_add_categoria.place(x=110, y=190)

porcentagem()
grafico_bar()
resumo()
grafico_pie()
mostrar_renda()



janele.mainloop()