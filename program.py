import customtkinter as ctk

# Configuração da aparencia
ctk.set_appearance_mode('dark')

def adicionarDinheiro():
    print("funcionou")

# Criação da janela principal
app = ctk.CTk()
app.title("Finanças")
app.geometry('400x650')

# Nome App
NomeApp = ctk.CTkLabel(app, text="Fin Tech")
NomeApp.pack(pady=10, anchor="w", padx=10)

# Criação dos campos
## Frame 1
FrameSuperior = ctk.CTkFrame(app)
FrameSuperior.pack(fill="x", padx=10, pady=10)

### Tela atual (" Dashboard ")
TelaDashboard = ctk.CTkLabel(FrameSuperior, text="Dashboard")
TelaDashboard.pack(pady=25, padx=25, side="left")

### Botão Adicionar Dinheiro
BotaoAdicionar = ctk.CTkButton(FrameSuperior, text="+", command=adicionarDinheiro, width=50,height=50, corner_radius=25, font=("Arial", 20))
BotaoAdicionar.pack(pady=10, padx=25, side="right")

#entry
#label
#entry
#button

# Iniciar o app
app.mainloop()