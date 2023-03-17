from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox 
from PIL import Image, ImageTk

from tkinter import filedialog as fd
from tkcalendar import Calendar, DateEntry

from datetime import date
import re
from view import *


#cores

co0 = "#2e2d2b" #preta
co1 = "#d8d6d6" #branca
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" #verde
co8 = "#0263238" # + verde
co9 = "#e8e8e8" # + verde

#criando janela 

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE,height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#Criando Frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=303, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

#Criando funções --------------------------------------------------------------------------

global tree

#Função Inserir

def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_modelo.get()
    data = e_data.get()
    valor = validar_entrada_valor(e_valor.get())
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            
            messagebox.showerror('Erro','Preencha todos os campos')

            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_modelo.delete(0, 'end')
    e_data.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0,'end')


    mostrar()


#função atualizar 
def atualizar():
    global imagem, imagem_string, l_imagem
    try:

        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_modelo.delete(0, 'end')
        e_data.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0,'end')

        id = int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0,treev_lista[3])
        e_modelo.insert(0, treev_lista[4])
        e_data.insert(0,treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]

        def atualizar():

            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_modelo.get()
            data = e_data.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro','Preencha os campos')
                    return

            atualizar_form(lista_atualizar)
            messagebox.showinfo('Sucesso','Dados atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_modelo.delete(0, 'end')
            e_data.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0,'end')

            b_confirmar.destroy()

            mostrar()


        b_confirmar = Button(frameMeio, command=atualizar, width=15, text='Confirmar'.upper(), overrelief=RIDGE, font=('ivy 8'), bg=co2, fg=co0)
        b_confirmar.place(x=330, y=185)




    except IndexError:
        messagebox.showerror('Erro','Selecione um item da tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'os dados foram deletados com sucesso')

    except IndexError:
        messagebox.showerror('Erro','Selecione um item da tabela')

    mostrar()





def validar_entrada_valor(valor):


    if valor.isdigit() == TRUE:
        return valor
    else:
        messagebox.showerror('Erro','O valor inserido para o campo valor é inválido')
        valor = ''
        return valor 
        



#função para inserir imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    #abrindo imagem na tela

    imagem= Image.open(imagem)
    imagem= imagem.resize((170,170))
    imagem= ImageTk.PhotoImage(imagem)


    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


#fução para ver imagens 

def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item(valor)

    print(item)
    
    imagem = item[0][8]


    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=680, y=10)




#abrindo imagem

app_img = Image.open('img\inventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)


app_logo = Label(frameCima, image=app_img, text='Registro de Inventário', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

#criando entradas 

l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Local\Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)


l_descricao= Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao= Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)


l_modelo = Label(frameMeio, text='Marca\Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_modelo.place(x=130, y=101)

l_data = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_data.place(x=10, y=130)
e_data = DateEntry(frameMeio, width=12,Backgroud='darkblue', bordewidth=2,year=2023)
e_data.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor da Compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text='Número de Série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)


#Criando Botões 

#Botão Carregar

l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)

b_carregar = Button(frameMeio, command=escolher_imagem, width=29, text='Carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)


#Botão Inserir

image_add = Image.open('img/add.png')
image_add = image_add.resize((23,23))
image_add = ImageTk.PhotoImage(image_add)

b_inserir = Button(frameMeio, command=inserir, image=image_add, width=95, text='Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

#Botão Atualizar

image_update = Image.open('img/refresh.png')
image_update = image_update.resize((18,18))
image_update = ImageTk.PhotoImage(image_update)

l_update = Button(frameMeio, command =atualizar, image=image_update, width=95, text=' Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
l_update.place(x=330, y=50)

#Botão deletar

image_delete = Image.open('img/delete.png')
image_delete = image_delete.resize((18,18))
image_delete = ImageTk.PhotoImage(image_delete)

l_delete = Button(frameMeio, command=deletar, image=image_delete, width=95, text=' Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
l_delete.place(x=330, y=90)


#Botão ver item

image_item = Image.open('img/item.png')
image_item = image_item.resize((18,18))
image_item = ImageTk.PhotoImage(image_item)

l_item = Button(frameMeio, command=ver_imagem, image=image_item, width=95, text=' Ver item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
l_item.place(x=330, y=221)


# Labels Quantidade e Valores

l_total= Label(frameMeio,  text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)

l_total_= Label(frameMeio,  text='    Valor total dos itens:             ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=12)

l_qtd= Label(frameMeio,  text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=93)
l_qtd_= Label(frameMeio,  text='   Quantidade total de itens:     ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_.place(x=450, y=92)



# criando tabela 

def mostrar():

        global tree

        tabela_head = ['#Item','Nome', 'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

        lista_itens = visualizar_dados()

        print(lista_itens)



        tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        frameBaixo.grid_rowconfigure(0, weight=12)

        hd=["center","center","center","center","center","center","center", 'center']
        h=[40,150,100,160,130,100,100, 100]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            # adjust the column's width to the header string
            tree.column(col, width=h[n],anchor=hd[n])
            n+=1


        # inserindo os itens dentro da tabela
        for item in lista_itens:
            tree.insert("", "1", values=item)


        quantidade = [] #VALORES APRESENTADOS NA TELA

        for iten in lista_itens:
            quantidade.append(iten[6])

        Total_valor = sum(quantidade)
        Total_itens = len(quantidade)

        l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
        l_qtd['text'] = Total_itens

mostrar()



janela.mainloop()