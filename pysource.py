#! usr/bin/python3
#Telergram:Adanlitrojan
#Coder:trojanx6
try:
	from PyPDF2 import PdfFileReader
	from deep_translator import GoogleTranslator
	import sys,os
except Exception as e:
	print(f"Modül Yüklü değil{e}")
	try:
		os.system("pip3 install deep-transtoler")
		os.system("pip3 install PyPDF2")
	except:
		print("Manuel yükleyiniz PyPDF2 and deep-transloter")
		sys.exit()
		
creteaFilesText = open("transtel_.txt", "w")
class PDFREAD(object):
	def __init__(self) -> None:
		super().__init__()
	def app(self):
		self.pdf_file_name = str(input("pdf Giriniz: ")).strip()
		self.Vote = input("Çevrilecek Dil giriniz: ")
		self.pdf_oku = PdfFileReader(self.pdf_file_name, strict=False)
		for i in range(self.pdf_oku.numPages):
			New_page = self.pdf_oku.getPage(i)
			New_Text = New_page.extractText()
			Transtel = GoogleTranslator(source="auto",target=self.Vote).translate(text=New_Text)
			print(Transtel)
			creteaFilesText.write(Transtel)
		Info = self.pdf_oku.getDocumentInfo()
		print(Info)
if __name__=="__main__":
	main = PDFREAD()
	main.app()
	creteaFilesText.close()
