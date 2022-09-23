# coding: utf-8
import glob
import chardet
from chardet.universaldetector import UniversalDetector

print('''Данная программа подсчитывает количество символов
во всех текстовых файлах *.txt в текущей директории
и сохраняет информацию в файл с именем "* техинфо.тхт"\n''')

# записывает заданную строку в файл
def write_line(out_filename, st):
    with open(out_filename, 'a', encoding='utf-8') as file_out:
        file_out.write(st+'\n')

# детектор кодировки
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
    
# получаем имена файлов для обработки
file_lst = [i for i in all_txt_files if 'техинфо' not in i and 'requirements.txt' not in i]
        
print('файлы для обработки: ', file_lst)

# обрабатываем каждый файл
for in_filename in file_lst:

    # собираем имя выходного файла
    out_filename = in_filename[:-4]+' техинфо'+'.txt' 

    # создаем/очищаем выходной файл
    with open(out_filename, 'w', encoding='utf-8') as f:
        # пишем информацию в файл
        f.write('Имя файла: ' + in_filename +'\n')
    
    # определяем кодировку входного файла
    enc = detect_charset(in_filename)
    print(in_filename, ',', enc)

    # открываем файл в нужной кодировке и считываем данные
    with open(in_filename, 'r', encoding=enc) as file_in:
     
        #считаем кол-во строк
        lines_num = sum([1 for i in file_in.readlines() if i.strip()])
        
        #записываем данные в файл
        write_line(out_filename, 'Cтрок: ' + str(lines_num))

        #перемотка в начало файла
        file_in.seek(0)

        #считываем данные
        s = file_in.read()
  
    # символы для удаления
    ch_for_del=['\f',		#перевод страницы
                '\n',		#новая строка
                '\r',		#перевод каретки
                '\v',		#вертикальная табуляция
                '\t'		#горизонтальная табуляция
                ]
 
    # очистка текста
    s_clear = ''.join([i for i in s if i not in ch_for_del])
    s = s_clear
    
    # считаем количество заглавных букв
    upper_num = sum(1 for i in s if i.isupper())
    write_line(out_filename, 'Заглавных букв: '+str(upper_num))

    # удаляем дублирующие пробелы
    while "  " in s:
        s= s.replace("  ", " ")
    
    s=s.lower()
    write_line(out_filename, 'количество символов учитывая пробелы: '+str(len(s)))
    
    # получаем список уникальных символов (множество)
    uniq_chars=set(s)
 
    # словарь в формате {символ:количество,...}
    chars_count={} 

    # считаем кол-во каждого символа в тексте и общее количество, заполняем словарь d{}
    total=0
    for i in uniq_chars:
        chars_count[i]=s.count(i)
        total+=s.count(i)

    # записываем в файл информационную строку
    write_line(out_filename, '\nСортировка по буквам:')

    list_keys = sorted(list(chars_count.keys()))

    # запись информации по заданному символу в файл
    def write_char_data(ch, d):
        descr = {' ':'пробелов: ', ',':'запятых: ', '.':'точек: '}
        if ch in descr: 
            write_line(out_filename, descr[ch]+ str(d))
        else:
            write_line(out_filename, ch+' : '+ str(d))
 
    for i in list_keys:
        write_char_data(i, chars_count[i])
    
    # запись информационной строки в файл
    write_line(out_filename, '\nСортировка по количеству:')

    list_d = list(chars_count.items())
    list_d.sort(key=lambda i: i[1], reverse=True)

    for i in list_d:
        write_char_data(i[0], i[1])

    # запись информационной строки в файл
    write_line(out_filename,'конец')
