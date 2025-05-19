import os
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

class PDFMerger:
    def __init__(self, input_folder='inputs', output_folder='outputs'):
        """
        Initializes the PDFMerger class with specified input and output folders.

        Args:
            input_folder (str): Folder where input PDF files are stored.
            output_folder (str): Folder where output PDF files will be saved.
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.writer = PdfWriter()

        # Ensure the folders exist
        os.makedirs(self.input_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)

    def merge_pdfs(self, pdf_files, output_file_name='merged_output.pdf'):
        """
        Merges the PDFs in the input folder and writes them to the output folder.

        Args:
            pdf_files (list): A list of PDF filenames (inside the input folder) to be merged.
            output_file_name (str): The name of the output merged PDF file.
        """
        # Process each PDF file in the specified order
        for pdf_file in pdf_files:
            file_path = os.path.join(self.input_folder, pdf_file)
            reader = PdfReader(file_path)
            for page in range(len(reader.pages)):
                self.writer.add_page(reader.pages[page])

        # Save the merged PDF in the output folder
        output_path = os.path.join(self.output_folder, output_file_name)
        with open(output_path, 'wb') as out_file:
            self.writer.write(out_file)

        print(f"Merged PDF saved as '{output_path}'")

# Example usage
pdf_merger = PDFMerger()
pdf_files = ["Allianz_annual_2024.pdf"]  # Place these PDFs in the 'inputs' folder
pdf_merger.merge_pdfs(pdf_files, 'merged_output.pdf')
