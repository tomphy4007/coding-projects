import customtkinter as ctk
from tkinter import filedialog

def save_to_json(text):
    with open("test.json", "w") as f:
        f.write(text)
    print("Text saved to test.json")

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            text = f.read()
            text_field.delete('1.0', ctk.END)  # Clear current text
            text_field.insert(ctk.END, text)  # Insert text from the file

def insert_text():
    text = text_field.get('1.0', ctk.END)  # Get all text from the CTkTextField
    save_to_json(text)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
  
        # configure window
        self.title("insert config")
        self.geometry("300x150")
        
        self.text_field = ctk.CTkInputDialog(self, width=50, height=10)  # Use CTkTextField instead of CTkEntry
        self.text_field.pack(pady=10)
        
        self.choose_button = ctk.CTkButton(self, text="Choose Text File", command=choose_file)
        self.choose_button.pack(pady=5)
        
        self.insert_button = ctk.CTkButton(self, text="Insert Text", command=insert_text)
        self.insert_button.pack(pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()
