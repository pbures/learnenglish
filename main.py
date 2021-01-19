from optparse import OptionParser
from playsound import playsound
import random
import os
import sys
from signal import signal, SIGINT
from sys import exit
import requests

def say_word(word):
    filename = ("mp3/%s.mp3") % word.replace("?","_").replace("!","_")

    if not os.path.exists("mp3"):
        os.makedirs("mp3")

    if not os.path.isfile(filename):
        url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={word}&tl=en&ttsspeed=1&total=1&idx=0&client=tw-ob"
        doc = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(doc.content)

    playsound(filename)

def playwtf():
    playsound(("wav/wtf%i.wav") % random.randint(1,3))

def ask_word(cesky, anglicky):

    bads = 0
    asks = 0

    while True:
        ans = input(("%s: ") % cesky)
        ans = ans.strip().lower()
        if ans == anglicky:
            say_word(anglicky)
            return (bads, asks)
        else:
            if (ans != '?'):
                playwtf()
                bads += 1
            if (bads >= 2 or ans == '?'):
                print(("Spravne je to: %s") % anglicky)
                say_word("Correct answer is")
                say_word(anglicky)
                if ans == '?' :
                    asks += 1
                if bads > 1:
                    bads = 1
                return (bads, asks)

def ask_index(index, score):
    (good,bad,asked) = score
    cesky = keys[index]
    anglicky = slovnik[cesky].strip().lower()

    (bads, asks) = ask_word(cesky, anglicky)
    bad += bads
    asked += asks
    if (asks == 0 and bads == 0):
        good += 1
    repeat = False
    if bads > 0:
        repeat = True

    print(("GOOD: %i, BAD: %i, ASKED: %i") % (good,bad,asked))
    return (good,bad,asked,repeat)

def handler(signal_received, frame):
    # Handle any cleanup here
    say_word("Ok so you give up. I hope to see you later you lazy dog!")
    exit(0)

# Tell Python to run the handler() function when SIGINT is recieved
signal(SIGINT, handler)

class Lekce:
    def __init__(self, name, slovicka):
        self.slovicka = slovicka
        self.name = name


def vylistuj_lekce(lekce):
    out = ""
    x = 0
    for l in lekce:
        out += ("-l%i...%s, " % (x,l.name))
        x += 1

    return out

lekce_kaja1 = Lekce("Kaja 1. lekce",
    {
        'Jedna': 'One',
        'Dvě': 'Two',
        'Tři': 'Three',
        'Čtyři': 'Four',
        'Pět': 'Five',
        'Šest': 'Six',
        'Sedm': 'Seven',
        'Osm': 'Eight',
        'Devět': 'Nine',
        'Deset': 'Ten',
        'Pes':'dog',
        'Auto':'car',
        'Kytara':'guitar',
        'Červená':'red',
        'Zelená':'green',
        'Modrá':'blue',
        'Žlutá':'yellow',
        'Bílá':'white',
        'Černá':'black',
        'Já':'I',
        'Ty':'You',
        'On':'he',
        'Ona':'she',
        'Ono':'it',
        'My':'we',
        'Vy':'you',
        'Oni':'they',
        'Zahrada':'garden',
        'Květina':'flower',
        'Pomeranč':'orange'
    }
)

lekce_adam1 = Lekce(
    "Adam 1. lekce",
    {
        'bát se':'afraid',
        'živý':'alive',
        'pořad o zvířatech':'animal programme',
        'výtvarná výchova':'art',
        'zadní':'back',
        'špatný':'bad',
        'košíková':'basketball',
        'koupelna':'bathroom',
        'pláž':'beach',
        'postel':'bed',
        'děti':'children',
        'tanec nebo tančit':'dance',
        'potápět se':'dive',
        'dělat':'do',
        'fotbal':'football'
    },
)

lekce_adam2 = Lekce("Adam 2. lekce",
    {
        'hokej':'hockey',
        'kilometr':'kilometre',
        'olympijský':'Olympic',
        'jezdit na kole':'ride a bike',
        'běhat':'run',
        'zpívat':'sing',
        'bruslit':'skate',
        'lyžovat':'ski',
        'zastavit':'stop',
        'plavat':'swim',
        'tam':'there',
        'triatlon':'triathlon',
        'chodím na procházky':'I go walking'
    }
)

lekce_adam3 = Lekce("Adam 3. lekce", 
    {
        'kde':'where',
        'z (neceho)':'from',
        'Německo':'Germany',
        'toto':'this',
        'manželka':'wife',
        'moje':'my',
        'jejich':'their',
        'vdaný, ženatý':'married',
        'syn':'son',
        'synovo':'son\'s',
        'britský':'british',
        'dnes':'today',
        'její':'her',
        'jeho':'his',
        'lidé':'people',
        'starý':'old',
        'tady':'here',
        'Spojené Státy':'united states',
        'velký':'large',
        'země':'country',
        'kde':'where',
        'peníze':'money',
        'každý':'everybody',
        'domov':'home',
        'doma':'at home',
    }
)

