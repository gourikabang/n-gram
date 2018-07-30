from nGram import *
from file import *

def test():
	
	
	print("Showing the unique 3-grams, 5-grams & 7-grams for each category of Attack and Normal data from their Test Set")
	print("-------------------------------------------------------------------------------------------------")
	for i in range(3):
		testdatafeatures = []
		dic = {}
		dic1 = {}
		dictionary = {}
		print("-------------------------------------------------------------------------------------------------")
		print("Enter the value of 'n' in n-gram:- ")
		n = int(input())
		for j in range(7):
			print("Choose the following category: ")
			print("1. Hydra_FTP")
			print("2. Hydra_SSH")
			print("3. Adduser")
			print("4. Java_Meterpreter")
			print("5. Meterpreter")
			print("6. Web_Shell")
			print("7. Validation_Data_Master")
			c = int(input())
			if c==1:
				filename="Hydra_FTP"
			elif c==2:
				filename="Hydra_SSH"
			elif c==3:
				filename="Adduser"
			elif c==4:
				filename="Java_Meterpreter"
			elif c==5:
				filename="Meterpreter"
			elif c==6:
				filename="Web_Shell"
			elif c==7:
				filename="Validation_Data_Master"
			program(filename,"Test")
			d, t = nGram("Testdata_"+filename+".txt",n)
			l = list(t)
			for lim in l:
				testdatafeatures.append(lim)
			dic[filename]=d

		filename = ["Hydra_FTP","Hydra_SSH","Adduser","Java_Meterpreter","Meterpreter","Web_Shell","Validation_Data_Master"]
		for file in filename:
			dic1 = dic[file]
			dic2={}
			for i in testdatafeatures:
				if str(tuple(i)) not in dic2.keys():
					if str(tuple(i)) in dic1.keys():
						dic2[str(tuple(i))]=dic1[str(tuple(i))]
					else:
						dic2[str(tuple(i))]=0
			dictionary[file]=dic2
		make_csv(dictionary, n, "Test")








