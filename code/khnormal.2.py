#!/usr/bin/python3
# Copyright (c) 2021, SIL International.
# Licensed under MIT license: https://opensource.org/licenses/MIT

# This file has been adopted for normalize sentences
# - character-cluster segmenter has been added based on the seg.py 
#   in https://lotus.kuee.kyoto-u.ac.jp/WAT/km-en-data/wat2020.km-en.zip
# - sentence_wapper() has been added.

import enum, re
from collections import Counter

class Cats(enum.Enum):
    Other = 0; Base = 1; Robat = 2; Coeng = 3; ZFCoeng = 4
    CoengB = 5; Shift = 6; Z = 7; VPre = 8; VB = 9; VA = 10
    VPost = 11; MS = 12; MF = 13

categories =  ([Cats.Base] * 35     # 1780-17A2
            + [Cats.Other] * 2      # 17A3-17A4
            + [Cats.Base] * 15      # 17A5-17B3
            + [Cats.Other] * 2      # 17B4-17B5
            + [Cats.VPost]          # 17B6
            + [Cats.VA] * 4         # 17B7-17BA
            + [Cats.VB] * 3         # 17BB-17BD
            + [Cats.VPre] * 8       # 17BE-17C5
            + [Cats.MS]             # 17C6
            + [Cats.MF] * 2         # 17C7-17C8
            + [Cats.Shift] * 2      # 17C9-17CA
            + [Cats.MS]             # 17CB
            + [Cats.Robat]          # 17CC
            + [Cats.MS] * 5         # 17CD-17D1
            + [Cats.Coeng]          # 17D2
            + [Cats.Other] * 10     # 17D3-17DC
            + [Cats.MS])            # 17DD

khres = {   # useful regular sub expressions used later
    "B":       "[\u1780-\u17A2\u17A5-\u17B3]",
    "NonRo":   "[\u1780-\u1799\u179B-\u17A2\u17A5-\u17B3]",
    "NonBA":   "[\u1780-\u1793\u1795-\u17A2\u17A5-\u17B3]",
    "S1":      "[\u1780-\u1783\u1785-\u1788\u178A-\u178D\u178F-\u1792"
               "\u1795-\u1797\u179E-\u17A0\u17A2]",
    "S2":      "[\u1784\u1780\u178E\u1793\u1794\u1798-\u179D\u17A1\u17A3-\u17B3]",
    "VAA":     "(?:[\u17B7-\u17BA\u17BE\u17BF\u17DD]|\u17B6\u17C6)",
    "VA":      "(?:[\u17C1-\u17C5]?{VAA})",
    "VAS":     "(?:{VA}|[\u17C1-\u17C3]?\u17D0)",
    "VB":      "(?:[\u17C1-\u17C3][\u17BB-\u17BD])",
    # contains series 1 and no BA
    "STRONG":  "{S1}\u17CC?(?:\u17D2{NonBA}(?:\u17D2{NonBA})?)?|"
               "{NonBA}\u17CC?(?:\u17D2{S1}(?:\u17D2{NonBA})?|\u17D2{NonBA}\u17D2{S1})",
    # contains BA or only series 2
    "NSTRONG": "(?:{S2}\u17CC?(?:\u17D2{S2}(?:\u17D2{S2})?)?|"
               "\u1794(?:\u17D2{B}(?:\u17D2{B})?)?"
               "\u17D2{B}\u17D2\u1794|\u17D2\u1794(?:\u17D2{B})?)",
    "COENG":   "(?:(?:\u17D2{NonRo})?\u17D2{B})",
    # final right spacing coeng
    "COENGR":  "(?:(?:[\u17C9\u17CA]\u200C?)?(?:{VB}?{VAS}|{VB}))",
    # final all coengs
    "COENGF":  "(?:(?:[\u17C9\u17CA]\u200C?)?[\u17C2-\u17C3]?{VB}?{VA}?"
               "[\u17B6\u17BF\u17C0\u17C4\u17C5])",
    "COENGS":  "(?:\u17C9\u200C?{VAS})",
    "FCOENG":  "(?:\u17D2\u200D{NonRo})",
    "SHIFT":   "(?:(?<={STRONG}{FCOENG}?)\u17CA\u200C(?={VA})|"
               "(?<={NSTRONG}{FCOENG}?)\u17C9\u200C(?={VAS})|[\u17C9\u17CA])",
    "V":       "(?:\u17C1[\u17BC\u17BD]?[\u17B7\u17B9\u17BA]?|"
               "[\u17C2\u17C3]?[\u17BC\u17BD]?[\u17B7-\u17BA]\u17B6|"
               "[\u17C2\u17C3]?[\u17BB-\u17BD]?\u17B6|\u17BE[\u17BC\u17BD]?\u17B6?|"
               "[\u17C1-\u17C5]?\u17BB(?![\u17D0\u17DD])|"
               "[\u17C2-\u17C5]?[\u17BC\u17BD]?[\u17B7-\u17BA]?|[\u17BF\u17C0])",
    "MS":      "(?:(?:[\u17C6\u17CB\u17CD-\u17CF\u17D1\u17D3]|"
               "(?<!\u17BB[\u17B6\u17C4\u17C5]?)[\u17D0\u17DD])"
               "[\u17C6\u17CB\u17CD-\u17D1\u17D3\u17DD]?)"
}

# expand 2 times: CEONGS -> VAS -> VA -> VAA
for i in range(3):
    khres = {k: v.format(**khres) for k, v in khres.items()}

def charcat(c):
    ''' Returns the Khmer character category for a single char string'''
    o = ord(c)
    if 0x1780 <= o <= 0x17DD:
        return categories[o-0x1780]
    elif o == 0x200C:
        return Cats.Z
    elif o == 0x200D:
        return Cats.ZFCoeng
    return Cats.Other

