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
        
        self.slider_1 = customtkinter.CTkSlider(self, from_=0, to=100, number_of_steps=255)
        self.slider_1.set(0)
        self.slider_1.grid(row=0, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")
        
        self.slider_value_label = customtkinter.CTkLabel(self, text =f"Value: ")
        self.slider_value_label.grid(row=2, column=0, padx=(20, 0), pady=(10, 0), sticky="w")        

if __name__ == "__main__":
    app = App()
    app.mainloop()
