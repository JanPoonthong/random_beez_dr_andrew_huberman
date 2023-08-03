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
    gap = 10 * 60
    total_amount_of_beez = 30

    i = 0
    while i < total_amount_of_beez:
        random_int = random.randint(0, minute * 60)

        if len(list_of_random) > 0:
            while (
                abs(random_int - list_of_random[i - 1]) <= gap
                or random_int < list_of_random[i - 1]
            ):
                random_int = random.randint(0, minute * 60)
                if (
                    abs(random_int - list_of_random[i - 1]) > gap
                    and random_int > list_of_random[i - 1]
                ):
                    if random_int not in list_of_random:
                        list_of_random.append(random_int)
                        i += 1
                        list_of_random = sorted(list_of_random)
                        break

            if random_int not in list_of_random:
                list_of_random.append(random_int)
                list_of_random = sorted(list_of_random)
                i += 1
        else:
            list_of_random.append(random_int)
            i += 1

    for i in list_of_random:
        print(i/60, end=",")
    list_of_random = sorted(list_of_random)
    play_random_beez(minute, list_of_random)


main()
