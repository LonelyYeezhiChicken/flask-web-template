import googletrans

# Initial
translator = googletrans.Translator()


class TranslateRepository:

    def translate_content_ch(inData):
        # 實現英文轉中文
        translation = translator.translate(inData, dest='zh-tw')
        return translation.text

    def translate_content_en(inData):
        # 實現中文轉英文
        translator = translator(from_lang='zh-tw', to_lang='english')
        translation = translator.translate(inData, dest="en")
        return translation.text
