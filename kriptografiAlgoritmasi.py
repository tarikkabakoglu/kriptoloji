import random

def sifreyicoz():
	alfabe_2 = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
			  "s", "ş", "t", "u", "ü", "v", "y", "z"]
	l=[]
	sifre=input("sifreyi girniz: ")
	for i in sifre:
		y=alfabe.index(i)
		l+=[y]
	gerçek_metin=""
	for j in l:
		t=alfabe_2[int(j)]
		gerçek_metin+=t
	print("Şifresi çözülmüş metin: ",gerçek_metin)
	print("##############################")


def sifreleme(x):
	global alfabe
	alfabe = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
			  "s", "ş", "t", "u", "ü", "v", "y", "z"]
	k = []
	for i in x:
		a = alfabe.index(i)
		k += [a]
	random.shuffle(alfabe)
	sifre = ""
	for i in k:
		x = alfabe[int(i)]
		sifre += x
	print("Şifrelenmiş metin: ",sifre)
	sifreyicoz()


sifreleme("buharfgrubunuşifreliyoruz")
sifreleme("dahasonrabuşifreyiçözücez")