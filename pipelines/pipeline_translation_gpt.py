import os
import json
from providers.azure_gpt_provider import AzureGPTProvider


openai_endpoint = os.getenv('OpenAIEndpoint')
openai_api_key = os.getenv('OpenAIKey')
openai_api_version = '2024-07-01-preview'

msgs = [
    {
        "role": "system",
        "content": "Your are an English-Chinese translator, \
        no matter what I say, you translate all my words into Chinese."
    },
    {
        "role": "user",
        "content": "你叫什么名字？"
    }
]

provider = AzureGPTProvider(
    endpoint=openai_endpoint,
    api_key=openai_api_key,
    api_version=openai_api_version
)
res = provider.generate_text(msgs, 50)


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
                # TODO add the translation process
                # a proper prompt is needed


if __name__ == '__main__':
    pipeline_run()
