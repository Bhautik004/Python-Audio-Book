import pyttsx3
import PyPDF2
from pyttsx3 import voice

book = open('oop.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # here index 1 for male voice and 2 index for female voice

for num in range(7,pages):
	page = pdfReader.getPage(7)
	text = page.extractText()
	engine.say(text)
	engine.runAndWait()
	