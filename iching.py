'''
sources:
https://aleadeum.com/2013/07/12/the-i-ching-random-numbers-and-why-you-are-doing-it-wrong/
http://www.homebrew.net/ching/

For the coin version we toss three coins six times and we build an hexagram from bottom up with the following correspondence and probabilities:

Three heads:  Old Yang       (9)    (Pr = 2/16)
Two head:       Young Yang  (8)    (Pr = 6/16)
Two tails:        Young Yin      (7)    (Pr = 6/16)
Three tails:     Old Yin           (6)    (Pr = 2/16)

But the probabilities are different than the Yarrow method! (according to aleadeum.com)

Recommended alternatives:
One coin for yin/yang
One d8 for young/old: [1] --> old yin
                      [6,7,8] --> old yang

'''

import random
import pandas
from pandas import DataFrame
import os

fuHsiOrdering = ['111111',
 '000000',
 '010001',
 '100010',
 '010111',
 '111010',
 '000010',
 '010000',
 '110111',
 '111011',
 '000111',
 '111000',
 '111101',
 '101111',
 '000100',
 '001000',
 '011001',
 '100110',
 '000011',
 '110000',
 '101001',
 '100101',
 '100000',
 '000001',
 '111001',
 '100111',
 '100001',
 '011110',
 '010010',
 '101101',
 '011100',
 '001110',
 '111100',
 '001111',
 '101000',
 '000101',
 '110101',
 '101011',
 '010100',
 '001010',
 '100011',
 '110001',
 '011111',
 '111110',
 '011000',
 '000110',
 '011010',
 '010110',
 '011101',
 '101110',
 '001001',
 '100100',
 '110100',
 '001011',
 '001101',
 '101100',
 '110110',
 '011011',
 '110010',
 '010011',
 '110011',
 '001100',
 '010101',
 '101010']


def getLine():
    sign = ['yin','yang'][random.randint(0,1)]
    if sign=='yin':
        dist = ['old'] + ['young'] * 7
    else:
        dist = ['young'] * 5 + ['old'] * 3
    age = dist[random.randint(0,7)]

    return age + ' ' + sign

def getLines():
    '''
    Get a hexagram with a traditional yarrow-like probability
     distribution, returned as a sign and series of 6 numbers.
    '''
    hexagram = []
    for i in range(6):
        hexagram.insert(0, getLine())
    return hexagram

def lookUpHexagram(lines):
    '''
    Translate the hexagram into a reading, one of the 64
    '''
    binString = ''
    for line in lines:
        if 'yin' in line:
            binString += '0'
        else:
            binString += '1'

    abspath = os.path.abspath(os.path.dirname(__file__))
    df = pandas.read_csv(abspath+'/iching_lookup.tsv', sep='\t', header=0, dtype={'binary':object})
    hexagram = df[df['binary']==binString]
    if len(hexagram) != 1:
        raise Exception('Wrong number of hexagrams for {}\nDataframe:\n{}'.format(binString, hexagram))
    return hexagram.iloc[0]

def getHexagram(printIt=False):
    lines = getLines()
    hexagram = lookUpHexagram(lines)
    if printIt:
        print('{} No. {}: {}'.format(hexagram.gua, hexagram.no, hexagram.english))
        return
    return hexagram
