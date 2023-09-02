import pygame
import random
import time


def play_random_beez(minute, list_of_random):
    i = 0
    count = 0
    while i < (minute * 60):
        if i == list_of_random[count]:
            pygame.mixer.music.play()
            pygame.event.wait()
            count += 1

        print("**")
        print("Seconds: %d" % i)
        print("Minutes: %d" % (i / 60))
        print("**")

        print(i, list_of_random[count])

        time.sleep(1)
        i += 1


def remove_near(list_of_random):
    temp = []
    i = 0
    while i < len(list_of_random) - 1:
        if list_of_random[i + 1] - list_of_random[i] >= 180:
            temp.append(list_of_random[i])
        i += 1

    return temp


def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("sound.mp3")

    list_of_random = []
    minute = 90

    i = 0
    while i < 30:
        random_int = random.randint(180, minute * 60)
        if random_int not in list_of_random:
            list_of_random.append(random_int)
            i += 1

    list_of_random = remove_near(sorted(list_of_random))
    print(list_of_random)
    play_random_beez(minute, list_of_random)


main()
