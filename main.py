import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Criar a janela principal
root = tk.Tk()
root.title("Digital Soul Application Analytic System")

# Variável para a configuração "Goffi"
goffi_enabled = tk.BooleanVar(value=False)

# Dados das contas como variáveis
accounts_ofc = [
    {"name": "OFC_1", "followers": 1200, "views": 3400, "links": 45, "comments": 67},
    {"name": "OFC_2", "followers": 980, "views": 2900, "links": 32, "comments": 54},
    {"name": "OFC_3", "followers": 1500, "views": 4100, "links": 56, "comments": 78},
    {"name": "OFC_4", "followers": 2100, "views": 5000, "links": 67, "comments": 89},
    {"name": "OFC_5", "followers": 1800, "views": 4300, "links": 52, "comments": 65},
]

accounts_fks = [
    {"name": "FKS_1", "followers": 800, "views": 2300, "links": 22, "comments": 45},
    {"name": "FKS_2", "followers": 1100, "views": 3200, "links": 34, "comments": 57},
    {"name": "FKS_3", "followers": 1400, "views": 3700, "links": 41, "comments": 61},
    {"name": "FKS_4", "followers": 1600, "views": 4200, "links": 49, "comments": 69},
    {"name": "FKS_5", "followers": 1900, "views": 4600, "links": 54, "comments": 74},
]

# Função para definir tema escuro básico
def set_dark_theme():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background="#333333")
    style.configure("TLabel", background="#333333", foreground="white", font=("Helvetica", 12))
    style.configure("TButton", background="#444444", foreground="white", font=("Helvetica", 12), padding=10)
    style.map("TButton",
              background=[("active", "#555555")],
              foreground=[("active", "white")])
    style.configure("TRadiobutton", background="#333333", foreground="white", font=("Helvetica", 12))

# Função para calcular totais
def calculate_totals(accounts):
    total_followers = sum(acc["followers"] for acc in accounts)
    total_views = sum(acc["views"] for acc in accounts)
    total_links = sum(acc["links"] for acc in accounts)
    total_comments = sum(acc["comments"] for acc in accounts)
    return total_followers, total_views, total_links, total_comments

# Função para criar a interface do grupo
def create_group_interface(frame, group_name, accounts):
    group_label = ttk.Label(frame, text=group_name, font=('Helvetica', 16, 'bold'))
    group_label.pack(pady=10)

    for account in accounts:
        account_frame = ttk.Frame(frame, padding="5 5 5 5", relief=tk.RIDGE)
        account_frame.pack(fill='x', pady=5)

        name_label = ttk.Label(account_frame, text=f"Conta: {account['name']}", font=('Helvetica', 12))
        name_label.grid(column=0, row=0, sticky='w', padx=5, pady=2)

        followers_label = ttk.Label(account_frame, text=f"Seguidores: {account['followers']}", font=('Helvetica', 10))
        followers_label.grid(column=1, row=0, sticky='w', padx=5, pady=2)

        views_label = ttk.Label(account_frame, text=f"Views: {account['views']}", font=('Helvetica', 10))
        views_label.grid(column=2, row=0, sticky='w', padx=5, pady=2)

        links_label = ttk.Label(account_frame, text=f"Links: {account['links']}", font=('Helvetica', 10))
        links_label.grid(column=3, row=0, sticky='w', padx=5, pady=2)

        comments_label = ttk.Label(account_frame, text=f"Comentários: {account['comments']}", font=('Helvetica', 10))
        comments_label.grid(column=4, row=0, sticky='w', padx=5, pady=2)

    totals = calculate_totals(accounts)
    total_label = ttk.Label(frame, text=f"Total - Seguidores: {totals[0]}, Views: {totals[1]}, Links: {totals[2]}, Comentários: {totals[3]}")
    total_label.pack(pady=10)

# Função para criar gráficos básicos
def create_charts():
    window = tk.Toplevel(root)
    window.title("Análise de Dados")

    sns.set(style="whitegrid")  # Estilo seaborn

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Gráfico de barras - Seguidores
    accounts = [acc['name'] for acc in accounts_ofc + accounts_fks]
    followers = [acc['followers'] for acc in accounts_ofc + accounts_fks]
    sns.barplot(x=range(len(accounts)), y=followers, ax=axs[0, 0], palette="Blues_d")
    axs[0, 0].set_title('Seguidores')
    axs[0, 0].set(xlabel=None)  # Remover o rótulo do eixo x
    axs[0, 0].set_xticklabels([])  # Remover os rótulos do eixo x

    # Gráfico de barras - Views
    views = [acc['views'] for acc in accounts_ofc + accounts_fks]
    sns.barplot(x=range(len(accounts)), y=views, ax=axs[0, 1], palette="Greens_d")
    axs[0, 1].set_title('Views')
    axs[0, 1].set(xlabel=None)  # Remover o rótulo do eixo x
    axs[0, 1].set_xticklabels([])  # Remover os rótulos do eixo x

    # Gráfico de barras - Links
    links = [acc['links'] for acc in accounts_ofc + accounts_fks]
    sns.barplot(x=range(len(accounts)), y=links, ax=axs[1, 0], palette="Reds_d")
    axs[1, 0].set_title('Links')
    axs[1, 0].set(xlabel=None)  # Remover o rótulo do eixo x
    axs[1, 0].set_xticklabels([])  # Remover os rótulos do eixo x

    # Gráfico de barras - Comentários
    comments = [acc['comments'] for acc in accounts_ofc + accounts_fks]
    sns.barplot(x=range(len(accounts)), y=comments, ax=axs[1, 1], palette="Purples_d")
    axs[1, 1].set_title('Comentários')
    axs[1, 1].set(xlabel=None)  # Remover o rótulo do eixo x
    axs[1, 1].set_xticklabels([])  # Remover os rótulos do eixo x

    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Função para analisar OFC vs FKS
