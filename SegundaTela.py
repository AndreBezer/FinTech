import customtkinter as ctk

class Dados:
    def __init__(self):
        self.historico = []
        self.categoria = ""
        self.valor = 0.0
    
    def adicionar_entrada(self, categoria, valor):
        self.categoria = categoria
        self.valor = valor
        self.historico.append((categoria, valor))

dados = Dados()

def TelaAdicionar(janela_principal):
    janela_adicionar = ctk.CTkToplevel(janela_principal)
    janela_adicionar.title("Adicionar valor")
    janela_adicionar.geometry("300x400")
    janela_adicionar.resizable(False, False)
    janela_adicionar.grab_set()

    ctk.CTkLabel(janela_adicionar, text="Adicionar Entrada", font=("Arial", 16)).pack(pady=20)

    frame_campos = ctk.CTkFrame(janela_adicionar)
    frame_campos.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(frame_campos, text="Valor:").pack()
    entrada_valor = ctk.CTkEntry(frame_campos, placeholder_text="R$0.00")
    entrada_valor.pack(pady=5, fill="x")

    ctk.CTkLabel(frame_campos, text="Categoria:").pack()
    opcoes_categoria = ["Salario", "Alimentação", "Transporte", "Lazer", "Outros"]
    combobox_categoria = ctk.CTkComboBox(frame_campos, values=opcoes_categoria)
    combobox_categoria.pack(pady=5, fill="x")

    def adicionar():
        try:
            valor = float(entrada_valor.get())
            categoria = combobox_categoria.get()

            if valor <= 0:
                raise ValueError("O valor deve ser positivo")
            if not categoria:
                raise ValueError("Selecione uma categoria")
            
            dados.adicionar_entrada(categoria, valor)
            janela_adicionar.destroy()

        except ValueError as e:
            if not hasattr(janela_adicionar, "label_erro"):
                janela_adicionar.label_erro = ctk.VTkLabel(janela_adicionar, text="", text_color="red")
                janela_adicionar.label_erro.pack(pady=5)
            janela_adicionar.label_erro.configure(text=f"Erro: {str(e)}")

    ctk.CTkButton(
        janela_adicionar, 
        text="Adicionar", 
        command=adicionar,
        height=40,
        font=("Arial", 14)
    ).pack(pady=20, padx=20, fill="x")

    ctk.CTkButton(
        janela_adicionar,
        text="Cancelar",
        command=janela_adicionar.destroy,
        height=40,
        font=("Arial", 14),
        fg_color="transparent",
        border_width=1,
        text_color=("gray10", "gray90")
    ).pack(pady=10, padx=20, fill="x")