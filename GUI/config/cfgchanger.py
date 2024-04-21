import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class AppConfigWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Insert your config")
        
        # Style
        style = ttk.Style(self)
        style.theme_use("clam")

        # Dark mode colors
        self.configure(bg="#202020")  # Set background color
        style.configure(".", background="#202020", foreground="#FFFFFF", fieldbackground="#303030")  # Set widget colors

        # Create a text entry field
        self.text_entry = tk.Text(self, width=50, height=10, bg="#303030", fg="#FFFFFF")
        self.text_entry.pack(pady=10)

        # Create a button to choose a text file
        choose_button = ttk.Button(self, text="Choose Config", command=self.choose_file, style="DarkButton.TButton")
        choose_button.pack(pady=5)

        # Create a button to insert text
        insert_button = ttk.Button(self, text="Insert Config", command=self.insert_text, style="DarkButton.TButton")
        insert_button.pack(pady=5)

        # Define custom style for buttons
        style.configure("DarkButton.TButton", background="#404040", foreground="#FFFFFF", bordercolor="#303030")
    
    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                text = f.read()
                self.text_entry.delete('1.0', tk.END)  # Clear current text
                self.text_entry.insert(tk.END, text)

    def insert_text(self):
        text = self.text_entry.get('1.0', tk.END)
        save_to_json(text)
        self.destroy()  # Close the window after inserting text

def save_to_json(text):
    with open("test.json", "w") as f:
        f.write(text)
    print("\033[31mupdated settings\033[0m")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main App")

        # Create a button to open the AppConfigWindow
        self.open_config_button = ttk.Button(self, text="Open Config Window", command=self.open_config_window)
        self.open_config_button.pack(pady=10)

    def open_config_window(self):
        config_window = AppConfigWindow(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