def khnormal(txt, lang="km"):
    ''' Returns khmer normalised string, without fixing or marking errors'''
    # Mark final coengs in Middle Khmer
    if lang == "xhm":
        txt = re.sub(r"([\u17B7-\u17C5]\u17D2)", "\\1\u200D", txt)
    # Categorise every character in the string
    charcats = [charcat(c) for c in txt]

    # Recategorise base -> coeng after coeng char
    for i in range(len(charcats)-1, 0, -1):
        if charcats[i-1] in (Cats.Coeng, Cats.ZFCoeng) and charcats[i] == Cats.Base:
            charcats[i] = Cats.CoengB

    # Find subranges of base+non other and sort components in the subrange
    i = 0
    res = []
    while i < len(charcats):
        c = charcats[i]
        if c != Cats.Base:
            res.append(txt[i])
            i += 1
            continue
        # Scan for end of syllable
        j = i + 1
        while j < len(charcats) and charcats[j].value > Cats.Base.value:
            j += 1
        # Sort syllable based on character categories
        # Sort the char indices by category then position in string
        newindices = sorted(range(i, j), key=lambda e:(charcats[e].value, e))
        replaces = "".join(txt[n] for n in newindices)

        replaces = re.sub("([\u200C\u200D]|\u17D2\u200D?)[\u17D2\u200C\u200D]+",
                          r"\1", replaces)      # remove multiple invisible chars
        # map compoound vowel sequences to compounds with -u before to be converted
        replaces = re.sub("\u17C1([\u17BB-\u17BD]?)\u17B8", "\u17BE\\1", replaces)
        replaces = re.sub("\u17C1([\u17BB-\u17BD]?)\u17B6", "\u17C4\\1", replaces)
        replaces = re.sub("(\u17BE)(\u17BB)", r"\2\1", replaces)
        # Replace -u + upper vowel with consonant shifter
        replaces = re.sub("({STRONG}{FCOENG}?[\u17C1-\u17C5]?)\u17BB"
                          "(?={VAA}|\u17D0)".format(**khres), "\\1\u17CA", replaces)
        replaces = re.sub("({NSTRONG}{FCOENG}?[\u17C1-\u17C5]?)\u17BB"
                          "(?={VAA}|\u17D0)".format(**khres), "\\1\u17C9", replaces)
        replaces = re.sub("(\u17D2\u179A)(\u17D2[\u1780-\u17B3])",
                          r"\2\1", replaces)    # coeng ro second
        replaces = re.sub("(\u17D2)\u178A", "\\1\u178F", replaces)  # coeng da->ta
        res.append(replaces)
        i = j
    return "".join(res)

def khtest(txt):
    ''' Tests normalized text for conformance to Khmer encoding structure '''
    import regex
    syl = ("{B}\u17CC?{COENG}?(?:\u17D2\u200D(?={COENGR})|{FCOENG}(?={COENGF})|"
           "(?<={NSTRONG})\u17D2\u200D{S1}(?={COENGS}))?{SHIFT}?{V}?{MS}?[\u17C7\u17C8]?|"
           "[\u17A3\u17A4\u17B4\u17B5\u17D3-\u17DC\u17E0-\u17F9]|"
           "[^\u1780-\u17F9]").format(**khres)
    res = regex.match(r"^({})+$".format(syl), txt)
    return res != None

################################### Adopted parts ##########################
################## seg() is copied from seg.py in https://lotus.kuee.kyoto-u.ac.jp/WAT/km-en-data/wat2020.km-en.zip
DEP = set ([chr (0x17b4+x) for x in range (28)] + [chr (0x17dd)])
STACK = chr (0x17d2)

def seg (k) :
    # k = list (''.join (k.lower ().strip ().split ()))
    k = list (''.join (k.strip ().split ()))
    ### generate basic units
    k.reverse ()
    for i in range (len (k)-1) : 
        if k [i][0] in DEP : k [i+1] += k [i]; k [i] = ''
    k.reverse ()
    ### glue stacked units
    k = ' '.join (k).split ()
    k = ' '.join (k).replace (' '+STACK+' ', STACK)
    return k

################### 
def sentence_wrapper(line):
    return ' '.join([
        ''.join([
            khnormal(cc) 
            for cc in seg(word).split(' ')
        ]) 
        for word in line.split(' ')
    ])
################################### End of Adopted parts ##########################

if __name__ == "__main__":
    import argparse, sys

    parser = argparse.ArgumentParser()
    parser.add_argument("infile",nargs="+",help="input file")
    # parser.add_argument("-o","--outfile", help="Output file")
    parser.add_argument("outfile")
    parser.add_argument("-u","--unicodes",action="store_true")
    # parser.add_argument("-f","--fail",action="store_true",
    #                     help="Only print lines that fail the regex after normalising")
    args = parser.parse_args()

    # fails = []

    if args.unicodes:
        instr = "".join(chr(int(x, 16)) for x in args.infile)
        res = sentence_wrapper(instr)
        print(res)
        # if not args.fail or not khtest(res):
        # 	print(" ".join("{:04X}".format(ord(x)) for x in res))
    else:
        infile = open(args.infile[0], encoding="utf-8")
        outfile = open(args.outfile, "w", encoding="utf-8") if args.outfile else sys.stdout
        for l in infile.readlines():
            res = sentence_wrapper(l)
            print(res, file=outfile)
            # if not args.fail or not khtest(res):
                #if l == res:
                #	continue
                #outfile.write('{}\t{}\n'.format(l.strip(), res.strip()))
