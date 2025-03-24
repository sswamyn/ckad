# Program to convert PDF slides to PowerPoint slides

import os
import sys
import glob
import shutil
import subprocess
import argparse


def convertPDFtoPPT(pdfFile, pptFile):
    # Convert PDF slides to PowerPoint slides
    # pdfFile: PDF file name
    # pptFile: PowerPoint file name

    # Check if the PDF file exists
    if not os.path.exists(pdfFile):
        print("Error: PDF file %s does not exist" % pdfFile)
        return

    # Check if the PowerPoint file exists
    if os.path.exists(pptFile):
        print("Error: PowerPoint file %s already exists" % pptFile)
        return

    # Convert PDF slides to PowerPoint slides
    print("Converting PDF slides to PowerPoint slides")
    command = "unoconv -f ppt %s" % pdfFile
    subprocess.call(command, shell=True)

    # Rename the converted file to the specified PowerPoint file
    pptFileNew = pdfFile.replace(".pdf", ".ppt")
    if os.path.exists(pptFileNew):
        shutil.move(pptFileNew, pptFile)
        print("Converted PowerPoint slides saved to %s" % pptFile)
    else:
        print("Error: Conversion failed")

# Main program to convert PDF slides to PowerPoint slides
# 

# Parse command line arguments
# Usage: python convertSlides.py -i <input> -o <output>
# Example: python convertSlides.py -i slides.pdf -o slides.ppt
# python convertSlides.py -i ckad20241716389883036.pdf -o ckad20241716389883036.ppt
# 
# Required arguments:
# -i: input PDF file name
# -o: output PowerPoint file name

parser = argparse.ArgumentParser(description='Convert PDF slides to PowerPoint slides')
parser.add_argument('-i', '--input', help='input PDF file name', required=True)
parser.add_argument('-o', '--output', help='output PowerPoint file name', required=True)
args = parser.parse_args()

# Convert PDF slides to PowerPoint slides
convertPDFtoPPT(args.input, args.output)
