"""

"""


from enum import auto
from runesanalyzer.utils import AutoName


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]

POINT = "᛫"
SEMI_COLUMN = "\u16EC"


class RunicAlphabetName(AutoName):
    elder_futhark = auto()
    younger_futhark = auto()
    short_twig_younger_futhark = auto()


class Rune:
    def __init__(self, runic_alphabet: RunicAlphabetName, form: str, sound: str, transcription: str, name: str):
        self.runic_alphabet = runic_alphabet
        self.form = form
        self.sound = sound
        self.transcription = transcription
        self.name = name

    @staticmethod
    def display_runes(runic_alphabet: list):
        return [rune.form for rune in runic_alphabet]

    @staticmethod
    def from_form_to_transcription(form: str, runic_alphabet: list):
        d_form_transcription = {rune.form: rune.transcription for rune in runic_alphabet}
        return d_form_transcription[form]

    def __repr__(self):
        return self.form

    def __str__(self):
        return self.form

    def __eq__(self, other):
        return self.form == other


class Transcriber:
    def __init__(self):
        pass

    @staticmethod
    def from_form_to_transcription(runic_alphabet: list):
        return {rune.form: rune.transcription for rune in runic_alphabet}

    @staticmethod
    def transcribe(rune_sentence: str, runic_alphabet: list):
        res = []
        d_form_transcription = Transcriber.from_form_to_transcription(runic_alphabet)
        for c in rune_sentence:
            if c in runic_alphabet:
                res.append(d_form_transcription[c])
            elif c in "()":
                res.append(c)
            else:
                res.append(POINT)
        return "".join(res)
