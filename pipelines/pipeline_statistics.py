import os
import json
from utils.word_util import WordUtil


"""
Tokens can be thought of as pieces of words. Before the API processes the request, the input is broken down into tokens. These tokens are not cut up exactly where the words start or end - tokens can include trailing spaces and even sub-words. Here are some helpful rules of thumb for understanding tokens in terms of lengths:

1 token ~= 4 chars in English

1 token ~= ¾ words

100 tokens ~= 75 words

Or 

1-2 sentence ~= 30 tokens

1 paragraph ~= 100 tokens

1,500 words ~= 2048 tokens
"""

def pipeline_run():
    total_en = 0
    total_zh = 0
    total_char = 0
    for i in range(0, 53):
        data_file = '../data/alpaca_chinese_part_{0}.json'.format(i)
        with open(data_file, 'r', encoding='utf-8') as rf:
            data = json.load(rf)
            en_words_count = 0
            zh_words_count = 0
            chars_count = 0
            index = 0
            for sample in data:
                # print(sample)
                en_instruction = sample.get('en_instruction')
                instruction = sample.get('instruction')
                en_input_text = sample.get('en_input')
                input_text = sample.get('input')
                en_output_text = sample.get('en_output')
                output_text = sample.get('output')
                en1 = WordUtil.count_en_words_fast(en_instruction)
                en2 = WordUtil.count_en_words_fast(en_input_text)
                zh1 = WordUtil.count_zh_words(instruction)
                zh2 = WordUtil.count_zh_words(input_text)
                char1 = WordUtil.count_chars(en_instruction)
                char2 = WordUtil.count_chars(en_input_text)
                en_words_count += (en1 + en2)
                zh_words_count += (zh1 + zh2)
                chars_count += (char1 + char2)
                index += 1

            total_en += en_words_count
            total_zh += zh_words_count
            total_char += chars_count
    print('total en: ', total_en)
    print('total zh: ', total_zh)
    print('total_char: ', total_char)
    print('total tokens (approximately 1): ', int(total_char / 4))
    print('total tokens (approximately 2): ', int(total_en * 0.75))


if __name__ == '__main__':
    pipeline_run()