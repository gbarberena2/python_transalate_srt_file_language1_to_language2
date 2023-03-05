import pysrt
from translate import Translator

# Abre el archivo SRT para leer
subs = pysrt.open('novel2.srt')

# Crea un objeto Translator
translator = Translator(to_lang='es')

# Traduce el texto de cada subtítulo y agrega los subtítulos traducidos a una lista
translated_subs = []
for sub in subs:
    # Traduce solo el texto del subtítulo, no los indicadores numéricos
    translated_text = translator.translate(sub.text.replace('\n', ' '))
    
    # Crea un nuevo objeto SRTSubtitle con el subtítulo traducido y la información de tiempo del subtítulo original
    translated_sub = pysrt.SubRipItem(index=sub.index, start=sub.start, end=sub.end, text=translated_text)
    
    print(translated_sub)
    # Agrega el subtítulo traducido a la lista
    translated_subs.append(translated_sub)

# Guarda los subtítulos traducidos en un nuevo archivo SRT
pysrt.SubRipFile(translated_subs).save('archivo_traducido.srt')
