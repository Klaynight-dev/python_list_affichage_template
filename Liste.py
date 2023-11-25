import tkinter as tk

class MaListBox(tk.Tk):
    def __init__(self):
        # Instanciation fenêtre Tk.
        tk.Tk.__init__(self)
        self.listbox = tk.Listbox(self, height=10, width=4)
        self.listbox.pack()
        # Ajout des items à la listbox (entiers).
        for i in range(1, 10+1):
            # Utilisation de ma méthode .insert(index, element)
            # Ajout de l'entier i (tk.END signifie en dernier).
            self.listbox.insert(tk.END, i)
        # Selection du premier élément de listbox.
        self.listbox.select_set(0)
        # Liaison d'une méthode quand clic sur listbox.
        self.listbox.bind("<<ListboxSelect>>", self.clic_listbox)

    def clic_listbox(self, event):
        # Récupération du widget à partir de l'objet event.
        widget = event.widget
        # Récupération du choix sélectionné dans la listbox (tuple).
        # Par exemple renvoie `(5,)` si on a cliqué sur `5`.
        selection = widget.curselection()
        # Récupération du nombre sélectionné (déjà un entier).
        choix_select = widget.get(selection[0])
        # Affichage.
        print(f"Le choix sélectionné est {choix_select}, "
              f"son type est {type(choix_select)}")



if __name__ == "__main__":
    app = MaListBox()
    app.title("MaListBox")
    app.mainloop()
