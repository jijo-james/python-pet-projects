from googletrans import Translator, LANGUAGES
import json

# print(json.dumps(googletrans.LANGUAGES, indent=2))

translator = Translator()


sreenivasan_sandeesham_poland = "പോളണ്ടിനെ പറ്റി ഒരക്ഷരം മിണ്ടിപ്പോകരുത്"
sreenivasan_nadodikattu_samayam = "എല്ലാത്തിനും അതിൻ്റേതായ സമയമുണ്ട് ദാസാ"
mammooty_vadakknveeragaha_chandu = "ചന്തുവിനെ തോൽപിക്കാൻ നിങ്ങൾക്കാവില്ല മക്കളേ"

godfather = "I'm gonna make him an offer he can't refuse"

print(translator.detect(sreenivasan_sandeesham_poland))

op = translator.translate(godfather, dest='ml').text


with open('translated_text.txt', 'w', encoding='utf8') as f:
    f.write(op)

print('done')
