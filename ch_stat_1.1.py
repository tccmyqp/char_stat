#  coding: utf-8
import glob
import chardet
from chardet.universaldetector import UniversalDetector

print('''Данная программа подсчитывает количество символов
во всех текстовых файлах *.txt в текущей директории
и сохраняет информацию в файл с именем "* техинфо.тхт"\n''')

def write_line(out_filename, st):
	with open(out_filename, 'a', encoding='utf-8') as file_out:
		file_out.write(st+'\n')

def detect_charset(in_filename):
	detector = UniversalDetector()
	detector.reset()   	
	with open(in_filename, 'rb') as file_in:
		for line in file_in:
			detector.feed(line)
			if detector.done:
				break
	detector.close()
	return detector.result['encoding']

all_txt_files = glob.glob('*.txt')

file_lst=[]
	
# получаем имена файлов для обработки
for i in all_txt_files:
	if 'техинфо' not in i and 'requirements.txt' not in i:
		file_lst.append(i)
print('файлы для обработки: ', file_lst)

#обрабатываем файлы
for filename in file_lst:

	in_filename = filename
	out_filename = in_filename[:-4]+' техинфо'+'.txt'
 
	# создаем/очищаем файл
	with open(out_filename, 'w', encoding='utf-8') as f:
		pass
 
	write_line(out_filename, 'Имя файла: '+ in_filename)
	
	enc = detect_charset(in_filename)
 
	# считываем файлы в нужной кодировке
	print(enc)
	with open(in_filename, 'r', encoding=enc) as file_in:
		#считаем строки
		write_line(out_filename, 'Cтрок: '+str(sum([1 for i in file_in.readlines() if i.strip()])))
		file_in.seek(0)#перемотка в начало файла
		s = file_in.read()#читаем данные
  
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
 
	write_line(out_filename, 'Заглавных букв: '+str(sum(1 for i in s if i.isupper())))

	s=s.lower()

	#удаляем дублирующие пробелы
	while "  " in s:
	    s= s.replace("  ", " ")

	write_line(out_filename, 'количество символов учитывая пробелы: '+str(len(s)))
	
	# получаем список уникальных символов (множество)
	uniq_chars=set(s)
 
	d={} # словарь в формате {символ:количество,...}

	# считаем кол-во каждого символа в тексте и общее количество, заполняем словарь d{}
	total=0
	for i in uniq_chars:
	  d[i]=s.count(i)
	  total+=s.count(i)

	write_line(out_filename, '\nСортировка по буквам:')

	list_keys = sorted(list(d.keys()))
 
	descr = {' ':'пробелов: ', ',':'запятых: ', '.':'точек: '}
 
	for i in list_keys:
		if i in descr: 
			write_line(out_filename, descr[i]+ str(d[i]))
		else:
			write_line(out_filename, i+' : '+ str(d[i]))
	 
	write_line(out_filename, '\nСортировка по количеству:')

	list_d = list(d.items())
	list_d.sort(key=lambda i: i[1], reverse=True)

	for i in list_d:
	  if i[0]==' ':
	    write_line(out_filename, 'пробелов: '+ str(i[1]))
	  elif i[0]==',':
	    write_line(out_filename, 'запятых: '+ str(i[1]))
	  elif i[0]=='.':
	    write_line(out_filename, 'точек: '+ str(i[1]))
	  else:
	    write_line(out_filename, i[0]+': '+ str(i[1]))

	write_line(out_filename,'конец')
