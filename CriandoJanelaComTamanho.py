import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Minha Aplicação GUI")

# Define o tamanho da janela como 400x300 pixels
root.geometry("400x300")

# Adiciona um widget de rótulo
label = tk.Label(root, text="Olá, Mundo!")
label.pack()

# Executa o loop principal
root.mainloop()
