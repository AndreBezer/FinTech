import customtkinter as ctk
from SegundaTela import TelaAdicionar, dados

# Configuração da aparencia
ctk.set_appearance_mode('dark')

# Criação da janela principal
app = ctk.CTk()
app.title("Finanças")
app.geometry('400x650')

# Nome App
NomeApp = ctk.CTkLabel(app, text="Fin Tech", font=("Arial", 20))
NomeApp.pack(pady=10)

# Criação dos campos
## Frame 1
FrameSuperior = ctk.CTkFrame(app)
FrameSuperior.pack(fill="x", padx=10)

### Tela atual (" Dashboard ")
TelaDashboard = ctk.CTkLabel(FrameSuperior, text="Dashboard")
TelaDashboard.pack(pady=25, padx=25, side="left")

### Botão Adicionar Dinheiro
BotaoAdicionar = ctk.CTkButton(FrameSuperior, text="+", command=lambda: TelaAdicionar(app), width=50,height=50, corner_radius=25, font=("Arial", 20))
BotaoAdicionar.pack(pady=10, padx=25, side="right")

# segundo frame
FrameInferior = ctk.CTkFrame(app)
FrameInferior.pack(fill="x", pady=10)

LabelCategoria = ctk.CTkLabel(FrameInferior, text=f"Categoria: {dados.categoria}")
LabelCategoria.pack(pady=25)

LabelValor = ctk.CTkLabel(FrameInferior, text=f"Valor: R$: {dados.valor}")
LabelValor.pack(pady=25)

def atualizar_labels():
    LabelCategoria.configure(text=f"Categoria: {dados.categoria}")
    LabelValor.configure(text=f"Valor: R$ {dados.valor}")
    app.after(100, atualizar_labels)
atualizar_labels()

# Iniciar o app
app.mainloop()