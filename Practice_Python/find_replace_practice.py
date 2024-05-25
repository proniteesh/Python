import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("XML Files", "*.xml"), ("All Files", "*.*")]
    )
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def find_and_replace():
    file_path = file_entry.get()
    find_text = find_entry.get()
    replace_text = replace_entry.get()

    if not file_path or not find_text:
        messagebox.showwarning("Input Error", "Please provide the file location and text to find.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = content.replace(find_text, replace_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        messagebox.showinfo("Success", "Text replaced successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Find and Replace Text in File")

# Create and place the widgets
tk.Label(root, text="File Location:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Find Text:").grid(row=1, column=0, padx=10, pady=10)
find_entry = tk.Entry(root, width=50)
find_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Replace Text:").grid(row=2, column=0, padx=10, pady=10)
replace_entry = tk.Entry(root, width=50)
replace_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Replace", command=find_and_replace).grid(row=3, column=1, pady=20)

# Run the application
root.mainloop()