def analyze_ofc_vs_fks():
        window = tk.Toplevel(root)
        window.title("Análise OFC X FKS")

        sns.set(style="whitegrid")  # Estilo seaborn

        totals_ofc = calculate_totals(accounts_ofc)
        totals_fks = calculate_totals(accounts_fks)

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # Gráfico de pizza - Seguidores
        labels = ['OFC', 'FKS']
        sizes = [totals_ofc[0], totals_fks[0]]
        colors = ['blue', 'green']
        explode = (0.1, 0)  # Explodir a fatia OFC para destaque
        wedges, texts, autotexts = axs[0, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
        axs[0, 0].set_title('Total de Seguidores\nTotal: {}'.format(sum(sizes)))
        for i, text in enumerate(autotexts):
            text.set_color('black')
            text.set_fontsize(10)
        axs[0, 0].legend(wedges, [f'{labels[i]}: {sizes[i]}' for i in range(len(labels))], loc="center", bbox_to_anchor=(0.5, 0.5))

        # Gráfico de pizza - Views
        sizes = [totals_ofc[1], totals_fks[1]]
        wedges, texts, autotexts = axs[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
        axs[0, 1].set_title('Total de Views\nTotal: {}'.format(sum(sizes)))
        for i, text in enumerate(autotexts):
            text.set_color('black')
            text.set_fontsize(10)
        axs[0, 1].legend(wedges, [f'{labels[i]}: {sizes[i]}' for i in range(len(labels))], loc="center", bbox_to_anchor=(0.5, 0.5))

        # Gráfico de pizza - Links
        sizes = [totals_ofc[2], totals_fks[2]]
        wedges, texts, autotexts = axs[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
        axs[1, 0].set_title('Total de Links\nTotal: {}'.format(sum(sizes)))
        for i, text in enumerate(autotexts):
            text.set_color('black')
            text.set_fontsize(10)
        axs[1, 0].legend(wedges, [f'{labels[i]}: {sizes[i]}' for i in range(len(labels))], loc="center", bbox_to_anchor=(0.5, 0.5))

        # Gráfico de pizza - Comentários
        sizes = [totals_ofc[3], totals_fks[3]]
        wedges, texts, autotexts = axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
        axs[1, 1].set_title('Total de Comentários\nTotal: {}'.format(sum(sizes)))
        for i, text in enumerate(autotexts):
            text.set_color('black')
            text.set_fontsize(10)
        axs[1, 1].legend(wedges, [f'{labels[i]}: {sizes[i]}' for i in range(len(labels))], loc="center", bbox_to_anchor=(0.5, 0.5))

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack()
        canvas.draw()

# Função para abrir a tela de configuração
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Configuração")

    settings_frame = ttk.Frame(settings_window, padding="10 10 10 10")
    settings_frame.pack(fill='both', expand=True)

    goffi_label = ttk.Label(settings_frame, text="Ativar Goffi", font=('Helvetica', 12))
    goffi_label.pack(side='left', padx=10, pady=10)

    goffi_checkbox = ttk.Checkbutton(settings_frame, variable=goffi_enabled, onvalue=True, offvalue=False)
    goffi_checkbox.pack(side='left', padx=10, pady=10)



# Definir tema escuro
set_dark_theme()

# Criar o frame principal
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill='both', expand=True)

# Criar o cabeçalho
header = ttk.Label(main_frame, text="Digital Soul Application Analytic System", font=("Helvetica", 20, "bold"))
header.pack(pady=20)

# Criar frames para cada grupo
groups_frame = ttk.Frame(main_frame)
groups_frame.pack(fill='both', expand=True)

ofc_frame = ttk.Frame(groups_frame, padding="10 10 10 10", relief=tk.RIDGE)
ofc_frame.pack(side='left', fill='both', expand=True)

fks_frame = ttk.Frame(groups_frame, padding="10 10 10 10", relief=tk.RIDGE)
fks_frame.pack(side='right', fill='both', expand=True)

# Adicionar as interfaces dos grupos
create_group_interface(ofc_frame, "Grupo OFC", accounts_ofc)
create_group_interface(fks_frame, "Grupo FKS", accounts_fks)

# Criar o rodapé com os botões
footer = ttk.Frame(main_frame)
footer.pack(pady=20)

# Botão para abrir a análise de dados
analyze_button = ttk.Button(footer, text="Analisar Dados", command=create_charts)
analyze_button.pack(side="left", padx=20)

# Botão para abrir a análise OFC vs FKS
compare_button = ttk.Button(footer, text="Analisar OFC X FKS", command=analyze_ofc_vs_fks)
compare_button.pack(side="left", padx=20)

# Botão para abrir a tela de configuração
settings_button = ttk.Button(footer, text="Configuração", command=open_settings)
settings_button.pack(side="right", padx=20)

# Executar a interface gráfica
root.mainloop()
