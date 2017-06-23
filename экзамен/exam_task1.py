import xml.etree.ElementTree as ET
import glob, os
#os.chdir("/mydir")
f = open('cout_of_sentences', 'w')

for file in glob.glob("*.xhtml"):
	print(file)
	tree = ET.parse(file)
	root = tree.getroot()
	i=0
	for word in root.iter('se'):
		
		#print ( (word.find('ana').attrib['gr']).find('abl') )
		i=i+1
	f.write(file+"\t"+str(i)+"\n") 
	print (i)
f.close()
