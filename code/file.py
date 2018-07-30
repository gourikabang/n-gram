import glob
import pandas as pd

def deleteContent(fname):
    with open(fname, "w"):
        pass
    return fname
def make_csv(d, n, key):
	df = pd.DataFrame(d)
	df.to_csv(str(n)+'-Gram'+key+'dataset-.csv')
def new_write(filename, date):
	f = open(filename, "w")
	f.write(data)
def new_read(filename, data):
	pass

def program(filename,var):
	if var=="Train":	
		filenames1 = []
		if filename=="Training_Data_Master":
			filenames1 = filenames1+glob.glob(filename+"/*.txt")
		else:
			for i in range(1,8):
				path = filename+"/"+filename+"-"+str(i)
				filenames1 = filenames1+glob.glob(path+"/*.txt")
			
		data1 = "Traindata_"+filename+".txt"
		# deleteContent(data1)
		
		f1 = open(data1, "w+")
		
		for file in filenames1:
			for line in open(file):
				line = line.rstrip()
				f1.write(line)

	elif var=="Test":
		filenames2 = []
		if filename=="Validation_Data_Master":
			filenames2 = filenames2+glob.glob(filename+"/*.txt")

		else:
			for i in range(8,11):
				path = filename+"/"+filename+"-"+str(i)
				filenames2 = filenames2+glob.glob(path+"/*.txt")

		data2 = "Testdata_"+filename+".txt"
		deleteContent(data2)

		f2 = open(data2, "w")

		for file in filenames2:
			for line in open(file):
				line = line.rstrip()
				f2.write(line)




