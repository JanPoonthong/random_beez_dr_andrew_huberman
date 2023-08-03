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
    count = 1
    random_int = gap
    while i < total_amount_of_beez:
        if random_int >= minute * 60:
            break
        random_int = random.randint(random_int, random_int + 10)

        if len(list_of_random) > 0:
            while random_int < list_of_random[i - 1]:
                random_int = random.randint(0, minute * 60)
                if random_int > list_of_random[i - 1]:
                    if random_int not in list_of_random:
                        list_of_random.append(random_int)
                        count += 1
                        i += 1
                        break

            if random_int not in list_of_random:
                list_of_random.append(random_int)
                i += 1
        else:
            list_of_random.append(random_int)
            count += 1
            i += 1

    print(list_of_random)
    # play_random_beez(minute, list_of_random)


main()
