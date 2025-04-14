import customtkinter as ctk

ctk.set_appearance_mode('dark')

class DadosSalvos:
    valor = ""
    categoria = ""

dados = DadosSalvos()

def salvar():
    global inserir_valor, combo
    dados.valor = inserir_valor.get()
    dados.categoria = combo.get()
    print(f"{dados.valor}, {dados.categoria}")

def TelaAdicionar(janela_principal):
    global inserir_valor, combo

    modal = ctk.CTkToplevel(janela_principal)
    modal.title("Adicionar Dinheiro")
    modal.geometry("300x300")
    modal.resizable(False, False)
    modal.grab_set()

    FrameSuperiorSegundaTela = ctk.CTkFrame(modal)
    FrameSuperiorSegundaTela.pack(fill="both", expand=True, padx=10, pady=10)

    # Nome dashboard
    dashboard = ctk.CTkLabel(FrameSuperiorSegundaTela, text="dashboard")
    dashboard.pack(pady=25, padx=25)

    inserir_valor = ctk.CTkEntry(FrameSuperiorSegundaTela, placeholder_text="Digite o valor")
    inserir_valor.pack(pady=10)

    combo = ctk.CTkComboBox(
        FrameSuperiorSegundaTela,
        values=["Salario", "Investimento", "Saque"],
        state="readonly",
        dropdown_hover_color="lightblue",
    )
    combo.pack(pady=10)

    BotaoAdicionar2 = ctk.CTkButton(FrameSuperiorSegundaTela,
        text="Adicionar",
        command=salvar,
        width=50,
        height=50,
        corner_radius=25,
        font=("Arial", 20)
        )
    BotaoAdicionar2.pack(pady=10)