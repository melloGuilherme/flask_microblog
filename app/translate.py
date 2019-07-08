import json
import requests
from app import app
from flask_babel import _


def translate(text, source_lang, dest_lang):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    url = (
        f'https://api.microsofttranslator.com/v2/Ajax.svc'
        f'/Translate?text={text}&from={source_lang}&to={dest_lang}'
    )

    r = requests.get(url, headers=auth)

    if r.status_code != 200:
        return _('Error: the translation service failed.')

    return json.loads(r.content.decode('utf-8-sig'))
