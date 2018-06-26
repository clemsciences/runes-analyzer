"""
Sources:
- Viking Language 1 by Jessie L. Byock 2013

Some mistakes may be remaining

Unicode: 16A0–16FF

"""
from enum import auto
from utils import AutoName


class RunicAlphabet(AutoName):
    elder_futhark = auto()
    younger_futhark = auto()


class Rune:
    def __init__(self, runic_alphabet: RunicAlphabet, form: str, sound: str, transcription: str, name: str):
        self.runic_alphabet = runic_alphabet
        self.form = form
        self.sound = sound
        self.transcription = transcription
        self.name = name

    @staticmethod
    def display_runes(runic_alphabet: list):
        for rune in runic_alphabet:
            print(rune.form)


# There are probably some mistakes
# Precisions are expected
OLD_FUTHARK = [
    Rune(RunicAlphabet.elder_futhark, "\u16A0", "f", "f", "fehu"),
    Rune(RunicAlphabet.elder_futhark, "\u16A2", "u", "u", "uruz"),
    Rune(RunicAlphabet.elder_futhark, "\u16A6", "θ", "þ", "þuriaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16A8", "a", "a", "ansuz"),
    Rune(RunicAlphabet.elder_futhark, "\u16B2", "k", "k", "kaunan"),
    Rune(RunicAlphabet.elder_futhark, "\u16B1", "r", "r", "raido"),
    Rune(RunicAlphabet.elder_futhark, "\u16B7", "g", "g", "gyfu"),
    Rune(RunicAlphabet.elder_futhark, "\u16B9", "w", "w", "wynn"),
    Rune(RunicAlphabet.elder_futhark, "\u16BC", "h", "h", "haglaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16BE", "n", "n", "naudiz"),
    Rune(RunicAlphabet.elder_futhark, "\u16C1", "i", "i", "isaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16C3", "j", "j", "jeran"),
    Rune(RunicAlphabet.elder_futhark, "\u16C7", "æ", "E", "eiwaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16C8", "p", "p", "peorð"),
    Rune(RunicAlphabet.elder_futhark, "\u16C9", "ʀ", "r", "algiz"),
    Rune(RunicAlphabet.elder_futhark, "\u16CA", "s", "s", "sowilo"),
    Rune(RunicAlphabet.elder_futhark, "\u16CF", "t", "t", "tiwaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16D2", "b", "b", "berkanan"),
    Rune(RunicAlphabet.elder_futhark, "\u16D6", "e", "e", "ehwaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16D7", "m", "m", "mannaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16DA", "l", "l", "laguz"),
    Rune(RunicAlphabet.elder_futhark, "\u16DC", "ŋ", "ng", "ingwaz"),
    Rune(RunicAlphabet.elder_futhark, "\u16DF", "ø", "œ", "odal"),
    Rune(RunicAlphabet.elder_futhark, "\u16DE", "d", "d", "dagaz"),
]


if __name__ == "__main__":
    Rune.display_runes(OLD_FUTHARK)
