import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Minha Aplicação GUI")

# Adiciona um widget de rótulo
label = tk.Label(root, text="Olá, Mundo!")
label.pack()

# Executa o loop principal
root.mainloop()
