import PyPDF2

open_file=open('/Practice/Files\\Free_Test_Data_100KB_PDF.pdf', 'rb')
File=PyPDF2.PdfReader(open_file)

# Fetch the File details
print(f'The PDF  file  details are : {File.metadata}')

# Find the number of  pages  in File
print(f'The number of pages present in the file are :{len(File.pages)}')

# print all the pages  one by one
for page in range(len(File.pages)):
    print(f'--------------------{page}-------------------')
    print(File.pages[page].extract_text())



