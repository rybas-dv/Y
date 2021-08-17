import os
from os.path import join
import time
import codecs

file = codecs.open('errors.txt', 'w', encoding='utf-8')

def get_files_info(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for file_name in files:
            abs_file_name = join(root, file_name)
            try:
                yield abs_file_name, os.stat(abs_file_name)
            except FileNotFoundError:
                print("Long name Error - " + abs_file_name)
                file.write('Long name Error - %s\n' % abs_file_name)
            except OSError:
                print("Access denied! - " + abs_file_name)
                file.write('Access denied! - %s\n' % abs_file_name)


def sizeof_fmt(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)

        num /= 1024.0

    return "%3.1f %s" % (num, 'TB')

def total_size(root):
    total = 0
    for dir, _, files in os.walk(root):
        for fn in files:
            try:
                total += os.path.getsize(os.path.join(dir, fn))
            except FileNotFoundError:
                print("calculate total")
            except OSError:
                print("calculate total")
    return total / 1000000

def get_date_as_string(dt):
    return time.strftime('%H:%M:%S %m.%d.%y', time.gmtime(dt))

total = 0

if __name__ == '__main__':
    #dir_name = r"c:\\Intel"
    dir_name = input("input direction by example - c:\\\\user\\\\administrator - ")
    # Сортировка по размеру
    files_sorted_by_size = sorted(get_files_info(dir_name), reverse=True, key=lambda x: x[1].st_size)

    # # Без сортировки
    # files_sorted_by_size = get_files_info(dir_name)

    # Сохраняем в HTML файл

    with open('result.html', 'w', encoding='utf-8') as f:
        f.write('''
        <html>
            <head>
                <meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>
                <style>
                    /* Добавление сетки таблицы */
                    table {
                        border-collapse: collapse; /* Убираем двойные линии между ячейками */
                    }
                    td, th {
                        padding: 3px; /* Поля вокруг содержимого таблицы */
                        border: 1px solid black; /* Параметры рамки */
                    }
                </style>
            </head>
            <body>
                <table>
        ''')

        f.write('<capture>{}</capture>'.format(dir_name) +  " Total size: " + str(total_size(dir_name)) + " MB ")

        f.write('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format('FILE NAME', 'SIZE', 'LAST MODIFICATION'))

        for file_name, file_stat in files_sorted_by_size:
            f.write('<tr>')

            f.write('<td>{}</td><td>{}</td><td>{}</td>'.format(
                '<a href="file://{f}">{f}</a>'.format(f=file_name),
                sizeof_fmt(file_stat.st_size),
                get_date_as_string(file_stat.st_mtime)
            ))

            f.write('</tr>')
        f.write('''
                </table>
            </body>
        </html>
        ''')
file.close()
