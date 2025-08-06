import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import requests
from io import BytesIO
from services.favorites import load_favorites, save_favorites

class DetailsView:
    def __init__(self, parent, data, on_fav_change=None):
        self.on_fav_change = on_fav_change
        self.window = Toplevel(parent)
        self.window.title(f"{data['name']} - Detalhes")
        self.window.configure(bg="#f0f8ff")  

        content_frame = tk.Frame(self.window, bg="#f0f8ff")
        content_frame.pack(padx=20, pady=20)

        # --- Imagem e shiny ---
        self.is_shiny = False
        self.poke_id = data.get('id', 0)
        sprite_url = data.get('image_url')
        self.img_label = tk.Label(content_frame, bg="#f0f8ff")
        self.img_label.pack(pady=10)
        self.load_image(sprite_url)

        def toggle_shiny():
            self.is_shiny = not self.is_shiny
            url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
            url += "shiny/" if self.is_shiny else ""
            url += f"{self.poke_id}.png"
            self.load_image(url)
        shiny_button = tk.Button(content_frame, text="Alternar Shiny/Normal", command=toggle_shiny,
                                 bg="#87ceeb", fg="#333", font=("Segoe UI", 10, "bold"))
        shiny_button.pack(pady=5)

        # --- Informações ---
        info_text = f"🧾 Nome: {data['name']}\n"
        info_text += f"📏 Altura: {data['height'] / 10:.1f} m\n"
        info_text += f"⚖️ Peso: {data['weight'] / 10:.1f} kg\n"
        types = ", ".join([t['type']['name'].capitalize() for t in data['types']])
        info_text += f"💥 Tipo(s): {types}\n"
        abilities = ", ".join([a['ability']['name'].capitalize() for a in data['abilities']])
        info_text += f"✨ Habilidades: {abilities}"
        info_label = tk.Label(content_frame, text=info_text, justify="left", bg="#f0f8ff",
                              font=("Segoe UI", 11))
        info_label.pack(pady=10)

        # --- Botão Favoritar ---
        favs = load_favorites()
        is_fav = data['name'].lower() in [f.lower() for f in favs]
        fav_text = "★ Favorito" if is_fav else "☆ Favoritar"
        def toggle_fav():
            favs = load_favorites()
            name = data['name']
            if name not in favs:
                favs.append(name)
            else:
                favs.remove(name)
            save_favorites(favs)
            fav_button.config(text="★ Favorito" if name in favs else "☆ Favoritar")
            if self.on_fav_change:
                self.on_fav_change()
        fav_button = tk.Button(content_frame, text=fav_text, command=toggle_fav,
                               bg="#FFD700", fg="#333", font=("Segoe UI", 10, "bold"))
        fav_button.pack(pady=5)

        # --- Botão Fechar ---
        close_button = tk.Button(content_frame, text="Fechar", command=self.window.destroy,
                                 bg="#ff6961", fg="white", font=("Segoe UI", 10, "bold"),
                                 padx=10, pady=5)
        close_button.pack(pady=10)

    def load_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_data = response.content
            img = Image.open(BytesIO(img_data)).resize((120, 120))
            photo = ImageTk.PhotoImage(img)
            self.window.photo = photo
            self.img_label.config(image=photo, text="")
        except Exception as e:
            self.img_label.config(text=f"Erro ao carregar imagem: {e}", image="")