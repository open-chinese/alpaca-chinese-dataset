from google.cloud import translate_v3
from google.oauth2 import service_account
import os


class GoogleTranslateProvider:

    def __init__(self):
        # TODO the account and credentials settings are not friendly to new Google Cloud users. That's Google:(
        # TODO update this config accordingly

        # NOTE please set the config file path in your environment variables
        service_account_file_path = os.getenv('GoogleServiceAccountFilePath')
        credentials = service_account.Credentials.from_service_account_file(service_account_file_path)
        self._client = translate_v3.TranslationServiceClient(credentials=credentials)
        pass

    def translate(self, texts, target='zh-CN'):
        """
        target languages: https://cloud.google.com/translate/docs/languages
        common languages: zh-CN, en, fr, ja
        """
        parent_project = os.getenv('GoogleCloudProject')
        request = translate_v3.TranslateTextRequest(
            {'contents': texts, 'target_language_code': target, 'parent': parent_project}
        )
        response = self._client.translate_text(request)
        if response:
            results = [i.translated_text for i in response.translations]
            return results

        return None


if __name__ == '__main__':
    translator = GoogleTranslateProvider()
    input_texts = ['You are a 40-year-old introverted librarian named Tom who takes his job very seriously. You find solace in reading historical novels and have a fascination with medieval history. Your current struggle is adapting to new technology as it changes the nature of libraries.',
                   "Well, *clears throat* I've always been fond of physical books. There's just something comforting about holding a book and turning its pages. *adjusts glasses* However, I understand that e-books have their benefits too, like accessibility and ease of use, but it's just been difficult for me to adapt to them."]
    output_texts = translator.translate(input_texts, target='zh-CN')
    input_len = sum([len(i) for i in input_texts])
    output_len = sum([len(i) for i in output_texts])
    print(input_len)

    for i in range(0, len(input_texts)):
        print('--------------------------')
        print(input_texts[i])
        print('-->')
        print(output_texts[i])

