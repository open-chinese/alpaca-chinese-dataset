import json
import math
from os import listdir
from os.path import isfile, join

split_file_dir = './data'
split_file_path_template = './data/alpaca_chinese_part_{0}.json'
chunk_size = 1000


target_patterns = ('nooutput',)


def clean():
    split_files = [join(split_file_dir, file_name) for file_name in listdir(split_file_dir)]
    total_count = 0
    for split_file in split_files[:]:
        if not split_file.endswith('.json'):
            continue
        with open(split_file, 'r', encoding='utf-8') as rf:
            items = json.load(rf)
            for item in items:
                en_output = item['en_output']
                # zh_output = item['output']
                for target_pattern in target_patterns:
                    if target_pattern in en_output.lower():
                        print(split_file, item['en_instruction'])
                        total_count += 1
                        break
                # print(item)
    print('batch clean done, found {0} samples'.format(total_count))


if __name__ == '__main__':
    clean()  # batch clean
