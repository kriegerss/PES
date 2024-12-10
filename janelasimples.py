import tkinter as tk
print("a extenção está instalada e funcionando!")

def clique_botao():
    texto_label.config(text="Botão clicado!", fg="blue")

janela= tk.Tk()
janela.title= "janela simples"
janela.geometry=("300x300")

texto_label = tk.Label(janela, text="Olá! Bem-vindo!", font=("Arial", 14), fg="red")
texto_label.pack(pady=10) 


botao = tk.Button(janela, text="Clique Aqui", command=clique_botao, bg="yellow", fg="black")
botao.pack(pady=10)


janela.mainloop()