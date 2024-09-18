import os
from openai import AzureOpenAI


class AzureGPTProvider:

    def __init__(self, endpoint, api_key, api_version):
        self._client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version
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
            "content": "Your are an English-Chinese translator, \
            no matter what I say, you translate all my words into Chinese."
        },
        {
            "role": "user",
            "content": "你叫什么名字？"
        }
    ]
    openai_endpoint = os.getenv('OpenAIEndpoint')
    openai_api_key = os.getenv('OpenAIKey')
    openai_api_version = '2024-07-01-preview'

    provider = AzureGPTProvider(
        endpoint=openai_endpoint,
        api_key=openai_api_key,
        api_version=openai_api_version
    )
    res = provider.generate_text(msgs, 50)
    print(res)
