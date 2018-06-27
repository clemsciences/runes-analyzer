"""
Sources:
- Viking Language 1 by Jessie L. Byock 2013

Some mistakes may be remaining

Unicode: 16A0–16FF

"""
from enum import auto
from utils import AutoName


POINT = "᛫"


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


# There are probably some mistakes
# Precisions are expected
# ᚠ ᚢ ᚦ ᚨ ᚲ ᚱ ᚷ ᚹ ᚼ ᚾ ᛁ ᛃ ᛇ ᛈ ᛉ ᛊ ᛏ ᛒ ᛖ ᛗ ᛚ ᛜ ᛟ ᛞ
ELDER_FUTHARK = [
    Rune(RunicAlphabetName.elder_futhark, "\u16A0", "f", "f", "fehu"),
    Rune(RunicAlphabetName.elder_futhark, "\u16A2", "u", "u", "uruz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16A6", "θ", "þ", "þuriaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16A8", "a", "a", "ansuz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16B1", "r", "r", "raido"),
    Rune(RunicAlphabetName.elder_futhark, "\u16B2", "k", "k", "kaunan"),
    Rune(RunicAlphabetName.elder_futhark, "\u16B7", "g", "g", "gyfu"),
    Rune(RunicAlphabetName.elder_futhark, "\u16B9", "w", "w", "wynn"),

    Rune(RunicAlphabetName.elder_futhark, "\u16BA", "h", "h", "haglaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16BE", "n", "n", "naudiz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16C1", "i", "i", "isaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16C3", "j", "j", "jeran"),
    Rune(RunicAlphabetName.elder_futhark, "\u16C7", "æ", "E", "eiwaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16C8", "p", "p", "peorð"),
    Rune(RunicAlphabetName.elder_futhark, "\u16C9", "ʀ", "r", "algiz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16CA", "s", "s", "sowilo"),

    Rune(RunicAlphabetName.elder_futhark, "\u16CF", "t", "t", "tiwaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16D2", "b", "b", "berkanan"),
    Rune(RunicAlphabetName.elder_futhark, "\u16D6", "e", "e", "ehwaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16D7", "m", "m", "mannaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16DA", "l", "l", "laguz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16DC", "ŋ", "ng", "ingwaz"),
    Rune(RunicAlphabetName.elder_futhark, "\u16DF", "ø", "œ", "odal"),
    Rune(RunicAlphabetName.elder_futhark, "\u16DE", "d", "d", "dagaz"),
]

YOUNGER_FUTHARK = [
    Rune(RunicAlphabetName.younger_futhark, "\u16A0", "f", "f", "fehu"),
    Rune(RunicAlphabetName.younger_futhark, "\u16A2", "u", "u", "uruz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16A6", "θ", "þ", "þuriaz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16AD", "a", "a", "ansuz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16B1", "r", "r", "raido"),
    Rune(RunicAlphabetName.younger_futhark, "\u16B4", "k", "k", "kaunan"),

    Rune(RunicAlphabetName.younger_futhark, "\u16BC", "h", "h", "haglaz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16BE", "n", "n", "naudiz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16C1", "i", "i", "isaz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16C5", "a", "a", "jeran"),
    Rune(RunicAlphabetName.younger_futhark, "\u16CB", "s", "s", "sowilo"),

    Rune(RunicAlphabetName.younger_futhark, "\u16CF", "t", "t", "tiwaz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16D2", "b", "b", "berkanan"),
    Rune(RunicAlphabetName.younger_futhark, "\u16D6", "e", "e", "ehwaz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16D8", "m", "m", "mannaz"),  # also \u16D9
    Rune(RunicAlphabetName.younger_futhark, "\u16DA", "l", "l", "laguz"),
    Rune(RunicAlphabetName.younger_futhark, "\u16E6", "r", "R", "algiz")
]


SHORT_TWIG_YOUNGER_FUTHARK = [
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16A0", "f", "f", "fehu"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16A2", "u", "u", "uruz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16A6", "θ", "þ", "þuriaz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16AD", "a", "a", "ansuz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16B1", "r", "r", "raido"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16B4", "k", "k", "kaunan"),

    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16BD", "h", "h", "haglaz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16BF", "n", "n", "naudiz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16C1", "i", "i", "isaz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16C5", "a", "a", "jeran"),  # not good
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16CC", "s", "s", "sowilo"),

    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16D0", "t", "t", "tiwaz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16D3", "b", "b", "berkanan"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16D6", "e", "e", "ehwaz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16D9", "m", "m", "mannaz"),  # also \u16D9
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16DA", "l", "l", "laguz"),
    Rune(RunicAlphabetName.short_twig_younger_futhark, "\u16E7", "r", "R", "algiz"),
]


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
            else:
                res.append(POINT)
        return "".join(res)


if __name__ == "__main__":
    print(" ".join(Rune.display_runes(ELDER_FUTHARK)))
    print(" ".join(Rune.display_runes(YOUNGER_FUTHARK)))
    print(" ".join(Rune.display_runes(SHORT_TWIG_YOUNGER_FUTHARK)))

    # https://sv.wikipedia.org/wiki/Upplands_runinskrifter_937
    inscription = "ᚦᛁᛅᚴᚾ᛫ᛅᚢᚴ᛫ᚴᚢᚾᛅᚱ᛫ᚱᛅᛁᛋᛏᚢ᛫ᛋᛏᛅᛁᚾᛅ ᛅᚠᛏᛁᛦ᛫ᚢᛅᚱ᛫ᛒᚱᚢᚦᚢᚱ᛫ᛋᛁᚾ"
    print(inscription)
    print(Transcriber.transcribe(inscription, YOUNGER_FUTHARK))
