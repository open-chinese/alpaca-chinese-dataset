import os
from openai import OpenAI


GPTTimeout = 15000
OpenAIKey = 'OpenAIKey'


class GPTProvider:

    def __init__(self):
        self._client = OpenAI(
            api_key=os.getenv(OpenAIKey)
        )

    def generate_text(self, messages, max_tokens=100, stop=None):
        chat_completion = self._client.chat.completions.create(
            messages=messages,
            model='gpt-3.5-turbo',
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
    provider = GPTProvider()
    res = provider.generate_text(msgs, 100)
    print(res)
