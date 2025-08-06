import tkinter as tk
from tkinter import messagebox
from services.api_client import get_pokemon_data
from ui.details_view import DetailsView
import threading
from tkinter import ttk
from services.favorites import load_favorites

def fetch_pokemon_names():
    import requests
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    try:
        resp = requests.get(url)
        results = resp.json()["results"]
        return [p["name"] for p in results]
    except:
        return []

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.is_dark = False

        def toggle_theme():
            self.is_dark = not self.is_dark
            bg = "#222" if self.is_dark else "#f0f8ff"
            fg = "#fff" if self.is_dark else "#333"
            self.root.configure(bg=bg)
            for widget in self.root.winfo_children():
                if isinstance(widget, (tk.Label, tk.Button, ttk.Combobox, tk.Listbox)):
                    widget.configure(bg=bg, fg=fg)
        theme_btn = tk.Button(self.root, text="🌙 Tema Escuro", command=toggle_theme,
                              bg="#333", fg="#fff", font=("Segoe UI", 9))
        theme_btn.pack(pady=5)

        self.root.title("📘 Pokédex")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f8ff")  # fundo azul claro

        # Título principal
        title = tk.Label(self.root, text="Pokédex Desktop", font=("Segoe UI", 16, "bold"),
                         fg="#333", bg="#f0f8ff")
        title.pack(pady=(20, 10))

        # Subtítulo
        subtitle = tk.Label(self.root, text="Digite o nome do Pokémon:",
                            font=("Segoe UI", 11), bg="#f0f8ff")
        subtitle.pack(pady=5)

        # Campo de entrada com autocompletar
        self.pokemon_names = []
        self.entry = ttk.Combobox(self.root, font=("Segoe UI", 12), width=25)
        self.entry.pack(pady=10)
        def load_names():
            self.pokemon_names = fetch_pokemon_names()
            self.entry["values"] = self.pokemon_names
        threading.Thread(target=load_names, daemon=True).start()

        # Botão de busca
        self.search_button = tk.Button(self.root, text="🔍 Buscar",
                                       command=self.search_pokemon,
                                       bg="#4CAF50", fg="white",
                                       font=("Segoe UI", 11, "bold"),
                                       activebackground="#45a049",
                                       padx=12, pady=6, relief="flat")
        self.search_button.pack(pady=10)

        # Lista de favoritos
        fav_label = tk.Label(self.root, text="Favoritos:", font=("Segoe UI", 11, "bold"), bg="#f0f8ff", fg="#333")
        fav_label.pack(pady=(10, 0))
        self.fav_listbox = tk.Listbox(self.root, font=("Segoe UI", 11), width=25, height=5)
        self.fav_listbox.pack(pady=5)
        self.fav_listbox.bind("<Double-Button-1>", self.open_selected_favorite)
        self.update_fav_listbox()

        # Créditos ou rodapé
        footer = tk.Label(self.root, text="by Senac ✨", font=("Segoe UI", 9),
                          bg="#f0f8ff", fg="#999")
        footer.pack(side="bottom", pady=10)

    def search_pokemon(self):
        name = self.entry.get().lower().strip()
        if not name:
            messagebox.showwarning("Aviso", "Digite um nome de Pokémon.")
            return

        data = get_pokemon_data(name)
        if data:
            DetailsView(self.root, data, on_fav_change=self.update_fav_listbox)
        else:
            messagebox.showerror("Erro", "Pokémon não encontrado.")

    def update_fav_listbox(self):
        self.fav_listbox.delete(0, tk.END)
        favs = load_favorites()
        for name in favs:
            self.fav_listbox.insert(tk.END, name.capitalize())

    def open_selected_favorite(self, event):
        selection = self.fav_listbox.curselection()
        if selection:
            name = self.fav_listbox.get(selection[0])
            data = get_pokemon_data(name)
            if data:
                DetailsView(self.root, data, on_fav_change=self.update_fav_listbox)

    def run(self):
        self.root.mainloop()