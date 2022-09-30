from translate import Translator


class TranslateRepository:

    def translate_content_ch(inData):
      # 實現英文轉中文
        translator = Translator(to_lang='zh-tw')
        translation = translator.translate(inData)
        return translation

    def translate_content_en(inData):
        # 實現中文轉英文
        translator = Translator(from_lang='zh-tw', to_lang='english')
        translation = translator.translate(inData)
        return translation
