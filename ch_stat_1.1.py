#  coding: utf-8
import glob
import chardet
from chardet.universaldetector import UniversalDetector

print('''Данная программа подсчитывает количество символов
во всех текстовых файлах *.txt в текущей директории
и сохраняет информацию в файл с именем "* техинфо.тхт"\n''')

def write_line(st):
	file_out.write(st+'\n')
	
all_txt_files = glob.glob('*.txt')

file_lst=[]
	
for i in all_txt_files:
	if 'техинфо' not in i and 'requirements.txt' not in i:
		file_lst.append(i)
print('файлы для обработки: ', file_lst)

#открываем файлы
detector = UniversalDetector()
for filename in file_lst:

	filename_read = filename
	filename_write = filename_read[:-4]+' техинфо'+'.txt'
	file_out = open(filename_write, 'w', encoding='utf-8')

	write_line('Имя файла: '+ filename_read)

	detector.reset()   	
	for line in open(filename_read, 'rb'):
	    detector.feed(line)
	    if detector.done: break
	detector.close()
	enc = detector.result['encoding']
	
	if enc!='utf-8':
		with open(filename_read, 'r') as file_in:
			#считаем строки
			write_line('Cтрок: '+str(sum([1 for i in file_in.readlines() if i.strip()])))
			file_in.seek(0)#перемотка в начало файла
			s = file_in.read()#читаем данные
		file_in.close()
	else:
		with open(filename_read, 'r', encoding=enc) as file_in:
			#считаем строки
			write_line('Cтрок: '+str(sum([1 for i in file_in.readlines() if i.strip()])))
		file_in.close()
		

		with open(filename_read, 'rb') as file_in:
			s = file_in.read()#читаем данные
			s = s.decode(enc)
		file_in.close()

	
	# символы для удаления
	ch_for_del = ['\f',		#перевод страницы
				  '\n',		#новая строка
				  '\r',		#перевод каретки
				  '\v',		#вертикальная табуляция
				  '\t'		#горизонтальная табуляция
				]
 
	#очистка текста
	s_clear = ''.join([i for i in s if i not in ch_for_del])
	s = s_clear
 
	write_line('Заглавных букв: '+str(sum(1 for i in s if i.isupper())))

	s=s.lower()

	#удаляем дублирующие пробелы
	while "  " in s:
	    s= s.replace("  ", " ")

	write_line('количество символов учитывая пробелы: '+str(len(s)))
	
	# получаем список уникальных символов (множество)
	uniq_chars=set(s)
 
	d={} # словарь в формате {символ:количество,...}

	# считаем кол-во каждого символа в тексте и общее количество, заполняем словарь d{}
	total=0
	for i in uniq_chars:
	  d[i]=s.count(i)
	  total+=s.count(i)

	write_line('\nСортировка по буквам:')

	list_keys = sorted(list(d.keys()))
 
	descr = {' ':'пробелов: ', ',':'запятых: ', '.':'точек: '}
 
	for i in list_keys:
		if i in descr: 
			write_line(descr[i]+ str(d[i]))
		else:
			write_line(i+' : '+ str(d[i]))
	 
	write_line('\nСортировка по количеству:')

	list_d = list(d.items())
	list_d.sort(key=lambda i: i[1], reverse=True)

	for i in list_d:
	  if i[0]==' ':
	    write_line('пробелов: '+ str(i[1]))
	  elif i[0]==',':
	    write_line('запятых: '+ str(i[1]))
	  elif i[0]=='.':
	    write_line('точек: '+ str(i[1]))
	  else:
	    write_line(i[0]+': '+ str(i[1]))

	file_out.write('конец')
	file_out.close()