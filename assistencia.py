import openpyxl as xl
import customtkinter as ctk
from tkinter import *

tela = ctk.CTk()

class Application():
    def __init__(self):
        self.tela = tela
        self.tema()
        self.layout()
        self.tela_inicial()
        tela.mainloop()

    @staticmethod
    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def layout(self):
        self.tela.geometry("600x500")
        self.tela.title("HB GOSCH")
        self.tela.iconbitmap("fotos/dev.ico")
        self.tela.resizable(width=False, height=False)

    @staticmethod
    def tela_inicial():
        #Frames
        tela_principal = ctk.CTkFrame(master=tela, width=600, height=500, corner_radius=2, fg_color="black")
        tela_principal.place(x=0, y=0)

        #Frame esquerdo
        tela_esquerda = ctk.CTkFrame(master=tela, width=244, height=350, corner_radius=20, bg_color="black")
        tela_esquerda.place(x=35, y=120)

        #Frame direito
        tela_direita = ctk.CTkFrame(master=tela, width=244, height=350, corner_radius=20, bg_color="black")
        tela_direita.place(x=325, y=120)
    
        #saudações
        introdução = ctk.CTkLabel(master=tela_principal, text="Bem vindo(a)", font=("Krona One", 40, "bold"))
        introdução.place(x=182, y=30)

        #menus de opções-produto
        opcoes_categoria = ctk.CTkOptionMenu(master=tela_esquerda,
                                      values=["TELAS","CARREGADORES","BATERIAS","ACESSÓRIOS"],
                                    width=209, height=29, corner_radius=12, button_hover_color="black",
                                    dropdown_hover_color="blue", dropdown_font=("Montserrat",12,"bold"),
                                    dropdown_fg_color="black"
                                      )
        opcoes_categoria.place(x=18, y=40)
        opcoes_categoria.set("Categoria")
        #menus de opções-categoria

        opcoes_marca = ctk.CTkOptionMenu(master=tela_esquerda,
                                      values=["SAMSUNG","XIAOMI","APPLE","MOTOROLA","LG","POSITIVO"],
                                    width=209, height=29, corner_radius=12, button_hover_color="black",
                                    dropdown_hover_color="blue", dropdown_font=("Montserrat",12,"bold"),
                                    dropdown_fg_color="black"
                                      )
        opcoes_marca.place(x=18, y=100)
        opcoes_marca.set("Marca")

        #menus de opções-modelo
        opcoes_modelo = ctk.CTkOptionMenu(master=tela_esquerda,
                                      values=["SAMSUNG","XIAOMI","APPLE","MOTOROLA","LG","POSITIVO"],
                                    width=209, height=29, corner_radius=12, button_hover_color="black",
                                    dropdown_hover_color="blue", dropdown_font=("Montserrat",12,"bold"),
                                    dropdown_fg_color="black"
                                      )
        opcoes_modelo.place(x=18, y=160)
        opcoes_modelo.set("Modelo")

        #menus de opções-preço
        opcoes_quantidade = ctk.CTkOptionMenu(master=tela_esquerda,
                                      values=["1","2","3","4","5","6","7","8","9","10"],
                                    width=209, height=29, corner_radius=12, button_hover_color="black",
                                    dropdown_hover_color="blue", dropdown_font=("Montserrat",12,"bold"),
                                    dropdown_fg_color="black"
                                      )
        opcoes_quantidade.place(x=18, y=220)
        opcoes_quantidade.set("QUANTIDADE")


        #imagens
        imagem_principal = PhotoImage(file="fotos/logo.png")
        imagem_botao_delete = PhotoImage(file="fotos/delete.png")
        imagem_botao_save = PhotoImage(file="fotos/correto.png")

        #foto principal
        logo_label = ctk.CTkLabel(master=tela_esquerda, text="", image=imagem_principal)
        logo_label.place(x=90, y=270)
  
        #foto botao delete
        def teste():
            print("haba")
            
        delete_label = ctk.CTkButton(master=tela_direita, text="", image=imagem_botao_delete, fg_color="transparent",
        hover_color="gray", bg_color="transparent", hover=None,width=50, height=10, command=teste)
        delete_label.place(x=5, y=300)

        #foto botao save

        def teste():
            print("haba")

        save_label = ctk.CTkButton(master=tela_direita, text="", image=imagem_botao_save, fg_color="transparent",
        hover_color="gray", bg_color="transparent", hover=None,width=50, height=10, command=teste)
        save_label.place(x=125, y=300)

        #descrição do problema/troca
        descricso_problema = ctk.CTkLabel(master=tela_direita, text="Descrição(Troca/Problema)", font=("Montserrat", 16))
        descricso_problema.place(x=25, y=10)

        #descrição do problema/troca
        texto_box_descricao = ctk.CTkTextbox(master=tela_direita ,width=224, height=230)
        texto_box_descricao.place(x=10, y=50)

        texto_box_descricao.insert("0.0","Titulo\n\n" + "insira o problema ou a troca")

Application()










tela.mainloop()

