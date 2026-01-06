import sys
from pypdf import PdfReader, PdfWriter
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
        for page_num in range(start_page - 1, end_page):  # start_page is 1-based, range to end_page inclusive
            writer.add_page(reader.pages[page_num])
        with open(output_pdf, "wb") as f:
            writer.write(f)
        return True, f"Extracted pages {start_page} to {end_page} from {input_pdf} to {output_pdf}"
    except Exception as e:
        return False, str(e)

def browse_input():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, filename)

def browse_output():
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if filename:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, filename)

def run_extraction():
    input_pdf = input_entry.get()
    output_pdf = output_entry.get()
    try:
        start_page = int(start_entry.get())
        end_page = int(end_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid page numbers.")
        return
    success, msg = extract_pages(input_pdf, output_pdf, start_page, end_page)
    if success:
        messagebox.showinfo("Success", msg)
    else:
        messagebox.showerror("Error", msg)

# GUI
root = tk.Tk()
root.title("PDF Page Extractor")

tk.Label(root, text="Input PDF:").grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2)

tk.Label(root, text="Output PDF:").grid(row=1, column=0, sticky="e")
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

tk.Label(root, text="Start Page:").grid(row=2, column=0, sticky="e")
start_entry = tk.Entry(root)
start_entry.grid(row=2, column=1, sticky="w")

tk.Label(root, text="End Page:").grid(row=3, column=0, sticky="e")
end_entry = tk.Entry(root)
end_entry.grid(row=3, column=1, sticky="w")

tk.Button(root, text="Extract Pages", command=run_extraction).grid(row=4, column=1)

root.mainloop()