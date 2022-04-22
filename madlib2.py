from random import randint
import copy

story = (
    "Suatu hari saya {} teman  dan saya memutuskan untuk pergi {} permainan di {}. "+
    "Kami benar-benar ingin melihat {} memainkan {}. Jadi, kami {} {} kita "+ 
    "ke {} dan membeli beberapa {}. Kami masuk ke dalam permainan dan "+
    "itu sangat menyenangkan. Kami makan {} {} dan minum {} {}. "+
    "Kami bersenang-senang! Kami berencana untuk pergi lagi tahun depan!"
)

word_dict = {
    'adjective':['tamak', 'kasar', 'kotor', 'asik', 'kaya', 'kasar', 'lezat', 'santai'], 
    'city name':['Jakarta',' Surabaya','Bandung','Banten','Bogor','Tanggerang'], 
    'noun':['orang','map','musik','anjing','hamster','bola','hotdog','salad'], 
    'action verb':['lari','gagal','merangkak','bergegas','nangis','nonton','renang','lompat','melambung'], 
    'sports noun':['bola','mit','keping','seragam','helm','papan angka','player']
}

def get_word(type, local_dict):
    ''' get a random word from the word_dict based on word type '''
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    ''' create a random story from word dict '''
    # create a local copy of the dict so that we can pop words as used
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict), 
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
)

print("Cerita 1: ")
print(create_story())
print()
print("Cerita 2: ")
print(create_story())