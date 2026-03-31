from pypdf import PdfReader

def extractpdf(pdf_doc): # module to load and extract text from the pdf
    try:
        pdf = PdfReader(pdf_doc)  # load pdf_doc
         raw_text= ''
         for index,page in enumerate(pdf.pages):
             text=page.extract_text()
             if text:
                 raw_text += text
        return raw_text
    except Exception as e:
        return f"Error in reading the pdf"
    
    
        text