# coding: utf-8
import glob
import chardet
from chardet.universaldetector import UniversalDetector

print('''Данная программа подсчитывает количество символов
во всех текстовых файлах *.txt в текущей директории
и сохраняет информацию в файл с именем "* техинфо.тхт"\n''')

# записывает заданную строку в файл
def write_line_to_file(out_filename, st):
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

# очистка текста от непечатаемых символов
def clear_non_print_chars(s):
    # символы для удаления
    ch_for_del=['\f',		#перевод страницы
                '\n',		#новая строка
                '\r',		#перевод каретки
                '\v',		#вертикальная табуляция
                '\t'		#горизонтальная табуляция
                ]
 
    # очистка текста
    s_clear = ''.join([i for i in s if i not in ch_for_del])
    return s_clear

# запись информации по заданному символу в файл
def write_char_data_to_file(out_filename, ch, count):
    descr = {' ':'пробелов: ', ',':'запятых: ', '.':'точек: '}
    if ch in descr: 
        write_line_to_file(out_filename, descr[ch]+str(count))
    else:
        write_line_to_file(out_filename, ch+' : '+str(count))

# получаем имена файлов для обработки
def get_filenames_for_processing():
    all_txt_files = glob.glob('*.txt')
    filtered_filenames = [i for i in all_txt_files if 'техинфо' not in i and 'requirements.txt' not in i]
    return filtered_filenames

# считаем кол-во каждого символа в тексте и общее количество
def get_chars_count(s):
    # получаем список уникальных символов (множество)
    uniq_chars=set(s)
    
    # словарь в формате chars_count{символ:количество,...}
    chars_count={}
    
    total_chars=0
    for i in uniq_chars:
        chars_count[i]=s.count(i)
        total_chars+=s.count(i)
    return chars_count, total_chars

filenames_for_processing = get_filenames_for_processing()   
print('файлы для обработки: ', filenames_for_processing)

# обрабатываем каждый файл
for in_filename in filenames_for_processing:
    
    # собираем имя выходного файла
    out_filename = in_filename[:-4]+' техинфо'+'.txt' 

    # создаем/очищаем выходной файл
    with open(out_filename, 'w', encoding='utf-8') as f:
        # и записываем строку с именем входного файла в выходной файл
        f.write('Имя файла: '+in_filename+'\n')
        
    # определяем кодировку входного файла
    enc = detect_charset(in_filename)
    print(in_filename, ',', enc)

    # открываем файл в нужной кодировке
    with open(in_filename, 'r', encoding=enc) as file_in:
     
        #считаем кол-во строк в файле
        lines_num = sum([1 for i in file_in.readlines() if i.strip()])
        
        #записываем данные в файл
        write_line_to_file(out_filename, 'Cтрок: '+str(lines_num))

        #перемотка в начало файла
        file_in.seek(0)

        #считываем данные из файла для дальнейшей обработки
        s = file_in.read()

    # удаляем непечатаемые символы
    s = clear_non_print_chars(s)
    
    # считаем количество заглавных букв
    upper_num = sum(1 for i in s if i.isupper())
    
    #записываем данные в файл
    write_line_to_file(out_filename, 'Заглавных букв: '+str(upper_num))

    # удаляем дублирующие пробелы
    while "  " in s:
        s= s.replace("  ", " ")
    
    # считаем и записываем в файл кол-во символов
    s=s.lower()
    write_line_to_file(out_filename, 'количество символов учитывая пробелы: '+str(len(s)))
    
    # записываем в файл информационную строку
    write_line_to_file(out_filename, '\nСортировка по буквам:')

    # получаем словарь частотности chars_count{символ:количество,...} и общее кол-во символов
    chars_count, total_chars = get_chars_count(s)
    sorted_uniq_chars = sorted(list(chars_count.keys()))
 
    # для каждого символа записываем данные в файл 
    for current_char in sorted_uniq_chars:
        write_char_data_to_file(out_filename, ch=current_char, count=chars_count[current_char])
    
    # запись информационной строки в файл
    write_line_to_file(out_filename, '\nСортировка по количеству:')

    # получаем список упорядоченный по частоте каждого символа
    list_d = list(chars_count.items())
    list_d.sort(key=lambda i: i[1], reverse=True)# key - ключ для сортировки, i[1] - частота символа в тексте

    # для каждого символа записываем данные в файл
    for i in list_d:
        write_char_data_to_file(out_filename, ch=i[0], count=i[1])

    # запись информационной строки в файл
    write_line_to_file(out_filename,'конец')
