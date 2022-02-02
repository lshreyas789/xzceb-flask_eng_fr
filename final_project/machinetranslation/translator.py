"""
Translates the text to French & French to English

"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator= IAMAuthenticator('_ChXTP4VmzdT3SZRH0eleUpm2AqjJcL1imj_9DJfg2h7')
language_translator = LanguageTranslatorV3(
    version= '2018-05-01',
    authenticator= authenticator
)

language_translator.set_service_url(
     'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/80acf9b8-c168-4e4b-a248-39f50f15263d')

languages= language_translator.list_identifiable_languages().get_result()

print(json.dumps(languages, indent=2))



def english_to_french(english_text):
    translation= language_translator.translate(text= english_text, model_id= 'en-fr').get_result()
    french_text= translation ['translations'] [0] ['translation']
    

    return french_text

def french_to_english(french_text):
    translation= language_translator.translate(text= french_text, model_id='fr-en').get_result()
    english_text= translation ['translations'] [0] ['translation']
    return english_text

