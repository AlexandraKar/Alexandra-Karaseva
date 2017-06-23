import xml.etree.ElementTree as ET
import csv
import glob, os
csvfile = open('info.csv', 'w') #открытие csv  файла
with csvfile:
	fieldnames = ['Название файла', 'Автор', 'Тематика текста'] #Формирование заголовков файла
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=';')#создание объекта DictWriter для работы с csv файлом
	writer.writeheader()#запись заголовка в файл
	for file in glob.glob("*.xhtml"):#перебор всех файлов в директории
		#print(file)
		tree = ET.parse(file)#разбор csv файла
		root = tree.getroot()#получение корневого тэга файла
		author=''
		topic=''
		for meta in root.iter('meta'):
			if (meta.attrib['name']=='author'):#Поиск тэга с атрибутом author и извлечение имени автора
				author=meta.attrib['content']
			if (meta.attrib['name']=='topic'):#Поиск тэга с атрибутом topic и извлечение названия темы
				topic=meta.attrib['content']
			#print (author+' '+topic)
			writer.writerow({'Название файла': file, 'Автор': author,'Тематика текста':topic})#запись созданной строки в csv файл

