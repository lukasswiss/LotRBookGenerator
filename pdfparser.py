from tika import parser

nameofpdf1 = input("PDF 1: ")
nameofpdf2 = input("PDF 2: ")

raw1 = parser.from_file(nameofpdf1)
raw2 = parser.from_file(nameofpdf2)
file = open(nameofpdf + "_" + nameofpdf + "TOTEXT.txt", "w")
file.write(raw1['content'] + raw2['content'])
file.close()
