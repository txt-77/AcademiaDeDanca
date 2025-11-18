from tkinter import *
from tkinter import messagebox, filedialog, ttk

def salvar_dados(nome, cpf, aula, dia):
    caminho = filedialog.asksaveasfilename(
        title="Salvar inscrição",
        defaultextension=".txt",
        filetypes=[("Arquivo de texto", "*.txt")]
    )

    if not caminho:
        messagebox.showwarning("Cancelado", "O arquivo não foi salvo.")
        return

    with open(caminho, "a") as arq:
        arq.write(f"Nome:{nome} ,CPF:{cpf}; Aula de interesse:{aula} ,Dia da aula:{dia}\n")

    messagebox.showinfo("Sucesso", "Inscrição salva!")
    print("Arquivo salvo em:", caminho)

def mudar_pagina(pag):
    for widget in Body.winfo_children():
        widget.destroy()

    match pag:
        case 1:
            Label(Body, text="Bem-vindo à Academia de Dança!", font=("Arial", 16, "bold"), bg="#d8b7f8").grid(row=0, column=0, pady=20)
        case 2:
            Label(Body, text="Sobre nós", font=("Arial", 16, "bold"), bg="#d8b7f8").grid(row=0, column=0, pady=10)
            Label(Body, text="A dança transforma vidas!", bg="#d8b7f8").grid(row=1, column=0)
        case 3:
            Label(Body, text="Formulário de Inscrição", font=("Arial", 16, "bold"), bg="#d8b7f8").grid(row=0, column=0, columnspan=2, pady=10)

            Label(Body, text="Nome completo:", bg="#d8b7f8").grid(row=1, column=0, sticky="e", padx=5, pady=5)
            nome_entry = Entry(Body, width=30)
            nome_entry.grid(row=1, column=1)

            Label(Body, text="CPF:", bg="#d8b7f8").grid(row=2, column=0, sticky="e", padx=5, pady=5)
            def formatar_cpf(event):
                cpf_text = cpf_entry.get().replace(".", "").replace("-", "")
                if len(cpf_text) == 11:
                    cpf_formatado = f"{cpf_text[:3]}.{cpf_text[3:6]}.{cpf_text[6:9]}-{cpf_text[9:]}"
                    cpf_entry.delete(0, END)
                    cpf_entry.insert(0, cpf_formatado)

            vcmd = root.register(lambda txt: txt.replace(".", "").replace("-", "").isdigit() or txt == "")
            cpf_entry = Entry(Body, width=30, validate="key", validatecommand=(vcmd, "%P"))
            cpf_entry.grid(row=2, column=1)
            cpf_entry.bind("<FocusOut>", formatar_cpf)

            Label(Body, text="Aula de interesse:", bg="#d8b7f8").grid(row=3, column=0, sticky="e", padx=5, pady=5)
            aulas_lista = ["Ballet", "Hip Hop", "Contemporanea"]
            aula_entry = ttk.Combobox(Body, values=aulas_lista, width=27, state="readonly")
            aula_entry.grid(row=3, column=1)

            Label(Body, text="Dia da aula:", bg="#d8b7f8").grid(row=4, column=0, sticky="e", padx=5, pady=5)
            dias_semana = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
            dia_entry = ttk.Combobox(Body, values=dias_semana, width=27, state="readonly")
            dia_entry.grid(row=4, column=1)

            def enviar():
                nome = nome_entry.get()
                cpf = cpf_entry.get()
                aula = aula_entry.get()
                dia = dia_entry.get()

                if not nome or not cpf or not aula or not dia:
                    messagebox.showwarning("Erro", "Preencha todos os campos!")
                    return

                cpf_num = cpf.replace(".", "").replace("-", "")
                if len(cpf_num) != 11:
                    messagebox.showwarning("Erro", "O CPF deve conter 11 dígitos.")
                    return

                salvar_dados(nome, cpf, aula, dia)

                nome_entry.delete(0, END)
                cpf_entry.delete(0, END)
                aula_entry.set("")
                dia_entry.set("")

            Button(Body, text="Enviar", bg="#b491e3", width=10, command=enviar).grid(row=5, column=0, columnspan=2, pady=10)

root = Tk()
root.title("Academia de Dança")
root.geometry("600x400")
root.config(bg="#d8b7f8")

Header = Frame(root, bg="#caa3f5")
Body = Frame(root, bg="#d8b7f8")
Footer = Frame(root, bg="#caa3f5")
Header.grid(row=0, column=0, sticky="ew")
Body.grid(row=1, column=0, sticky="nsew")
Footer.grid(row=2, column=0, sticky="ew")

logo = Label(Header, text="LOGO", bg="#caa3f5", font=("Arial", 12, "bold"))
logo.grid(row=0, column=0, padx=10, pady=5, sticky="w")
sobre = Label(Header, text="Sobre nós", bg="#caa3f5", cursor="hand2")
sobre.grid(row=0, column=1, padx=10)
alugar = Label(Header, text="Alugar aula", bg="#caa3f5", cursor="hand2")
alugar.grid(row=0, column=2, padx=10)

logo.bind("<Button-1>", lambda e: mudar_pagina(1))
sobre.bind("<Button-1>", lambda e: mudar_pagina(2))
alugar.bind("<Button-1>", lambda e: mudar_pagina(3))

mudar_pagina(1)
root.mainloop()