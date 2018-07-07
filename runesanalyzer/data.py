"""
Sources:
- Viking Language 1 by Jessie L. Byock 2013


Unicode: 16A0–16FF
Swedish runic inscriptions
http://runes.verbix.com/index.html
http://runes.verbix.com/vikingage/Uppland.html

"""
import json
from runesanalyzer.runes import RunicAlphabetName, Rune, Transcriber

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


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


# https://fr.wikipedia.org/wiki/Petite_pierre_de_Jelling
little_jelling_stone = "᛬ᚴᚢᚱᛘᛦ᛬ᚴᚢᚾᚢᚴᛦ᛬ᚴ(ᛅᚱ)ᚦᛁ᛬ᚴᚢᛒᛚ᛬ᚦᚢᛋᛁ᛬ᛅ(ᚠᛏ)᛬ᚦᚢᚱᚢᛁ᛬ᚴᚢᚾᚢ᛬ᛋᛁᚾᛅ᛬ᛏᛅᚾᛘᛅᚱᚴᛅᛦ᛬ᛒᚢᛏ᛬"
big_jelling_stone = "ᚼᛅᚱᛅᛚᛏᚱ᛬ᚴᚢᚾᚢᚴᛦ᛬ᛒᛅᚦ᛬ᚴᛅᚢᚱᚢᛅ ᚴᚢᛒᛚ᛬ᚦᛅᚢᛋᛁ᛬ᛅᚠᛏ᛬ᚴᚢᚱᛘ ᚠᛅᚦᚢᚱ ᛋᛁᚾ ᛅᚢᚴ ᛅᚠᛏ᛬ᚦᚭᚢᚱᚢᛁ᛬ᛘᚢᚦᚢᚱ᛬ᛋᛁᚾᛅ᛬ᛋᛅ " \
                    "ᚼᛅᚱᛅᛚᛏᚱ(᛬)ᛁᛅᛋ᛬ᛋᚭᛦ᛫ᚢᛅᚾ᛫ᛏᛅᚾᛘᛅᚢᚱᚴ\nᛅᛚᛅ᛫ᛅᚢᚴ᛫ᚾᚢᚱᚢᛁᚴ\n᛫ᛅᚢᚴ᛫ᛏ(ᛅ)ᚾᛁ(᛫ᚴᛅᚱᚦᛁ᛫)ᚴᚱᛁᛋᛏᚾᚭ"

ramsund_runestone = "ᛋᛁᚱᚦ᛬ᚴᛁᛅᚱᚦᛁ᛬ᛒᚢᚦ᛬ᚦᚭᛋᛁ᛬ᛘᚢᚦᛁᛦ᛬ᛅᛚᚱᛁᚴᛋ᛬ᛏᚢᛏᛁᛦ᛬ᚢᚱᛘᛋ᛬ᚠᚢᚱ᛬ᛋᛅᛚᚢ᛬ᚼᛅᛚᚢ᛬ᚼᚢᛚᛘᚴᛁᚱᛋ᛬ᚠᛅᚦᚢᚱ᛬ᛋᚢᚴᚱᚢᚦᛅᚱ᛬ᛒᚢᛅᛏᛅ᛬ᛋᛁᛋ"

# The Ed (Boulder) Inscription from Uppland, Sweden
# http://runes.verbix.com/vikingage/Uppland.html
ed_inscription = "ᚱᛅᚼᚾᚢᛅᛚᛏᚱ ᛫ ᛚᛁᛏ ᛫ ᚱᛁᛋᛏᛅ ᛫ ᚱᚢᚾᛅᚱ ᛫ ᚽᚡᛦ ᛫ ᚡᛅᛋᛏᚢᛁ ᛫ ᛘᚬᚦᚢᚱ ᛫ ᛋᛁᚾᛅ ᛫ ᚬᚾᚽᛘᛋ ᛫ ᛏᚬᛏᛦ ᛫ ᛏᚬ ᛁ ᛫ " \
                 "ᛅᛁᚦᛁ ᛫ ᚴᚢᚦ ᚼᛁᛅᛚᛒᛁ ᛫ ᛅᚾᛏ ᛫ ᚼᚽᚾᛅ ᛫ " \
                 "§B ᚱᚢᚾᛅ ᛫ ᚱᛁᛋᛏᛅ ᛫ ᛚᛁᛏ ᛫ ᚱᛅᚼᚾᚢᛅᛚᛏᚱ ᛫ ᚼᚢᛅᚱ ᛅ × ᚵᚱᛁᚴᛚᛅᚾᛏᛁ ᛫ ᚢᛅᛋ ᛫ ᛚᛁᛋ ᛫ ᚡᚬᚱᚢᚾᚴᛁ ᛫"

# https://en.wikipedia.org/wiki/Uppland_Runic_Inscription_448
u448 = "ᚴᚢᛚ᛫ᛅᚢᚴ᛫ᛒᛁᚢᚱᚾ᛫ᛚᛁᛏᚢ᛫ᚱᛅᛁᛋᛅ᛫ᛋᛏᛅᛁᚾ᛫ᛂᚠᛏᛁᛦ᛫ᚦᚢᚱᛋᛏᛅᛁᚾ᛫ᚠᛅᚦᚢᚱ"


# https://en.wikipedia.org/wiki/Uppland_Runic_Inscription_92
u92 = "ᚴᚾᚢᛏᚱ ' ᛁ ᚢᛁᚴ'ᚼᚢᛋᚢᛘ ' ᛚᛁᛏ ' ᛋᛏᛅᛁᚾ ' ᚱᛁᛏᛅ ' ᚢᚴ ' ᛒᚱᚬ ' ᚴᛁᚱᛅ ᛫ ᛁᚡᛏᛁᛦ ' ᚡᛅᚦᚢᚱ ᚢᚴ ᛫ ᛘᚬᚦᚬᚱ ᛫ ᚢᚴ ᛫" \
      " ᛒᚱᚤᚦᚱ ᛫ ᛋᛁᚾᛅ ᛫ ᚢᚴ ᛫ ᛋᚢᛋᛏᚢᚱ"


sweden_runic_inscription_filename = "sweden_runes.json"


def read_sweden_runes():
    with open(sweden_runic_inscription_filename, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    print(" ".join(Rune.display_runes(ELDER_FUTHARK)))
    print(" ".join(Rune.display_runes(YOUNGER_FUTHARK)))
    print(" ".join(Rune.display_runes(SHORT_TWIG_YOUNGER_FUTHARK)))

    # https://sv.wikipedia.org/wiki/Upplands_runinskrifter_937
    inscription = "ᚦᛁᛅᚴᚾ᛫ᛅᚢᚴ᛫ᚴᚢᚾᛅᚱ᛫ᚱᛅᛁᛋᛏᚢ᛫ᛋᛏᛅᛁᚾᛅ ᛅᚠᛏᛁᛦ᛫ᚢᛅᚱ᛫ᛒᚱᚢᚦᚢᚱ᛫ᛋᛁᚾ"
    print(inscription)
    print(Transcriber.transcribe(inscription, YOUNGER_FUTHARK))
    print(little_jelling_stone)
    print(Transcriber.transcribe(little_jelling_stone, YOUNGER_FUTHARK))
    print(big_jelling_stone)
    print(Transcriber.transcribe(big_jelling_stone, YOUNGER_FUTHARK))
    print(ramsund_runestone)
    print(Transcriber.transcribe(ramsund_runestone, YOUNGER_FUTHARK))
