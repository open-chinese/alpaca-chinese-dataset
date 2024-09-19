import os
import json
from providers.azure_gpt_provider import AzureGPTProvider


openai_endpoint = os.getenv('OpenAIEndpoint')
openai_api_key = os.getenv('OpenAIKey')
openai_api_version = '2024-07-01-preview'

demo_msgs = [
    {
        "role": "system",
        "content": "Your are an English-Chinese translator, \
        no matter what I say, you translate all my words into Chinese."
    },
    {
        "role": "user",
        "content": "what is your name??"
    }
]

translator = AzureGPTProvider(
    endpoint=openai_endpoint,
    api_key=openai_api_key,
    api_version=openai_api_version
)
res = translator.generate_text(demo_msgs, 2000)
print(res)


translation_prompt = '''
Your are an English-Chinese translator, please translate my message into Chinese. 
You should translate wisely, below are some of the guidelines for you.
1 If some content is not suitable in Chinese culture, you should say it in a Chinese way.
2 If some content is not property to translate, just keep it as it is, for example, programming code, math equations, etc.
3 If some content is not able to translate directly, e.g. some English proverb, please find a similar Chinese one as the output.
4 I will give you a json, please give me the corresponding translated json.
'''


batch_size = 2
total_files = 10
max_token_len = 8000


def parse_output(text):
    try:
        if not text:
            return text

        text = text.strip('"')
        text = text.strip('```')
        items = json.loads(text)
        return items
    except Exception as e:
        print('parse_output error: ', e)
        return None


def pipeline_run():
    for i in range(0, total_files):
        data_file = '../data/alpaca_chinese_part_{0}.json'.format(i)
        output_file = '../data_v2/alpaca_chinese_part_{0}.json'.format(i)
        with open(data_file, 'r', encoding='utf-8') as rf, open(output_file, 'w', encoding='utf-8') as wf:
            data = json.load(rf)
            translated_results = []

            #n = len(data)
            n = 10
            for i in range(0, n, batch_size):
                print('processing item {0} / {1}'.format(i + 1, n))
                batch_samples = data[i: i + batch_size]
                input_items = []
                for sample in batch_samples:
                    en_instruction = sample.get('en_instruction')
                    # instruction = sample.get('instruction')
                    en_input_text = sample.get('en_input')
                    # input_text = sample.get('input')
                    en_output_text = sample.get('en_output')
                    # output_text = sample.get('output')

                    input_items.append({
                        'text1': en_instruction,
                        'text2': en_input_text,
                        'text3': en_output_text
                    })
                input_query = json.dumps(input_items, ensure_ascii=False)
                msgs = [
                    {
                        "role": "system",
                        "content": translation_prompt
                    },
                    {
                        "role": "user",
                        "content": input_query
                    }
                ]
                max_token = len(input_query) if len(input_query) < max_token_len else max_token_len
                output_content = translator.generate_text(messages=msgs, max_tokens=max_token)
                print('input len: {0}, output len {1}'.format(len(input_query), len(output_content)))
                output_items = parse_output(output_content)
                if not output_items or len(output_items) != batch_size:
                    print('Failed to translate or parse the result, output_content: ', output_content)
                    output_items = None

                # print(output_items)
                for j in range(0, batch_size):
                    item = batch_samples[j]
                    new_item = {
                        'en_instruction': item.get('en_instruction'),
                        'en_input': item.get('en_input'),
                        'en_output': item.get('en_output'),
                        'zh_instruction': None,
                        'zh_input': None,
                        'zh_output': None,
                        'metadata': {
                            'translated': False
                        }
                    }
                    if output_items:
                        output_item = output_items[j]
                        if 'text1' in output_item and 'text2' in output_item and 'text3' in output_item:
                            new_item['zh_instruction'] = output_item['text1']
                            new_item['zh_input'] = output_item['text2']
                            new_item['zh_output'] = output_item['text3']
                            new_item['metadata']['translated'] = True

                    translated_results.append(new_item)

            wf.write(json.dumps(translated_results, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    pipeline_run()
