from googletrans import Translator
from summarizer import textrank

f=open('/home/deecoders/Desktop/MiniProject/HindiText','r')
hinText=f.read()
f.close()

engText=Translator().translate(hinText,'en')
engSum=textrank(engText.text)

for sentence in engSum:
	hinSent=Translator().translate(sentence,'hi')	
	temp=hinSent.text	
	f=open('/home/deecoders/Desktop/MiniProject/HindiSum','a')
	f.write(temp.encode('utf-8'))
	f.close()


		
