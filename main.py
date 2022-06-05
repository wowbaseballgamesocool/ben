
import random
import time
import socket
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()


''' recording the sound '''
def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)
        print('Done!')
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
        return text
    except sr.UnknownValueError:
        print('Could not understand audio')
    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))

global z
global choice
global words

x = 1
y = 1

potion_choice = 'yellow, green, cyan, pink, blue'


# potion availabilities

def potions():
    global potion_choice

    if z == 99:
        potion_choice = 'green, cyan, pink, blue'

    elif z == 98:
        potion_choice = 'yellow, cyan, pink, blue'

    elif z == 97:
        potion_choice = 'yellow, green, pink, blue'

    elif z == 96:
        potion_choice = 'yellow, green, cyan, blue'

    elif z == 95:
        potion_choice = 'yellow, green, cyan, pink'


# potion combinations

def fire():
    print('*fire comes out of pot*')


def black_ben():
    print('black ben')


def ben_vapes():
    print('ben vapes')


def volcano():
    print('volcano')


def macaroni_fire():
    print('macaroni fire')


def explodes_pot():
    print('explodes pot')


def plant_monster():
    print('plant monster')


def ben_drinks_lean():
    print('ben drinks lean')


def thunderstorm():
    print('thunderstorm')


def lean_tornado():
    print('LEANADO')


# start of game

print('"news paper opens"')

time.sleep(1)

