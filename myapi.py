import paralleldots
class API:
    def __init__(self):
        paralleldots.set_api_key('xAoJQMIhQHezUixxxqWZultvc5mfkwsJ5h3Bf8k2Gzc')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion(self,text):
        response = paralleldots.emotion(text)
        return response

