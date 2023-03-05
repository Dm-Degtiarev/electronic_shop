class MixinChangeLang:
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        language_tpl = ('EN', 'RU', 'CH')

        try:
            index = 0
            for language in language_tpl:
                if language == self.__language:
                    self.__language = language_tpl[index + 1]
                    break
                index += 1

        except IndexError:
            self.__language = language_tpl[0]




