import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

def add_task():
    task = simpledialog.askstring("Nova Tarefa", "Digite a descrição da tarefa:")
    if task:
        listbox_tasks.insert(tk.END, task)

def remove_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada.")

def edit_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(selected_index)
        new_task = simpledialog.askstring("Editar Tarefa", "Edite a descrição da tarefa:", initialvalue=old_task)
        if new_task:
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, new_task)
    except IndexError:
        messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada.")

def show_help():
    messagebox.showinfo("Ajuda", "Para adicionar uma tarefa, clique em 'Adicionar'.\n"
                                "Para remover uma tarefa, selecione-a e clique em 'Remover'.\n"
                                "Para editar uma tarefa, selecione-a e clique em 'Editar'.")

root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

frame_tasks = tk.Frame(root, bg="#d0e0f0", padx=10, pady=10)
frame_tasks.pack(pady=10, fill=tk.BOTH, expand=True)

frame_buttons = tk.Frame(root, bg="#d0e0f0", padx=10, pady=10)
frame_buttons.pack(pady=10, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectmode=tk.SINGLE, bg="#ffffff", fg="#000000", selectbackground="#add8e6", selectforeground="#000000")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

button_add = tk.Button(frame_buttons, text="Adicionar Tarefa", command=add_task, bg="#4CAF50", fg="#ffffff", font=("Arial", 12, "bold"))
button_add.pack(side=tk.LEFT, padx=5)

button_edit = tk.Button(frame_buttons, text="Editar Tarefa", command=edit_task, bg="#FFC107", fg="#ffffff", font=("Arial", 12, "bold"))
button_edit.pack(side=tk.LEFT, padx=5)

button_remove = tk.Button(frame_buttons, text="Remover Tarefa", command=remove_task, bg="#F44336", fg="#ffffff", font=("Arial", 12, "bold"))
button_remove.pack(side=tk.LEFT, padx=5)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajuda", menu=menu_help)
menu_help.add_command(label="Sobre", command=show_help)

root.mainloop()