lekce_artem1 = Lekce("Artem 1. lekce",
    {
        'jsi (ty) mladý?':'are you young?',
        'jak říci':'how to say',
        'je mi teplo':'I am warm',
        'promiňte!':'excuse me!',
        'kdo jsi':'who are you',
        'kluk':'boy',
        'holka':'girl',
        'obraz':'picture',
        'mrak':'cloud',
        'nebe':'sky',
        'slunce':'sun',
        'dům':'house',
        'okno':'window',
        'sůl':'salt',
        'televize':'tv',
        'pohovka':'sofa',
        'stěna':'wall',
        'já jsem':'I am',
        'ty jsi':'you are',
        'on je':'he is',
        'ona je':'she is',
        'ono je':'it is',
        'oni jsou':'they are',
        'vy jste':'you are',
        'my jsme':'we are',
        'šťastný':'happy',
        'smutný':'sad',
        'dobrý':'good',
        'špatný':'bad',
        'silný':'strong',
        'slabý':'weak',
        'chytrý':'clever',
        'hloupý':'stupid',
        'vysoký':'tall',
        'krátký':'short',
        'malý':'small',
        'velký':'big'
    }
)

lekce_adam4s = Lekce("Skola domaci vyucovani slovicka 2",
    {
        'možná':'maybe',
        'chytrý':'clever',
        'hnusný':'vile',
        'smradlavý':'stinking',
        'tvoje':'your',
        'moje':'my',
        'její':'her',
        'jeho':'his',
        'jejich':'their',
        'nebo':'or',
        'virus':'virus',
        'hloupý':'stupid',
        'trefa':'shot',
        'jako':'like',
        'satelit':'satelite',
        'teplo':'warm',
        'přinést':'bring',
        'ukázat':'show',
        'něco':'something',
        'kde':'where',
        'někdo':'somebody',
        'stůl':'table',
        'kuchyň':'kitchen',
        'bratr':'brother',
        'rodiče':'parents',
        'starý':'old',
        'obývák':'living room',
        'narozeniny':'birthday',
        'kdy':'when',
        'tužka':'pencil',
        'sekera':'axe',
        'krompáč':'pickaxe',
        'večer':'evening',
        'odpoledne':'afternoon',
        'ráno':'morning',
        'venku':'outside',
        'co':'what',
        'ruka':'hand',
        'ložnice':'bedroom',
        'město(velké)':'city',
        'ženatý':'married',
        'které':'which',
        'létat':'fly',
        'velice':'very',
        'moc':'much'
    }
)

lekce_adam4f = Lekce("Skola domaci vyucovani fráze 2",
    {
        'já chci':'I want',
        'já mohu létat':'I can fly',
        'kdo je to?':'who is it?',
        'jak se máš?':'how are you?',
        'kde je moje tužka?':'where is my pencil?',
        'to je na stole':'it is on the table',
        'kde jsou tvojí rodiče?':'where are your parents?',
        'jak starý je tvůj bratr?':'how old is your brother?',
        'je mu dvacet pět':'he is twenty-five',
        'kdy máš narozeniny':'when is your birthday',
        'zima (myšleno roční období)':'winter',
        'zima (myšleno teplotou)':'cold',
        'co je v tvé ruce?':'what is in your hand?',
        'dobrý den':'good day',
        'rád tě poznávám (potěšen tě potkat)':'pleased to meet you',
        'rád tě poznávám (hezké tě potkat)':'nice to meet you',
        'kde žiješ?':'where do you live?',
        'žiju v česku':'I live in czechia',
        'v Praze':'in Prague',
        'jaká je tvoje adresa?':'what is your address?',
        'děkuji ti':'thank you',
        'jaká je tvoje práce?':'what is your job?',
    }
)

lekce_adam3s = Lekce("Skola Lekce 3",
    {
        'kola':'cola',
        'studený':'cold',
        'doktor':'doctor',
        'ne':'no',
        'pít':'drink',
        'nápoj':'drink',
        'jíst':'eat',
        'ovoce':'fruit',
        'jít do postele':'go to bed',
        'jít spát':'go to bed',
        'bolest hlavy':'headache',
        'zdravý':'health',
        'hodně (lots of)':'lots of',
        'hlasitý':'loud',
        'hudba':'music',
        'venku':'outside',
        'bolest v krku':'sore throat',
        'bolest žaludku':'stomach ache',
        'sladkosti':'sweets',
        'voda':'water',
        'co se děje':'what is the matter',
    },
)

