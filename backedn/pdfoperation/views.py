from django.shortcuts import render
import subprocess
import os.path
import sys
from shutil import copyfile
import pdfx
from PyPDF2 import PdfMerger
import io
from PIL import Image   
import fitz
import pdfplumber
import docx
# Create your views here.
def compress(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: input file is not a PDF")
        sys.exit(1)

    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[power]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done.")

def getreference(request):
    pdf = pdfx.PDFx("82.ChangingApproachesinCampusPlacement.pdf")
    metadata = pdf.get_metadata()
    references_list = pdf.get_references()
    references_dict = pdf.get_references_as_dict()
    print(references_dict)
    pdf.download_pdfs("target-directory")
    
def mergepdf(request):
    pdfs = ['1.pdf', '2.pdf']

    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()
    
def extractimage(request):
        # file path you want to extract images from
    file = "C:\\Users\\AYUSH SHUKLA\\Desktop\\optimizedhtr\\pdfoperation\\PDF_Published.pdf"

    # open the file
    pdf_file = fitz.open(file)

    # iterate over PDF pages
    for page_index in range(len(pdf_file)):

        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()

        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.get_images(), start=1):
            # get the XREF of the image
            xref = img[0]

            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]

            # get the image extension
            image_ext = base_image["ext"]

            img = Image.open(io.BytesIO(image_bytes))
            img.save(open(f"image{page_index + 1}_{image_index}.{image_ext}", "wb"))    

def pdftoword(request):


    # Open PDF file and extract text with pdfplumber
    with pdfplumber.open('plagarisimdetectionofimages.pdf') as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Create a Word document with docx
    doc = docx.Document()

    # Add text to the Word document with formatting and alignment
    for line in text.split('\n'):
        if line.strip():
            # Check if the line is centered
            if line.center(len(line)).strip() == line.strip():
                p = doc.add_paragraph(line)
            # Check if the line is right-aligned
            elif line.rstrip() == line.strip():
                p = doc.add_paragraph(line, style='Right')
            # Otherwise, add the line as left-aligned
            else:
                p = doc.add_paragraph(line)

    # Save the Word document
    doc.save('example1.docx')
