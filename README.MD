Логика работы приложения:

    - приложение просматривает директорию запуска на наличие текстовых файлов
    - подсчитывает кол-во символов в каждом найденном файле
    - сортирует результат по алфавиту и по частоте
    - сохраняет результат в файле с добавлением 'техинфо' в имени

Поддержка форматов:

    ansi (windows-1251)
    utf8
    utf8-BOM
    mac

Файлы:

    ch_stat_*.py         скрипт
    text_ansi.txt        тестовый ansi файл
    text_utf8.txt        тестовый utf8 файл
    text_utf-bom.txt     тестовый ansi файл
    text_mac.txt         тестовый utf8 файл
    text_* техинфо.txt   пример результата
    ch_stat_*.exe        приложение под Windows7

Зависимости:

Для запуска приложения возможно потребуется установить vc_redist:
- [Список vc_redist на сайте Microsoft](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022/ "https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022/")
- Прямая ссылка [vc_redist.x86_2015-2022](https://aka.ms/vs/17/release/vc_redist.x86.exe "https://aka.ms/vs/17/release/vc_redist.x86.exe")
- Прямая ссылка [vc_redist.x64_2015-2022](https://aka.ms/vs/17/release/vc_redist.x64.exe "https://aka.ms/vs/17/release/vc_redist.x64.exe")

    