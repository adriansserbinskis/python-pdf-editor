import os
import io
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import img2pdf
import PyPDF2
from tkinter import messagebox
from tkinter import filedialog
from pypdf import PdfReader



# Functions=====================================================================

def extract_pages(page_string, total_pages):
    try:
        result_pages = []
        page_ranges = page_string.split(",")

        for page_range in page_ranges:
            start_end = page_range.split("-")

            if len(start_end) == 1:
                page = int(start_end[0])
                result_pages.append(max(1, min(page, total_pages)))
            elif len(start_end) == 2:
                start_page, end_page = map(int, start_end)
                start_page = max(1, min(start_page, total_pages))
                end_page = max(start_page, min(end_page, total_pages))
                result_pages.extend(range(start_page, end_page + 1))

        return result_pages
    except:
        return []

# ==============================================================================


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Editor")
        self.width=500
        self.height=400
        self.geometry("%dx%d+%d+%d" % (self.width, self.height, (self.winfo_screenwidth()-self.width)/2, (self.winfo_screenheight()-self.height)/2))
        self.resizable(width=False, height=False)
        self.style = ttk.Style(self)
        self.style.theme_use("xpnative")

        self.Notebook1 = ttk.Notebook(self)
        self.Tab1 = ttk.Frame(self.Notebook1)
        self.Tab2 = ttk.Frame(self.Notebook1)
        self.Tab3 = ttk.Frame(self.Notebook1)
        self.Tab4 = ttk.Frame(self.Notebook1)

        self.Notebook1.add(self.Tab1, text="Split")
        self.Notebook1.add(self.Tab2, text="Merge")
        self.Notebook1.add(self.Tab3, text="Images to PDF")
        self.Notebook1.add(self.Tab4, text="Extract images")
        self.Notebook1.pack(expand=1, fill="both")

        self.__init_tab1(self.Tab1)
        self.__init_tab2(self.Tab2)
        self.__init_tab3(self.Tab3)
        self.__init_tab4(self.Tab4)

    def __init_tab1(self, tab):
        self.Entry1_text = tk.StringVar()
        self.Entry1 = ttk.Entry(tab, state="readonly", cursor="arrow", textvariable=self.Entry1_text)
        self.Entry1.place(x=20, y=20, width=460, height=25)

        self.Entry2_text = tk.StringVar()
        self.Entry2 = ttk.Entry(tab, textvariable=self.Entry2_text)
        self.Entry2.place(x=20, y=55, width=460, height=25)

        self.Button1 = ttk.Button(tab, text="Split", command=self.Button1_command)
        self.Button1.place(x=50, y=90, width=70, height=25)

        self.Button2 = ttk.Button(tab, text="+", command=self.Button2_command)
        self.Button2.place(x=20, y=90, width=25, height=25)

    def __init_tab2(self, tab):
        self.Listbox1 = ttk.Treeview(tab, show="tree")
        self.Listbox1.place(x=20, y=20, width=460, height=250)
        self.Listbox1.bind("<Delete>", lambda event: self.Listbox_delete(self.Listbox1))

        self.Button3 = ttk.Button(tab, text="Merge", command=self.Button3_command)
        self.Button3.place(x=50, y=280, width=70, height=25)

        self.Button4 = ttk.Button(tab, text="+", command=lambda: self.Listbox_add(self.Listbox1, [("PDF files", "*.pdf")]))
        self.Button4.place(x=20, y=280, width=25, height=25)

    def __init_tab3(self, tab):
        self.Listbox2 = ttk.Treeview(tab, show="tree")
        self.Listbox2.place(x=20, y=20, width=460, height=250)
        self.Listbox2.bind("<Delete>", lambda event: self.Listbox_delete(self.Listbox2))

        self.Button5 = ttk.Button(tab, text="Convert", command=self.Button5_command)
        self.Button5.place(x=50, y=280, width=70, height=25)

        self.Button6 = ttk.Button(tab, text="+", command=lambda: self.Listbox_add(self.Listbox2, [("Image files", "*.png;*.jpeg;*.jpg;*.bmp;*.gif")]))
        self.Button6.place(x=20, y=280, width=25, height=25)

    def __init_tab4(self, tab):
        self.Entry3_text = tk.StringVar()
        self.Entry3 = ttk.Entry(tab, state="readonly", cursor="arrow", textvariable=self.Entry3_text)
        self.Entry3.place(x=20, y=20, width=460, height=25)

        self.Button7 = ttk.Button(tab, text="Extract", command=self.Button8_command)
        self.Button7.place(x=50, y=55, width=70, height=25)

        self.Button8 = ttk.Button(tab, text="+", command=lambda: self.Entry_set(self.Entry3_text, [("PDF files", "*.pdf")]))
        self.Button8.place(x=20, y=55, width=25, height=25)

    def Entry_set(self, entry_text, filetypes):
        filename = fd.askopenfilename(title="Open a file", filetypes=[("PDF files", "*.pdf")])
        entry_text.set(filename)
        return filename

    def Listbox_add(self, listbox, filetypes):
        files = fd.askopenfilenames(title="Open a files", filetypes=filetypes)
        for item in files: listbox.insert("", "end", text=item)

    def Listbox_delete(self, listbox):
        for item in listbox.selection(): listbox.delete(item)

    def Button1_command(self):
        filename = self.Entry1_text.get()
        if (filename == ""): return messagebox.showinfo("Info", "Select pdf file first")
        if (not os.path.exists(filename)): return messagebox.showinfo("Info", "File not found")

        pdf_reader = PyPDF2.PdfReader(open(filename, "rb"))
        pages = extract_pages(self.Entry2_text.get(), len(pdf_reader.pages))
        if (len(pages) == 0): return messagebox.showinfo("Info", "Incorrect range formating")

        filename = fd.asksaveasfile(title="Save a file", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]).name
        if (filename == ""): return

        pdf_writer = PyPDF2.PdfWriter()
        for index in pages: pdf_writer.add_page(pdf_reader.pages[index-1])
        with open(filename, "wb") as out: pdf_writer.write(out)
        messagebox.showinfo("Info", "Split successful")

    def Button2_command(self):
        filename = self.Entry_set(self.Entry1_text, [("PDF files", "*.pdf")])
        if (filename == ""): return
        pdf_file = PyPDF2.PdfReader(open(filename, "rb"))
        self.Entry2_text.set(f"{1}-{len(pdf_file.pages)}")

    def Button3_command(self):
        try:
            selected_items = self.Listbox1.get_children()
            if not selected_items: return messagebox.showinfo("Info", "No files selected for merging")
            out_filename = fd.asksaveasfile(title="Save a file", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]).name
            if (out_filename == ""): return
            pdf_writer = PyPDF2.PdfWriter()

            for item in selected_items:
                file_path = self.Listbox1.item(item, "text")
                pdf_reader = PyPDF2.PdfReader(open(file_path, "rb"))
                for page in pdf_reader.pages: pdf_writer.add_page(page)

            with open(out_filename, "wb") as out: pdf_writer.write(out)
            messagebox.showinfo("Info", "Merging successful")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error merging files: {str(e)}")

    def Button5_command(self):
        try:
            selected_items = self.Listbox2.get_children()
            if not selected_items: return messagebox.showinfo("Info", "No files selected for converting")
            out_filename = fd.asksaveasfile(title="Save a file", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]).name
            if (out_filename == ""): return
            pdf_writer = PyPDF2.PdfWriter()

            for item in selected_items:
                file_path = self.Listbox2.item(item, "text")
                pdf_data = img2pdf.convert(file_path)
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_data))
                for page in pdf_reader.pages: pdf_writer.add_page(page)

            with open(out_filename, "wb") as out: pdf_writer.write(out)
            messagebox.showinfo("Info", "Converting successful")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error converting files: {str(e)}")

    def Button8_command(self):
        filename = self.Entry3_text.get()
        if (filename == ""): return messagebox.showinfo("Info", "Select pdf file first")
        if (not os.path.exists(filename)): return messagebox.showinfo("Info", "File not found")

        directory = filedialog.askdirectory()
        if (directory == ""): return
        pdf_reader = PdfReader(filename)

        for pc, page in enumerate(pdf_reader.pages, start=0):
            for ic, image_object in enumerate(page.images, start=0):
                with open(f"{directory}/{os.path.basename(filename)}_{pc+1}_{ic+1}_{image_object.name}", "wb") as file:
                    file.write(image_object.data)

        messagebox.showinfo("Info", "Extract successful")


# Main loop=====================================================================


if __name__ == "__main__":
    app = App()
    app.mainloop()
