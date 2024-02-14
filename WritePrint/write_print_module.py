import os

class WritePrintClass:
    def __init__(self):
        # print('started')
        # print(str(os.listdir('./output')))
        with open(
            '.\\output\\source_text_file\\ref.txt',
            'w',
            encoding='utf-8'
        ) as writefile:
            writefile.write('')
    def out(text, end='\n'):
        # print("recieved text: \'" + text + '\'')
        with open(
            '.\\output\\source_text_file\\ref.txt',
            'a',
            encoding='utf-8'
        ) as appendfile:
            appendfile.write(str(text) + end)