lekce_kaja2 = Lekce("Lekce Kaja 2",
    {
        'letadlo':'aeroplane',
        'odpoledne':'afternoon',
        'a':'and',
        'rozzlobený':'angry',
        'zvíře':'animal',
        'jablko':'apple',
        'taška':'bag',
        'velký':'big',
        'pták':'bird',
        'kniha':'book',
        'chlapec':'boy',
        'kočka':'cat',
        'třída (jako ve škole)':'classroom',
        'hodiny':'clock',
        'krokodýl':'crocodile',
        'pes':'dog',
        'slon':'elephant',
        'oblíbený':'favourite',
        'ryba':'fish',
        'čtrnáct':'fourteen',
        'žirafa':'giraffe',
        'děvče':'girl',
        'tráva':'grass',
        'tady máte':'here you are',
        'hroch':'hippo',
        'je to?':'is it?',
        'to je':'it is',
        'listy':'leaves',
        'lev':'lion',
        'malý (l.....)':'little',
        'opice':'monkey',
        'myš':'mouse',
        'pštros':'ostrich',
        'papoušek':'parrot',
        'pero':'pen',
        'penál':'pencil case',
        'tužka':'pencil',
        'tučnák':'penguin',
        'ukázat na (p.... ..)':'point to',
        'prosím':'please',
        'guma':'rubber',
        'pravítko':'ruler',
        'posaďte se':'sit down',
        'had':'snake',
        'stoupněte si':'stand up',
        'tam jsou':'there are',
        'tam je':'there is',
        'co je toto?':'what is this?',
        'toto':'this',
        'to':'it',
        'tyto':'these',
        'křídla':'wings'
    }
)

lekce_adam5s = Lekce("Lekce Adam 4",
    {
        'knihkupectví':'bookshop',
        'kavárna':'cafe',
        'hrad':'castle',
        'kostel':'church',
        'kino':'cinema',
        'obchod s oděvy':'clothes shop',
        'promiňte':'excuse me',
        'jít rovně kolem':'go straight past',
        'hotel':'hotel',
        'obchod (m.....)':'market',
        'muzeum':'museum',
        'vedle':'next to',
        'naproti':'opposite',
        'část':'part',
        'škola':'school',
        'sportovní centrum':'sports centre',
        'náměstí':'square',
        'superkmarket':'supermarket',
        'věž':'tower',
        'zatoč vlevo (at)':'turn left at',
        'vesnice':'village',
        'socha':'statue',
        'tusks':'kly'
    }
)

lekce_adam10 = Lekce("Adam 10", 
    {
        'ahoj':'hello',
        'knihkupectví':'bookshop',
        'kavárna':'cafe',
        'hrad':'castle',
        'kostel':'church',
        'kino':'cinema',
        'mněsto':'city',
        'elektrické piáno':'electric piano',
        'babibo[babibo]':'babibo',
        'obchod s oblecenim':'clothes shop',
        'milý':'dear',
        'prominte':'excuse me',
        'padá':'falling',
        'fantastický':'fantastic',
        'živící se rybami[***h eater]':'fish eater',
        'dovolená':'holiday',
        'já skáču':'I am jumping',
        'točit':'spin',
        'palma':'palm tree',
        'básen':'poem',
        'hraje':'plaing',
        'píše':'writing'
        'pipapo':'pipapo'
        'pipapoli':'pipapoli'
        'bibo':'bibo'

    }
)

lekce = [ lekce_kaja1, lekce_adam1, lekce_adam2, lekce_adam3, lekce_artem1, lekce_adam4s, lekce_adam4f, lekce_adam3s, lekce_kaja2, lekce_adam5s, lekce_adam10 ]



parser = OptionParser(usage="anglictina.py [ -l <num> [ -l <num> [...]]]")
parser.add_option("-l", "--lesson", dest="lesson", action="append", type="int",
                  help="List of lessons to try. Use multiple -l parameters. Lessons availabe are:\n %s" % (vylistuj_lekce(lekce)))

(options, args) = parser.parse_args()

if not options.lesson:
    lessons = [i for i in range(3)]
else:
    lessons = options.lesson

slovnik = {}

for l in lessons:
    if l > len(lekce)-1 :
        print("Sorry, we don't have lesson number %i" % (l))
        exit(1)
    slovnik = {**slovnik, **(lekce[l].slovicka)}

keys = list(slovnik.keys())

indices = [ i for i in range(len(keys))]
random.shuffle(indices)

repeats = []
(good,bad,asked) = (0,0,0)

while True:
    for ind in indices:
        (good,bad,asked,repeat)= ask_index(ind, (good,bad,asked))
        if repeat:
            repeats.append(ind)

    if repeats:
        random.shuffle(repeats)
        indices = repeats
        repeats = []
    else:
        say_word("GOOD JOB MAN!")
        break



