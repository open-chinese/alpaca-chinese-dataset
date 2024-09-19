
class WordUtil:
    @staticmethod
    def count_en_words(text):
        """
        This function does not validate the input language
        :param text:
        :return:
        """
        if not text:
            return 0
        words = text.split(' ')
        words = [w for w in words if w.strip()]
        return len(words)

    @staticmethod
    def count_en_words_fast(text):
        """
        This function does not validate the input language
        :param text:
        :return:
        """
        c = 0
        i = 0
        n = len(text)
        while i < n:
            while i < n and text[i] == ' ':
                i += 1
            skip_word = False
            while i < n and text[i] != ' ':
                i += 1
                skip_word = True
            if skip_word:
                c += 1
        return c

    @staticmethod
    def count_zh_words(text):
        """
        This function does not validate the input language
        :param text:
        :return:
        """
        return WordUtil.count_chars(text)

    @staticmethod
    def count_chars(text):
        if not text:
            return 0
        return len(text)


if __name__ == '__main__':
    s = '   Hellowho are   you     ..'
    n = WordUtil.count_en_words_fast(s)
    print(n)