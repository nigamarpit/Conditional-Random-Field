from collections import Counter
import string
class HW2(object):
	def __init__(self):
		self.l=list()
		self.d=dict()
		self.readpos()
		self.modifiedFile()
		self.makeList()
		self.readFile()
		self.removeC()

	def removeC(self):
		f=open('average.txt','r+',encoding="latin-1")
		g=open('average1.txt','w+')
		for line in f:
			g.write('\t'.join(line[:-1].split(','))+'\n')

	def readpos(self):
		f=open('pos10.csv','r+',encoding="latin-1")
		g=open('pos11.csv','w+')
		l=['east','west','north','south']
		for line in f:
			if any(dir in line.split(',')[0].lower() for dir in l):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()

		
		f=open('pos7.csv','r+',encoding="latin-1")
		g=open('pos8.csv','w+')
		l=['quake','earthquake','typoon','volcano','eruption','storm','hurricane','flood','fire','cyclone','wildfire','landslide']
		for line in f:
			if(line.split(',')[0].lower() in l):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		
		
		f=open('pos7.csv','r+',encoding="latin-1")
		g=open('pos8.csv','w+')
		l=['january','february','march','april','june','july','august','september','october','november','december']
		for line in f:
			if(line.split(',')[0].lower() in l):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		

		
		f=open('pos6.csv','r+',encoding="latin-1")
		g=open('pos7.csv','w+')
		l=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
		for line in f:
			if(line.split(',')[0].lower() in l):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		
		
		f=open('pos5.csv','r+',encoding="latin-1")
		g=open('pos6.csv','w+')
		l=['week','month','year']
		for line in f:
			if(line.split(',')[0].lower() in l):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		

		
		f=open('pos4.csv','r+',encoding="latin-1")
		g=open('pos5.csv','w+')
		l=string.punctuation
		for line in f:
			if any(char in l for char in line.split(',')[0]):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		

		
		f=open('pos3.csv','r+',encoding="latin-1")
		g=open('pos4.csv','w+')
		for line in f:
			if(line.split(',')[0][0].isupper()):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		

		
		f=open('pos2.csv','r+',encoding="latin-1")
		g=open('pos3.csv','w+')
		for line in f:
			try:
				float(line.split(',')[0])
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			except:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		
		
		f=open('pos1.csv','r+',encoding="latin-1")
		g=open('pos2.csv','w+')
		for line in f:
			if(line.split(',')[0].isdigit()):
				g.write(','.join(line[:-1].split(',')[:])+','+'1'+'\n')
			else:
				g.write(','.join(line[:-1].split(',')[:])+','+'0'+'\n')
		f.close()
		g.close()
		




	def makeList(self):
		f=open('input.txt','r+',encoding='utf-8')
		for line in f:
			self.l.extend(line.split())
		self.d=dict(Counter(self.l))
		f.close()
		f=open('tokens.txt','w+')
		#f.write('{')
		for x in list(self.l):
			f.write(x+'\n')
			#f.write('"'+x+'":['+str(self.d[x])+'],\n')
		#f.write('}')
		f.close()

	def readFile(self):
		f=open('tokens.txt','r+')
		d=eval(f.read())
		print(type(d))

	def modifiedFile(self):
		f=open('InputModified.txt','r+',encoding="utf-8")
		g=open('pos.csv','w+')
		for line in f:
			l=line.split()
			for x in l:
				g.write(x.split('/')[0]+','+x.split('/')[1]+'\n')
		f.close
		g.close()

HW2()