start_symbol = 'K'
dic = {}


def display(get_dic):
    for i in get_dic:
        print(i, '-->', end='')
        print(*get_dic[i], sep='|')
        print()


def insert_grammar():
    global dic
    cfg = [
        'K > S P Pel | S P O | S P O Pel | S P Pel Ket',
        'S > NP',
        'P > VP',
        'O > PP',
        'Pel > PP',
        'Ket > PP',
        'NP > NP Pronoun | NP Noun | Noun | Noun NP | PropNoun | NP PropNoun | NP Verb | Pronoun | NP Adj | Noun PP',
        'AdjP > AdjP Adv | Adj',
        'VP > Adv VP | Verb | AdjP Verb | Verb VP | Verb PP',
        'PP > Prep NP',
        'Adj > baru | malang',
        'Adv > saja | sedang | selalu | sudah | tidak',
        'Noun > baju | bapak | bayi | seorang | penculik | sungai | gelas | dapur | adik | guru | kakak | ayam | ibu '
        '| rambut | lukisan | meja | pak | tukang | kayu | mobil | ayah | paman | pencuri | perhiasan | polisi | '
        'pintu | pohon | pinus | relawan | pecinta | alam | sampah | sepeda | tanaman',
        'Prep > di | oleh | karena',
        'Pronoun > aku | dia | itu | kami | saya',
        'PropNoun > Ani | Mona Lisa | Leonardo Da Vinci | Olah-raga',
        'Verb > belajar | dipasang | bisa | mengendarai | diajarkan | dibersihkan | dibuang | dibuka | didorong | '
        'mogok | dilukis | dimarahi | membangkang | dimasak | dipecahkan | disetrika | disiram | ditanam | ditangkap '
        '| ditarik',
    ]

    for i in range(len(cfg)):
        lhs = cfg[i].split(' > ')[0]
        rhs = set(cfg[i].split(' > ')[1].split(' | '))
        dic.update({lhs: list(rhs)})

insert_grammar()