while True:

    # newspaper

    if x == 1:

        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 400

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source, duration=1)

            recorded_audio = recognizer.record(source, duration=2)


        ''' Recorgnizing the Audio '''
        try:
            choice = recognizer.recognize_google(
                recorded_audio,
                language="en-US"
            )

        except Exception as ex:
            print(ex)

        print(choice)


        if 'phone' in choice:
            x = 2

        elif 'talk' in choice:
            x = 3

        elif 'lab' in choice:
            x = 4

        elif 'more apps' in choice:
            x = 5

        else:

            if random.randint(1, 2) == 1:
                # convert this text to speech
                text = "Na Na Na Na"
                engine.say(text)
                # play the speech
                engine.runAndWait()


            else:
                # convert this text to speech
                text = "Shut up"
                engine.say(text)
                # play the speech
                engine.runAndWait()

    # phone

    elif x == 2:

        if y == 1:
            print('"news paper closes"')

        if y == 3:
            print('"goggles taken off"')

        print('"gololgaling"')

        time.sleep(1)

        print('Ben')

        while True:

            recognizer = sr.Recognizer()
            recognizer.energy_threshold = 400

            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(source, duration=1)

                recorded_audio = recognizer.record(source, duration=4)

            ''' Recorgnizing the Audio '''
            try:
                question = recognizer.recognize_google(
                    recorded_audio,
                    language="en-US"
                )

            except Exception as ex:
                print(ex)

            print(question)

            answer = random.randint(1, 3)

            if question == 'talk':
                y = 2
                x = 3
                break

            elif question == 'lab':
                x = 4
                y = 2
                break

            elif question == 'more apps':
                x = 5
                break

            else:

                if answer == 1:

                    chance = random.randint(1, 5)

                    if chance == 1:
                        # convert this text to speech
                        text = "Gender: female, Race: White, Birthday: 1/8/1989 (33 years old), Street: 3344 Lakeland Park Drive City, State, Zip: Roswell, Georgia(GA), 30075 Telephone: 770-643-6809 Mobile: 912-978-0482"
                        engine.say(text)
                        # play the speech
                        engine.runAndWait()

                    else:

                        # convert this text to speech
                        text = "Yes"
                        engine.say(text)
                        # play the speech
                        engine.runAndWait()

                elif answer == 2:

                    # convert this text to speech
                    text = "No"
                    engine.say(text)
                    # play the speech
                    engine.runAndWait()

                elif answer == 3:
                    # convert this text to speech
                    text = "Hohoho"
                    engine.say(text)
                    # play the speech
                    engine.runAndWait()

    # talk

    elif x == 3:

        if y == 1:
            print('"news paper closes"')

        if y == 2:
            print('"puhcling"')

        if y == 3:
            print('"goggles taken off"')

        while True:

            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(source, duration=0.1)

                recorded_audio = recognizer.record(source, duration=3)



            ''' Recorgnizing the Audio '''
            try:
                words = recognizer.recognize_google(
                    recorded_audio,
                    language="en-US"
                )

            except Exception as ex:
                print(ex)

            if 'face' in words:
                # convert this text to speech
                text = "Wumpaflump"
                engine.say(text)
                # play the speech
                engine.runAndWait()

            elif 'stomach' in words:
                print('BUM POO')

            elif 'arm' in words:
                print('WEERP')

            elif 'leg' in words:
                print('WOOMP')

            elif words == 'drink':
                print('hmmm *wumpaflump*')
                gulp_amount = random.randint(1, 5)
                if gulp_amount == 1:
                    print('GULP')
                    print('GULP')
                    print('GULP')

                elif gulp_amount == 2:
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')

                elif gulp_amount == 3:
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')

                elif gulp_amount == 4:
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')

                elif gulp_amount == 5:
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                    print('GULP')
                print('auggh *chickclccl*')

            elif words == 'beans':
                print('hmm *picks up beans*')
                gulpsculp = random.randint(1, 5)
                if gulpsculp == 1:
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                elif gulpsculp == 2:
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                elif gulpsculp == 3:
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                elif gulpsculp == 4:
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                elif gulpsculp == 5:
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('GULPASCULP')
                    print('*throws can* CHACHAHCAHHLCLLLGGNG')

            elif 'slap' in words:
                slap_noise = random.randint(0, 1)
                if slap_noise == 0:
                    print('PISH')
                else:
                    print('PISH ULGH')

            elif 'burp' in words:
                burp_noise = random.randint(0, 5)
                if burp_noise == 0:
                    print('BlUUGHGHUUHGH')
                elif burp_noise == 1:
                    print('BLUUGHH')
                elif burp_noise == 2:
                    print('BLURBFD')
                elif burp_noise == 3:
                    print('BLUGH')
                elif burp_noise == 4:
                    print('EEEEEEEEEEEEEEEEEEEEEEEEEUUUUUUUUUUUUUUUUGGHHHGH')
                elif burp_noise == 5:
                    print('BLOUUUUUUUUUUUUUAAGAAGHGA')


            elif words == 'news paper':
                x = 1
                y = 0
                break

            elif words == 'phone':
                x = 2
                y = 0
                break

            elif words == 'lab':
                x = 4
                y = 0
                break

            elif words == 'more apps':
                x = 5

            elif words == 'i am gay': 

                print("Hostname: " + socket.gethostname())
                print("IP Address: " + socket.gethostbyname(socket.gethostname()))

            elif words == 'i have a bomb':

                print('calling 911...')

            elif words == 'i like men':

                print('(´･_･`)')

            else:
                # convert this text to speech
                text = words
                engine.setProperty("rate", 75)
                engine.say(text)
                # play the speech
                engine.runAndWait()

    # lab

    elif x == 4:

        z = 100

        if y == 2:
            print('"puhcling"')
            y = 3

        print('yellow, green, cyan, pink, blue')

        pot1 = input('... ')

        if pot1 == 'yellow':
            z -= 1

            print('pshhlllllle')

            time.sleep(0.5)

            print(pot1, 'potion')

        elif pot1 == 'green':
            z -= 2

            print('pshhlllllle')

            time.sleep(0.5)

            print(pot1, 'potion')

        elif pot1 == 'cyan':
            z -= 3

            print('pshhlllllle')

            time.sleep(0.5)

            print(pot1, 'potion')

        elif pot1 == 'pink':
            z -= 4

            print('pshhlllllle')

            time.sleep(0.5)

            print(pot1, 'potion')

        elif pot1 == 'blue':
            z -= 5

            print('pshhlllllle')

            time.sleep(0.5)

            print(pot1, 'potion')

        elif pot1 == 'phone':
            y = 3
            x = 2

        elif pot1 == 'talk':
            y = 3
            x = 3

        elif pot1 == 'more apps':
            x = 5

        else:
            print('mmmnnn mmmnnn')

        potions()

        if z < 100:

            print(potion_choice)

            pot2 = input('... ')

            if pot2 == 'yellow':
                z -= 10

                print('pshhlllllle')

                time.sleep(0.5)

                print(pot2, 'potion')

            elif pot2 == 'green':
                z -= 20

                print('pshhlllllle')

                time.sleep(0.5)

                print(pot2, 'potion')

            elif pot2 == 'cyan':
                z -= 30

                print('pshhlllllle')

                time.sleep(0.5)

                print(pot2, 'potion')

            elif pot2 == 'pink':
                z -= 40

                print('pshhlllllle')

                time.sleep(0.5)

                print(pot2, 'potion')

            elif pot2 == 'blue':
                z -= 50

                print('pshhlllllle')

                time.sleep(0.5)

                print(pot2, 'potion')

            elif pot2 == 'phone':
                y = 3
                x = 2

            elif pot2 == 'talk':
                y = 3
                x = 3

            elif pot2 == 'more apps':
                x = 5

            else:
                print('mmmnnn mmmnnn')

        time.sleep(1)

        # beginning of round 1

        if z == 79:
            fire()

        if z == 69:
            black_ben()

        if z == 59:
            ben_vapes()

        if z == 49:
            volcano()

        if z == 68:
            macaroni_fire()

        if z == 58:
            explodes_pot()

        if z == 48:
            plant_monster()

        if z == 57:
            ben_drinks_lean()

        if z == 47:
            thunderstorm()

        if z == 46:
            lean_tornado()

        # beginning of round 2

        if z == 88:
            fire()

            time.sleep(1)

        if z == 87:
            black_ben()

            time.sleep(1)

        if z == 86:
            ben_vapes()

            time.sleep(1)

        if z == 85:
            volcano()

            time.sleep(1)

        if z == 77:
            macaroni_fire()

            time.sleep(1)

        if z == 76:
            explodes_pot()

            time.sleep(1)

        if z == 75:
            plant_monster()

            time.sleep(1)

        if z == 66:
            ben_drinks_lean()

            time.sleep(1)

        if z == 65:
            thunderstorm()

            time.sleep(1)

        if z == 55:
            lean_tornado()

            time.sleep(1)

    elif x == 5:

        time.sleep(1)

        if y == 1:
            print('"news paper closes"')

        if y == 2:
            print('"puhcling"')

        if y == 3:
            print('"goggles taken off"')

        time.sleep(0.5)

        print('more apps')

        time.sleep(0.5)

        print('talking bayload')

        time.sleep(0.5)

        print('aromafry is bad')

        time.sleep(1)

        print('"news paper opens"')

        y = 1
        x = 1


