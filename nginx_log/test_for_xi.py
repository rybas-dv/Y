from collections import Counter
import re 

with open("test.txt", "r") as file_handler:
    ip = file_handler.read()
    print(Counter(re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip)))

    file_handler.close()