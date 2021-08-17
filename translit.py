import csv
import transliterate
with open('name1.csv', 'r', encoding='utf-8') as f:
    line = f.readlines()
    input_data = list()
    result = list()
    for x in line:
        translit = transliterate.translit(x, 'ru', reversed=True, )
        input_data.append(translit)
    for s in input_data:
        n = s.index(" ")
        s1 = s[0:n]
        s1 = s1 + "_"
        s1 = s1 + s[n + 1]
        n = s.find(' ', n + 1)
        s1 = s1 + s[n + 1]
        result.append(s1)
    file = open('result.csv', 'w', encoding='Utf-8')
    for item in result:
        file.write('%s\n' % item)
    file.close()
f.close()