import PyPDF2

def encrypt_pdf(input_pdf, output_pdf, password):
    # Open the input PDF file in binary mode
    with open(input_pdf, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add pages from the input PDF to the writer object
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Encrypt the PDF with the provided password
        pdf_writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f'Encryption successful. Encrypted PDF saved to {output_pdf}')

ask1 = input("Enter PDF Name: ")
input_pdf_file = ask1 +".pdf"
output_pdf_file = ask1 + "(Encrypted)"+".pdf"
ask2 = input("Enter password for pdf: ")
password = ask2

encrypt_pdf(input_pdf_file, output_pdf_file, password)
