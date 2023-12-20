from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os

#function to get metadata
def metadata(file_path):
    reader = PdfReader(file_path)
    info = reader.metadata
    print("Author: ",info.author)
    print("Creator: ",info.creator)
    print("Producer: ",info.producer)
    print("Title: ",info.title)
    print("Total no of pages: ",len(reader.pages))
    print(reader.pages[0].extract_text())
def Showinf():
    ask = input("Enter PDf name Case sensitive:")
    file = open(ask+".pdf","rb")
    metadata(file)


#function to extract text from pdf
def extract_text_from_pdf(pdf_path):
    with open(pdf_path,"rb") as f:
        reader = PdfReader(f)
        results = []
        for i in range(0,len(reader.pages)): # prev read.getNumPages()
            selected_page = reader.pages[i]
            text = selected_page.extract_text()
            results.append(text)
        return ' '.join(results) # convert list to a single doc
    
#function to split the pdf Into multiple Pdf pages
def get_pdf_upto(pdf_path,start_page:int=0,stop_page: int = 0):
    with open(pdf_path,"rb") as f:
        
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page,stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page) # prev ::  addPage()
            filename = os.path.splitext(pdf_path)[0]
            output_filename = f"{filename}_from_{start_page+1}_to_{stop_page}.pdf"
        with open(output_filename, "wb") as out:
            writer.write(out)
def Pdf_merger():
    nme1 = input("Enter name of first PDf: ")
    nme2 = input("Enter name of the second pdf: ")
    filem1 = open(nme1+".pdf","rb")
    filem2 = open(nme2+".pdf","rb")
    merger = PdfMerger()
    pdfs = [filem1, filem2]
    for pdf in pdfs:
        merger.append(pdf)
    merger.write('merge result.pdf')
    print('print pdf file merged succesfully')
    merger.close()

def main():
    flag = 0
    while True:
        print("_____________________________________________________________________")
        print("Press 1 to get details of PDF:")
        print("Press 2 to extract text from PDF:")
        print("Press 3 to split the PDF:")
        print("Press 4 to merge the PDF:")
        print("Press 5 to quit")
        print("_____________________________________________________________________")
        flag = int(input("Enter your choice:"))
        if flag == 1:
            Showinf()

        elif flag == 2:
            ext = input("Enter PDf name Case sensitive: ")
            a = extract_text_from_pdf(ext+".pdf")
            print(a)
        elif flag == 3:
            name_pdf = input("Enter PDF Name: ")
            initial_page = int(input("Starting page: "))
            final_page = int(input("Final page: "))       
            get_pdf_upto(name_pdf+".pdf",initial_page-1,final_page)
        elif flag == 4:
            
            Pdf_merger()
        elif flag == 5:
            print("Thanks for Testing.")
            break
def ask():
    while True:
        ask2 = input("Are you have pdf in this directory y/n:")
        if ask2 in "yY":
            main()
            break
        elif ask2 in "nN":
            print("Please move all those pdf you want to handle and run again")
            print("I am waiting for you...")
            break
        else: 
            print("Enter valid input: ")
            continue

print("Welcome to PDF Manager.")
print("-->Please Move the all pdf in working directory that you want to handle")
print("-->Please install module named PyPDF2")
ask()







