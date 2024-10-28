import random
from tkinter import messagebox
from tkinter import *
import tkinter as tk

janela = tk.Tk()
janela.title("Amor da Vivi❤")
janela.geometry("600x600")
janela.configure(background="#ffc8dd")
    
def destruir():
    messagebox.showinfo("Não fale com eu", "Você nãããããõoo ama euuuu!!!!!")
    janela.destroy()
    
def mover(e):
    if abs(e.x - botao_destruir.winfo_x()) < 50 and abs(e.y - botao_destruir.winfo_y()) < 40:
        x = random.randint(0, janela.winfo_width() - botao_destruir.winfo_width())
        y = random.randint(0, janela.winfo_height() - botao_destruir.winfo_height())
        botao_destruir.place(x=x, y=y)
    
def botao_certo():
    messagebox.showinfo("Amor da momo!", "Ebbbbaaaaaaa Momo me amaaaaaaa!!!!")

margem = Canvas(janela, width=500, bg="#ffc8dd", height=100,
                bd=0, highlightthickness=0, relief='ridge')
margem.pack()

texto = Label(janela, background="#ffc8dd", text="O quanto você ama eu momo???",
              foreground="#590d22", font=("Montserrat", 24, "bold"))
texto.pack(pady=10)

botao_destruir = tk.Button(janela, text="Muito pouquinho", background="#ffb3c1", font=("Montserrat", 15, "bold"),
                relief=RIDGE, command=destruir, border=3)
botao_destruir.pack(pady=10)
janela.bind('<Motion>', mover)

botao_mensagem = tk.Button(janela, text="Amoooo muuiiitooooo!!!", background="#ffb3c1", font=("Montserrat", 15, "bold"),
                relief=RIDGE, command=botao_certo, border=3)
botao_mensagem.pack(pady=5)


janela.mainloop()