import pygame, time, random, pyttsx3, speech_recognition as sr
engine = pyttsx3.init()
screen = pygame.display.set_mode((600, 700))
font = pygame.font.SysFont(None, 40)

# potion availabilities

def potions(z):

    if z == 99:
        return 'green, cyan, pink, blue'

    elif z == 98:
        return 'yellow, cyan, pink, blue'

    elif z == 97:
        return 'yellow, green, pink, blue'

    elif z == 96:
        return 'yellow, green, cyan, blue'

    elif z == 95:
        return 'yellow, green, cyan, pink'





# potion combinations
class reaction:
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



def flash(a, b):
    for i in range(a):
        screen.fill((0, 0, 0))
        pygame.display.update()
        time.sleep(b)
        screen.fill((255, 255, 255))
        pygame.display.update()
        time.sleep(b)



def say(what):
    engine.say(what)
    # show the words on the screen for 5 seconds before clearing the screen again 
    
    #def message_to_screen(msg, color, size, x, y):

    screen_text = font.render("CC: " + str(what), True, (0, 0, 0))
    screen.blit(screen_text, [100, 600])
    pygame.display.update()
    time.sleep(2)
    engine.runAndWait()



def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        #print('You said: {}'.format(text))
        return text
    except sr.UnknownValueError:
        print('Could not understand audio')
    except sr.RequestError as e:
        print('Could not request results; {0}'.format(e))