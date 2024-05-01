import customtkinter
import os

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Get the path to the icon file
ico_path = os.path.join(os.path.dirname(__file__), "yes.ico")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("V-Z-2008")
        self.geometry(f"{770}x{680}")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.entry = customtkinter.CTkButton(self, width=30, height=40)
        self.entry.grid(column=0, row=0, pady=20, padx=30, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
