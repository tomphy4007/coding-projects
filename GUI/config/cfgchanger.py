import tkinter as tk
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
            text_entry.delete(0, tk.END)  # Clear current text
            text_entry.insert(tk.END, text)

def insert_text():
    text = text_entry.get()
    save_to_json(text)

# Create the main window
root = tk.Tk()
root.title("Text to JSON")

# Create a text entry field
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Create a button to choose a text file
choose_button = tk.Button(root, text="Choose Text File", command=choose_file)
choose_button.pack(pady=5)

# Create a button to insert text
insert_button = tk.Button(root, text="Insert Text", command=insert_text)
insert_button.pack(pady=5)

# Run the application
root.mainloop()
