import pyttsx3
import PyPDF3
speaker= pyttsx3.init()
pdfreader = PyPDF3.PdfFileReader(open('George R. R. Martin - Buz ve Ateşin Şarkısı #2 - Kralların Çarpışması.pdf','rb'))

for page_number in range(pdfreader.numPages):
    text =pdfreader.getPage(page_number).extractText()
    speaker.say(text)
    speaker.runAndWait()
   
speaker.stop()