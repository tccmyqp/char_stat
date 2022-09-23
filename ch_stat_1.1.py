#  coding: utf-8
#from imp import reload
#import sys
import glob
#import urllib.request
import chardet
from chardet.universaldetector import UniversalDetector
#import string
#import chardet

#reload(sys)
#print (sys.version)

print('''Данная программа подсчитывает количество символов
во всех текстовых файлах *.txt в текущей директории
и сохраняет информацию в файл с именем "* техинфо.тхт"\n''')

def write_step(st):
	#print(st)
	file_out.write(st+'\n')
	
all_txt_files = glob.glob('*.txt')

file_lst=[]
print(len(all_txt_files))
	
for i in all_txt_files:
	print(i)
	if 'техинфо' not in i:
		file_lst.append(i)
print(file_lst)

#открываем файлы
detector = UniversalDetector()
for filename in file_lst:

	filename_read = filename
	filename_write = filename_read[:-4]+' техинфо'+'.txt'
	file_out = open(filename_write, 'w', encoding='utf-8')

	#print(handle)

	write_step('Имя файла: '+ filename_read)

	detector.reset()   	
	for line in open(filename_read, 'rb'):
	    detector.feed(line)
	    if detector.done: break
	detector.close()
	enc = detector.result['encoding']
	#print (enc)
	
	if enc!='utf-8':
		with open(filename_read, 'r') as file_in:
			#считаем строки
			write_step('Cтрок: '+str(sum([1 for i in file_in.readlines() if i.strip()])))
			file_in.seek(0)#перемотка в начало файла
			s = file_in.read()#читаем данные
		file_in.close()
		#print(s,'\n')
	else:
		with open(filename_read, 'r', encoding=enc) as file_in:
			#считаем строки
			write_step('Cтрок: '+str(sum([1 for i in file_in.readlines() if i.strip()])))
		file_in.close()
		

		with open(filename_read, 'rb') as file_in:
			s = file_in.read()#читаем данные
			s = s.decode(enc)
		#print(s,'\n')
		file_in.close()

	#очистка текста
	s=s.replace('\f','')#перевод страницы
	s=s.replace('\n','')#новая строка
	s=s.replace('\r','')#перевод каретки
	s=s.replace('\v','')#вертикальная табуляция
	s=s.replace('\t',' ')#горизонтальная табуляция

	write_step('Заглавных букв: '+str(sum(1 for i in s if i.isupper())))

	
	s=s.lower()

	while "  " in s:#удаляем лишние пробелы
	    s= s.replace("  ", " ")

	write_step('количество символов с пробелами: '+str(len(s)))
	
	data=set(s)
	d={}

	total=0
	for i in data:
	  d[i]=s.count(i)
	  total+=s.count(i)

	#write_step('Символов подсчитано:'+str(total))

	write_step('\nСортировка по буквам:')

	list_keys = list(d.keys())
	list_keys.sort()

	for i in list_keys:
	  if i==' ':
	    write_step('пробелов: '+ str(d[i]))
	  elif i==',':
	    write_step('запятых: '+ str(d[i]))
	  elif i=='.':
	    write_step('точек: '+ str(d[i]))
	  else:
	    write_step(i+' : '+ str(d[i]))
	 
	write_step('\nСортировка по количеству:')

	list_d = list(d.items())
	list_d.sort(key=lambda i: i[1], reverse=True)

	for i in list_d:
	  if i[0]==' ':
	    write_step('пробелов: '+ str(i[1]))
	  elif i[0]==',':
	    write_step('запятых: '+ str(i[1]))
	  elif i[0]=='.':
	    write_step('точек: '+ str(i[1]))
	  else:
	    write_step(i[0]+': '+ str(i[1]))

	file_out.write('конец')
	print('\n')
	file_out.close()