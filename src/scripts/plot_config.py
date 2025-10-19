import matplotlib.pyplot as plt
import seaborn as sns

plot_config= {
        "axes.facecolor": "#fff",     # Cor de fundo dos gráficos
        "axes.spines.top": False,     # Ativar ou remover borda superior
        "axes.spines.right": False,   # Ativar ou remover borda direita
        "axes.grid": False,           # Ativar ou remover grade
        "figure.figsize": (15, 6)     # Tamanho padrão da figura
}

def set_matplotlib():
    plt.rcParams.update(plot_config)

def set_seaborn():
    sns.set_theme(rc= plot_config)
