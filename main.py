from tkinter import *
import tkinter
import tkinter.messagebox
from ClasseEbook import *
import tkinter as tk
from tkinter import filedialog


# Geração de TK usando das funções da ClasseEbook importada.


# FUNÇÕES ACESSORIAS DE ACIONAMENTO DE BOTÕES
# Botão 0 = começar scrap
def btn_clicked0():
    site_inicio = f'{entry3.get()}'
    site_final = f'{entry2.get()}'
    copiar_ebook = ClasseEbook()
    copiar_ebook.copiarcapitulos(site_inicio=site_inicio, site_final=site_final)
    tkinter.messagebox.showinfo(title="Status do Scrap", message='Scrap Finalizado com sucesso')


# Botão 1 = Gerar Ebook

def btn_clicked1():
    caminho_ebook = ClasseEbook()
    caminho = var_caminho.get()
    if len(caminho) > 3:
        nome_ebook = f'{entry4.get()}'
        caminho_ebook.passarArquivo(caminho, nome_ebook)
        tkinter.messagebox.showinfo(title="Status do ebook", message=f'Ebook --{entry4.get()}-- gerado com sucesso')
    else:
        tkinter.messagebox.showinfo(f'Caminho de ebook não selecionado')


# Botão 2 = Gerar log

def btn_clicked2():
    log_ebook = ClasseEbook()
    lista = log_ebook.pegaLog()
    for item in lista:
        entry0.insert(tk.END, item + "\n")


# Botão 3 = Clique para selecionar destino do ebook
def btn_clicked3():
    caminho = filedialog.askdirectory(title='Selecione o diretório do e-book')
    tkinter.messagebox.showinfo(title="Seleção de caminho", message=f'Caminho selecionado:{caminho}')
    entry1.insert(0, f'Caminho: {caminho}')
    var_caminho.set(caminho)


# GERAÇÃO DA JANELA TK

window = Tk()

window.title('Ferramenta de scrap e geração de ebook')
window.geometry("1130x655")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=655,
    width=1130,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"GUI/background.png")
background = canvas.create_image(
    366.0, 327.5,
    image=background_img)

# Botão 0 = começar scrap
img0 = PhotoImage(file=f"GUI/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked0,
    relief="raised")

b0.place(
    x=732, y=441,
    width=397,
    height=102)

# Botão 1 = Gerar Ebook
img1 = PhotoImage(file=f"GUI/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked1,
    relief="raised")

b1.place(
    x=732, y=553,
    width=197,
    height=102)

# Botão 2 = Gerar log
novo_ebook = ClasseEbook()
img2 = PhotoImage(file=f"GUI/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked2,
    relief="raised")

b2.place(
    x=932, y=553,
    width=197,
    height=102)

var_caminho = tk.StringVar()

# Botão 3 =  clique para selecionar destino do ebook
img3 = PhotoImage(file=f"GUI/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked3,
    relief="raised")

b3.place(
    x=732, y=348,
    width=397,
    height=48)

# GERAÇÃO DAS ENTRADAS DE TEXTO DO TK ORDENADAS DE FORMA A RESPEITAR O TAB

# entry0 = Caixa de texto
entry0_img = PhotoImage(file=f"GUI/img_textBox0.png")
entry0_bg = canvas.create_image(
    931.5, 174.0,
    image=entry0_img)

entry0 = Text(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry0.place(
    x=732, y=0,
    width=399,
    height=340)

# entry4 = Nome do arquivo
entry4_img = PhotoImage(file=f"GUI/img_textBox4.png")
entry4_bg = canvas.create_image(
    502.0, 492.5,
    image=entry4_img)

entry4 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry4.place(
    x=288, y=477,
    width=428,
    height=29)

# entry3 = Endereço inicial
entry3_img = PhotoImage(file=f"GUI/img_textBox3.png")
entry3_bg = canvas.create_image(
    502.0, 542.5,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry3.place(
    x=288, y=527,
    width=428,
    height=29)

# entry2 = Endereço final
entry2_img = PhotoImage(file=f"GUI/img_textBox2.png")
entry2_bg = canvas.create_image(
    502.0, 592.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry2.place(
    x=288, y=577,
    width=428,
    height=29)

# entry1 = caminho do arquivo
entry1_img = PhotoImage(file=f"GUI/img_textBox1.png")
entry1_bg = canvas.create_image(
    932.5, 418.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry1.place(
    x=734, y=403,
    width=397,
    height=29)

window.resizable(False, False)
window.mainloop()
