import pygame
import random
import time

def play_random_beez(MINS, LIST_OF_RANDOM):

    i = 0
    count = 0
    while i < (MINS * 60):
        if i == LIST_OF_RANDOM[count]:
            pygame.mixer.music.play()
            pygame.event.wait()
            count += 1

        print("**")
        print("Seconds: %d" % i)
        print("Minutes: %d" % (i / 60))
        print("**")

        print(i, LIST_OF_RANDOM[count])

        time.sleep(1)
        i += 1

def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('sound.mp3')

    LIST_OF_RANDOM = []
    MINS = 90

    i = 0
    while i < 30:
        random_int = random.randint(0, MINS * 60)
        if random_int not in LIST_OF_RANDOM:
            LIST_OF_RANDOM.append(random_int)
            i += 1

    play_random_beez(MINS, LIST_OF_RANDOM)

main()
