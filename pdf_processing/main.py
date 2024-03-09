import fitz  # PyMuPDF
import os

def extract_table_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    tables = []
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text = page.get_text()
        lines = text.split("\n")
        table_start = False
        table = []
        for line in lines:
            if line.startswith("Key: Value"):
                table_start = True
                continue
            if table_start:
                key, value = line.split(":", 1)  
                table.append({"key": key.strip(), "value": value.strip()})
        if table:
            tables.append(table)
    pdf_document.close()
    return tables

if __name__ == "__main__":
    pdf_path = r"C:\Users\pvtru\Downloads\Invoice-INV-1.pdf"
    extracted_tables = extract_table_from_pdf(pdf_path)
    for table in extracted_tables:
        print(table)
