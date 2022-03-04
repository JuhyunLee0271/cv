from googletrans import Translator

string = "Hello My name is Juhyun"
string2 = "안녕하세요. 저는 이주현입니다."

translator = Translator()

result = translator.translate(string, src='en', dest='ko')
result2 = translator.translate(string2, src='ko', dest='en')

print(result.text)  # 안녕하세요 내 이름은 Juhyun입니다
print(result2.text) # Hello.I am Lee Ju-hyun.

print(translator.detect(string))    # Detected(lang=en, confidence=None)
print(translator.detect(string2))   # Detected(lang=ko, confidence=None)

