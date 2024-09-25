import os
import json
from providers.azure_gpt_provider import AzureGPTProvider


openai_endpoint = os.getenv('OpenAIEndpoint')
openai_api_key = os.getenv('OpenAIKey')
openai_api_version = '2024-07-01-preview'


translator = AzureGPTProvider(
    endpoint=openai_endpoint,
    api_key=openai_api_key,
    api_version=openai_api_version
)


translation_prompt = '''
Your are an English-Chinese translator, I will give you a list of English sentences and the corresponding Chinese sentences that translated from them. 
Your task is to give a score to each of the translated sentence with 1 ~ 5 based on the translation quality.

Below are the score (1 ~ 5) and the corresponding translation quality rubric
1 – Poor (Almost entirely incorrect)
- The translation fails to convey the intended meaning of the original text.  
- Significant errors in understanding or misinterpretation throughout.  
- The target language output is nearly incomprehensible or nonsensical.

2 – Inadequate (Partially correct)
- Some parts of the translation capture the meaning of the original, but many key details are incorrect or omitted.  
- Several significant errors that hinder understanding of the original text.  
- The translation may contain fragments that are correct, but the overall text lacks coherence and accuracy.

3 – Acceptable (Mostly correct but lacking fluency)
- The translation captures the general meaning of the original text.  
- There may be some minor translation errors or awkward phrasing that affects fluency, but the overall message is understandable.  
- Issues such as unnatural phrasing, improper use of idiomatic expressions, or lack of attention to context may be present.

4 – Good (Accurate but lacks natural flow)
- The translation is accurate and conveys the intended meaning of the original text.  
- There are no major errors, but minor flaws may exist, such as overly literal translation or phrasing that feels unnatural in the target language.  
- While grammatically correct, the translation may feel rigid or lack the fluidity of native language usage.

5 – Excellent (Accurate and idiomatic)
- The translation is flawless, capturing not only the exact meaning of the original text but also reflecting cultural nuances and idiomatic expressions of the target language.  
- The text reads smoothly and naturally, as if originally written in the target language.  
- The translation shows attention to detail in both meaning and tone, with no discernible errors or awkwardness.


The input is in json format, with index, English, Chinese given:
[
    {
        "Index": 1,
        "English": "...",
        "Chinese": "..."
    }
    ...
]

The output should also be in json format, with index, and score based on above translation quality rubric:
[
    {
        "Index": 1,
        "Score": 4
    }
    ...
]
'''


batch_size = 50
total_files = 53


def parse_output(text):
    try:
        if not text:
            return text

        text = text.strip('"')
        text = text.strip('```')
        text = text.strip('json')
        items = json.loads(text)
        return items
    except Exception as e:
        print('parse_output error: ', e)
        return None


def get_score(items, i):
    if not items:
        return None
    for item in items:
        if item.get('Index') == i:
            return item.get('Score')
    return None


def pipeline_run():
    # TODO update here
    for i in range(13, 53):
        data_file = '../data/alpaca_chinese_part_{0}.json'.format(i)
        output_file = '../data_v3/alpaca_chinese_part_{0}.json'.format(i)
        with open(data_file, 'r', encoding='utf-8') as rf, open(output_file, 'w', encoding='utf-8') as wf:
            data = json.load(rf)
            translated_results = []

            samples_count = len(data)
            # n = 100
            for i in range(0, samples_count, batch_size):
                print('processing item {0} / {1}'.format(i + 1, samples_count))
                batch_samples = data[i: i + batch_size]
                input_items = []
                index = 0
                for sample in batch_samples:
                    en_instruction = sample.get('en_instruction')
                    instruction = sample.get('instruction')
                    en_input_text = sample.get('en_input')
                    input_text = sample.get('input')
                    en_output_text = sample.get('en_output')
                    output_text = sample.get('output')

                    en_content = '{0}\n{1}\n{2}'.format(en_instruction, en_input_text, en_output_text)
                    zh_content = '{0}\n{1}\n{2}'.format(instruction, input_text, output_text)
                    input_items.append({
                        'Index': index,
                        'English': en_content,
                        'Chinese': zh_content
                    })
                    index += 1

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
                max_token = len(input_items) * 20 + 20
                output_content = translator.generate_text(messages=msgs, max_tokens=max_token)
                print('input len: {0}, output len {1}'.format(len(input_query), len(output_content)))
                output_items = parse_output(output_content)
                if not output_items or len(output_items) != batch_size:
                    print('Failed to translate or parse the result, output_content: ', output_content)
                    output_items = None
                print(output_items)

                # print(output_items)
                for j in range(0, batch_size):
                    item = batch_samples[j]
                    score = get_score(output_items, j)
                    new_item = {
                        'en_instruction': item.get('en_instruction'),
                        'en_input': item.get('en_input'),
                        'en_output': item.get('en_output'),
                        'zh_instruction': item.get('instruction'),
                        'zh_input': item.get('input'),
                        'zh_output': item.get('output'),
                        'metadata': {
                            'translated': True,
                            'score': score
                        }
                    }

                    translated_results.append(new_item)

            wf.write(json.dumps(translated_results, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    pipeline_run()
