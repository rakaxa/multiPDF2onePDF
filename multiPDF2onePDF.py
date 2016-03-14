#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
import PyPDF2

def main():
  if len(sys.argv) != 3:
    sys.exit("usage : > python multiPDF2onePDF.py [DirectoryName] [OutputName]")
  pdfout = PyPDF2.PdfFileWriter()
  for path in glob.glob(sys.argv[1] + '/*.pdf'):
    pdfin = PyPDF2.PdfFileReader(open(path, "rb"))
    for i in range(0, pdfin.getNumPages()):
      now_page = pdfin.getPage(i)
      pdfout.addPage(now_page)
  outputStream = open(sys.argv[2], "wb")
  pdfout.write(outputStream)
  outputStream.close()

if __name__ == '__main__':
  sys.exit(main())

