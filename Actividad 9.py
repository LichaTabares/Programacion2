import tkinter as tk

def cifCesar(mens,desp):
    res=""
    for i in mens:
        codascii= ord(i)
        ncod=codascii+desp
        if codascii>96 and codascii<123:
            if ncod>122:
                ncod-=26
            elif ncod<97:
                ncod+=26
        res+=chr(ncod)
    return res

def cifrar_texto():
    texto=entrada_texto.get()
    desplazamiento=int(entrada_desp.get())
    resultado=cifCesar(texto,desplazamiento)
    salida.set(resultado)

app= tk.Tk()
app.geometry("300x400")
app.configure(background="cyan")
tk.Wm.wm_title(app, "cifrado Cesar")

entrada_texto=tk.StringVar(app)
entrada_desp=tk.StringVar(app)
salida=tk.StringVar(app)

tk.Label(app, text="ingrese una palabra", font=("Verdana", 16),
         bg="cyan", fg="black").pack(pady=10)
tk.Entry(app, textvariable=entrada_texto, font=("Verdana", 16),
         bg="sky blue", fg="black").pack(pady=10)

tk.Label(app, text="ingresa el desplazamiento:", font=("Verdana", 16),
         bg="cyan", fg="black").pack(pady=10)
tk.Entry(app, textvariable=entrada_desp, font=("Verdana", 16),
         bg="sky blue", fg="black").pack(pady=10)

tk.Button(app, text="cifrar/descifrar", font=("Verdana", 16),
          bg="gray", fg="white",
          command=cifrar_texto).pack(pady=10)

tk.Label(app, text="resultado cifrado", font=("Verdana", 16),
         bg="cyan", fg="black").pack(pady=10)
tk.Label(app, textvariable=salida, font=("Verdana", 16),
         bg="cyan", fg="black").pack(pady=10)

app.mainloop()