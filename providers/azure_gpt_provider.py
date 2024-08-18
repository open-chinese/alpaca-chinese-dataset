import os
from openai import AzureOpenAI


GPTTimeout = 15000
OpenAIEndpoint = os.getenv('OpenAIEndpoint')
OpenAIKey = os.getenv('OpenAIKey')
OpenAIAPIVersion = '2024-07-01-preview'


class AzureGPTProvider:

    def __init__(self):
        self._client = AzureOpenAI(
            azure_endpoint=OpenAIEndpoint,
            api_key=OpenAIKey,
            api_version=OpenAIAPIVersion

        )

    def generate_text(self, messages, max_tokens=100, stop=None):
        chat_completion = self._client.chat.completions.create(
            messages=messages,
            model='gpt-4o',
            max_tokens=max_tokens,
            stop=stop
        )
        response = chat_completion.choices[0].message.content
        return response


if __name__ == '__main__':
    msgs = [
        {
            "role": "system",
            "content": "请将我的所有输入都翻译成中文，不要输出其它内容。"
        },
        {
            "role": "user",
            "content": "你叫什么名字？"
        }
    ]
    provider = AzureGPTProvider()
    res = provider.generate_text(msgs, 50)
    print(res)
