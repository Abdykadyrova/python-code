
languages = {
    'ru': {
        'go': 'идти',
        'think': 'Думать',
        'friend': 'Друг',
        'we': 'Мы',
        'edit': 'Изменить',
        'view': 'просмотр',
        'run': 'Бегать',
        'room': 'комната',
        'i': 'я',
        'number': 'число',
        'it': 'оно',
        'she': 'Она',
        'he': 'Он',
    },
    'en': {
        'идти': 'Go'
    },
    'kg': {
        'go': 'басуу',
        'think': 'Ойлонуу',
        'friend': 'Друг',
        'we': 'Биз',
        'edit': 'Озгортуу',
        'view': 'Коруу',
        'run': 'Чуркоо',
        'room': 'Болмо',
        'i': 'Мен',
        'number': 'Сан',
        'it': 'бул',
        'she': 'Аял',
        'he': 'Эркек',
    }
}
def to_translate(word, code):
    word_to_lower = word.lower()
    if code in languages:
       if word in languages[code]:
            print(
                word, 
                'На', code, 'языке', 
                languages[code][word_to_lower]
            )

def to_translate_many(*args,**kwargs):
    for a in args:
        to_translate(a,kwargs['lang'])


to_translate_many('go','eat','run','she','he',lang = 'kg')