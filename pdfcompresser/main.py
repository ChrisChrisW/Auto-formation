import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfFileReader, PdfFileWriter

class PDFCompressor:
    def compress_pdf(self, input_path, output_path):
        pdf_reader = PdfFileReader(input_path)
        pdf_writer = PdfFileWriter()

        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.compressContentStreams()
            pdf_writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

class PDFMerger:
    def merge_pdfs(self, input_paths, output_path):
        pdf_writer = PdfFileWriter()

        for path in input_paths:
            pdf_reader = PdfFileReader(path)
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

class PDFToolApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Compression et fusion de fichiers PDF")

        self.file_list = tk.Listbox(self.window, width=50)
        self.file_list.pack(pady=10)

        scrollbar = tk.Scrollbar(self.window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_list.yview)

        select_button = tk.Button(self.window, text="Sélectionner les fichiers", command=self.select_files)
        select_button.pack(pady=10)

        compress_button = tk.Button(self.window, text="Compresser les fichiers sélectionnés", command=self.compress_selected)
        compress_button.pack(pady=5)

        merge_button = tk.Button(self.window, text="Fusionner les fichiers sélectionnés", command=self.merge_selected)
        merge_button.pack(pady=5)

        self.pdf_compressor = PDFCompressor()
        self.pdf_merger = PDFMerger()

        self.window.mainloop()

    def select_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if file_paths:
            self.file_list.delete(0, tk.END)
            for path in file_paths:
                self.file_list.insert(tk.END, path)

    def compress_selected(self):
        selected_files = self.file_list.curselection()
        if selected_files:
            for index in selected_files:
                input_file = self.file_list.get(index)
                output_file = input_file[:-4] + "_compressed.pdf"
                self.pdf_compressor.compress_pdf(input_file, output_file)
            messagebox.showinfo("Compression terminée", "La compression des fichiers sélectionnés est terminée.")

    def merge_selected(self):
        selected_files = self.file_list.curselection()
        if selected_files:
            input_files = [self.file_list.get(index) for index in selected_files]
            output_file = "merged.pdf"
            self.pdf_merger.merge_pdfs(input_files, output_file)
            messagebox.showinfo("Fusion terminée", "La fusion des fichiers sélectionnés est terminée.")

# Instantiation de la classe PDFToolApp
pdf_tool_app = PDFToolApp()
