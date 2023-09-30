import random
import threading
import time

import pynput


class Main:
    def __init__(self):
        self.chat_key = "/"
        self.F1_Phrase = "trash"
        self.F2_Phrase = "easy :)"
        self.F3_Phrase = "dead lol"
        self.F4_Phrase = "bad?"
        self.phrases = []
        self.last_phrase = ""

        with open("phrases.txt") as phrases_file:
            for line in phrases_file:
                self.phrases.append(line.strip())

    def say(self, string):
        pynput.keyboard.Controller().tap(key=self.chat_key)
        time.sleep(0.05)
        pynput.keyboard.Controller().type(string)
        time.sleep(0.05)
        pynput.keyboard.Controller().tap(pynput.keyboard.Key.enter)

    def random_phrase(self):
        if len(self.phrases) != 0:
            self.phrase_index = random.randint(0, len(self.phrases) - 1)
            phrase = self.phrases[self.phrase_index]

            if self.last_phrase.lower() == phrase.lower():
                if len(self.phrases) > 1:
                    if self.phrase_index == 0:
                        phrase = self.phrases[self.phrase_index + 1]
                    elif self.phrase_index == len(self.phrases) - 1:
                        phrase = self.phrases[self.phrase_index - 1]
                    else:
                        phrase = self.phrases[self.phrase_index + 1]

            random_number = random.randint(0, 2)

            if random_number == 0:
                phrase = phrase.lower()
            elif random_number == 1:
                phrase = phrase.upper()
            else:
                phrase = phrase.title()

            self.say(phrase)
            self.last_phrase = phrase

    def on_press(self, key):
        if str(key) == "Key.f1":
            self.say(self.F1_Phrase)
        elif str(key) == "Key.f2":
            self.say(self.F2_Phrase)
        elif str(key) == "Key.f3":
            self.say(self.F3_Phrase)
        elif str(key) == "Key.f4":
            self.say(self.F4_Phrase)
        elif str(key) == "Key.f8":
            self.random_phrase()

    def main_loop(self):
        input("type something to quit > ")


def keyboard_listener(main):
    with pynput.keyboard.Listener(on_press=lambda key: main.on_press(key)) as keyboard_listener:
        keyboard_listener.join()


def main():
    main = Main()
    keyboard_listener_thred = threading.Thread(target=keyboard_listener, args=(main,))
    keyboard_listener_thred.daemon = True
    keyboard_listener_thred.start()
    main.main_loop()


if __name__ == "__main__":
    main()
