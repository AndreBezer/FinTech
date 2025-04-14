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

# Frame para o histórico
FrameHistorico = ctk.CTkScrollableFrame(app)
FrameHistorico.pack(fill="both", expand=True, padx=10, pady=10)

def atualizar_historico():
    # Limpa o frame antes de atualizar
    for widget in FrameHistorico.winfo_children():
        widget.destroy()
    
    # Adiciona cada entrada do histórico
    for idx, (categoria, valor) in enumerate(dados.historico, 1):
        entrada_frame = ctk.CTkFrame(FrameHistorico)
        entrada_frame.pack(fill="x", pady=5, padx=5)
        
        ctk.CTkLabel(entrada_frame, text=f"Entrada {idx}:").pack(side="left", padx=5)
        ctk.CTkLabel(entrada_frame, text=f"Categoria: {categoria}").pack(side="left", padx=5)
        ctk.CTkLabel(entrada_frame, text=f"Valor: R$ {valor:.2f}").pack(side="left", padx=5)
    
    # Agenda a próxima atualização
    app.after(1000, atualizar_historico)

# Inicia a atualização do histórico
atualizar_historico()

# Iniciar o app
app.mainloop()