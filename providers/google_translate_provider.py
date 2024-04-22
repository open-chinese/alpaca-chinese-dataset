from google.cloud import translate_v2
from google.oauth2 import service_account


class GoogleTranslateProvider:

    def __init__(self):
        # TODO the account and credentials settings are not friendly to new Google Cloud users. That's Google:(
        # TODO update this config accordingly
        credentials = service_account.Credentials.from_service_account_file('/some/path/GoogleTranslateAPI.json')
        self._client = translate_v2.Client(credentials=credentials)
        pass

    def translate(self, text, target='zh-CN'):
        """
        target languages: https://cloud.google.com/translate/docs/languages
        common languages: zh-CN, en, fr, ja
        """

        result = self._client.translate(text, target_language=target)
        return result


if __name__ == '__main__':
    translator = GoogleTranslateProvider()
    text_en = 'Hello'
    text_zh = translator.translate(text_en, target='zh-CN')
    print('{0} --> {1}'.format(text_en, text_zh))
