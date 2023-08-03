#!/usr/bin/env python3
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


def main():
    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load("sound.mp3")

    list_of_random = []
    minute = 90
    gap = 3 * 60
    total_amount_of_beez = 30

    i = 0
    random_int = gap
    while i < total_amount_of_beez:
        if random_int >= minute * 60:
            break
        random_int = random.randint(random_int, random_int + gap)
        if len(list_of_random) == 0:
            list_of_random.append(random_int)
        elif abs(random_int - list_of_random[i]) > gap:
            list_of_random.append(random_int)
            i += 1

    # play_random_beez(minute, list_of_random)


main()
