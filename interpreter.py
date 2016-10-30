import math
import random
from datetime import datetime

def score_elements(planet1, planet2):
    el1 = el2 = ''
    if 'element' in planet1:
        el1 = planet1['element']
    if 'element' in planet2:
        el2 = planet2['element']

    if el1 == el2 and el1 != '':
        return 2
    else:
        if el1 in ['fire','water'] and el2 in ['fire','water']:
            return -1
        if el1 in ['earth','air'] and el2 in ['earth','air']:
            return -1
    return 0

def score_modalities(planet1, planet2):
    mod1 = mod2 = ''
    if 'modality' in planet1:
        mod1 = planet1['modality']
    if 'modality' in planet2:
        mod2 = planet2['modality']

    if mod1 == mod2 and mod1 != '':
        return 0.25
    if mod1 in ['mutable', 'fixed'] and mod2 in ['mutable', 'fixed']:
        return -0.25
    return 0

def score_traits(planet1, planet2):
    t1 = t2 = l1 = l2 = ''
    if 'trait' in planet1:
        t1 = planet1['trait']
    if 'trait' in planet2:
        t2 = planet2['trait']
    if 'lacks' in planet1:
        l1 = planet1['lacks']
    if 'lacks' in planet2:
        l2 = planet2['lacks']

    if l1 == t2 or l2 == t1:
        # opposites
        return -1
    if t1 == t2 and l1 == l2:
        # twinsies
        return 2
    if t1 == t2:
        return 1
    if l1 == l2:
        return 0.5
    return 0

def score_quickness(planet1, planet2):
    q1 = q2 = 0
    if 'quickness' in planet1:
        q1 = planet1['quickness']
    if 'quickness' in planet2:
        q2 = planet2['quickness']
    return abs(q1 - q2)

def why_score(planetName1, planetName2):
    planet1 = planets[planetName1.lower()]
    planet2 = planets[planetName2.lower()]
    print(planetName1.capitalize())
    for key in planet1.keys():
        print('\t',key+':', planet1[key])
    print(planetName2.capitalize())
    for key in planet2.keys():
        print('\t',key+':', planet2[key])
    print('final score:', score_planets(planet1,planet2,verbose=True))

def score_planets(planet1, planet2, verbose=False):
    '''Return a score which indicated the difference or similarity between planets, where larger means more similar'''
    elements = score_elements(planet1, planet2)
    modalities = score_modalities(planet1, planet2)
    traits = score_traits(planet1, planet2)
    quickness = score_quickness(planet1, planet2)
    if verbose:
        print('elements: {} modalities: {} traits: {} quickness difference: {}'.format(elements, modalities, traits, quickness))
    result = elements + modalities + traits - quickness
    if verbose:
        print('raw score:', result)
    return (result**3)/10

def score_opposition(planet1, planet2, offset):
    score = score_planets(planet1, planet2) - 2
    return score * (2/math.exp(offset))

def score_conjunction(planet1, planet2, offset):
    score = score_planets(planet1, planet2) + 2
    return score * (1/math.exp(offset))

planets = {
    'ceres': {'element': 'earth', 'modality': 'mutable', 'trait':'physical', 'lacks':'mental', 'quickness': 0},
    #'chiron': {},
    #'comet': {'trait':'spiritual', 'lacks':'mental', 'quickness':1},
    'earth': {'element': 'earth', 'modality': 'fixed', 'trait':'physical', 'lacks':'spiritual', 'quickness': 0},
    #'eris': {'trait':'mental', 'lacks':'physical', 'quickness':0},
    #'hygiea': {},
    #'juno': {},
    'jupiter': {'element': 'fire', 'modality': 'mutable', 'trait':'mental', 'lacks':'spiritual', 'quickness': -1},
    'mars': {'element': 'fire', 'modality': 'cardinal', 'trait':'physical', 'lacks':'spiritual', 'quickness': 0.25},
    'mercury': {'element': 'air', 'modality': 'mutable', 'trait':'mental', 'lacks':'spiritual', 'quickness': 1},
    'moon': {'element': 'water', 'modality': 'cardinal', 'trait':'spiritual', 'lacks':'physical', 'quickness': 0.5},
    'neptune': {'element': 'water', 'modality': 'mutable', 'trait':'spiritual', 'lacks':'physical', 'quickness': -0.5},
    #'pallas': {},
    'pluto': {'element': 'water', 'modality': 'fixed', 'trait':'spiritual', 'lacks':'mental', 'quickness': -0.25},
    'saturn': {'element': 'earth', 'modality': 'cardinal', 'trait':'mental', 'lacks':'physical', 'quickness': -0.8},
    'sun': {'element': 'fire', 'modality': 'fixed', 'trait':'', 'lacks':'', 'quickness':0.5},
    'uranus': {'element': 'air', 'modality': 'fixed', 'trait':'mental', 'lacks':'spiritual', 'quickness':-0.5},
    'venus': {'element': 'air', 'modality': 'cardinal', 'trait':'physical', 'lacks':'mental', 'quickness':0.5},
    #'vesta': {}
}

'''
I need to define a couple things. First, I need the output axes that I'm quantifying.
Obviously I'm quantifying doom. What's the opposite of doom? Relief? Safety? Mercy?
I like mercy the best so far. Let me try to do an opposites sheet (this is all just
inspiration and not valid logic):
original P->Q (Doom),
negation not(P->Q) (Mercy),
converse Q->P (Exaltation),
contrapositive not Q->not P (Destruction).


        Doom axis -->

Mercy >>>>>>>>>>>>>>>>>>> Doom      Intensity
v  1                     2  v       axis
v                           v       |
v                           v       |
v             5             v       V
v                           v
v                           v
v  4                     3  v
Euphoria >>>>>>>> Destruction

1: The world will turn on its axis another day, life goes on
2: Today is not your day, best to stay inside.
3: Calamity and chaos. Board up your windows and call your loved ones, possibly for the last time.
4: The sunlights bursts forth from the clouds and shines down upon you.
5: Not great

possible third dimensions: beware, sorrow

'''
def print_diff_scores():
    combos = []
    planet_names = sorted(list(planets.keys()))
    while planet_names:
        planet1 = planet_names.pop(0)
        for planet2 in planet_names:
            if planet1 != planet2:
                final = score_planets(planets[planet1], planets[planet2])
                combos.append([planet1.capitalize() + ', ' + planet2.capitalize(), final])

    combos.sort(key=lambda x: x[1])
    for name,score in combos:
        print(name.ljust(20), round(score,2))

def print_opposition_scores(offset=0):
    combos = []
    planet_names = sorted(list(planets.keys()))
    while planet_names:
        planet1 = planet_names.pop(0)
        for planet2 in planet_names:
            if planet1 != planet2:
                final = score_opposition(planets[planet1], planets[planet2],0)
                combos.append([planet1.capitalize() + ', ' + planet2.capitalize(), final])

    combos.sort(key=lambda x: x[1])
    for name,score in combos:
        print(name.ljust(20), score)

def print_conjunction_scores(offset=0):
    combos = []
    planet_names = sorted(list(planets.keys()))
    while planet_names:
        planet1 = planet_names.pop(0)
        for planet2 in planet_names:
            if planet1 != planet2:
                final = score_conjunction(planets[planet1], planets[planet2],0)
                combos.append([planet1.capitalize() + ', ' + planet2.capitalize(), final])

    combos.sort(key=lambda x: x[1])
    for name,score in combos:
        print(name.ljust(20), score)

def make_printable(planet):
    if planet in ['sun','moon']:
        planet = 'the ' + planet
    else:
        planet = planet.capitalize()
    return planet

def get_astrology_score(cast_time=None):
    '''Get a score for the given time, with all contributing factors (conjunctions & oppotisions) involved. Negative scores are bad.'''
    from astrologic import now_cast, signs, symbols
    cast = now_cast(cast_time=cast_time, to_console=False, diff=5)
    result = []
    for planet1,planet2,offset in cast['aspects']['conjunction']:
        score = score_conjunction(planet1,planet2,offset)

        #print('{}, {}: {}'.format(planet1,planet2,score))
        planet1 = make_printable(planet1).capitalize()
        planet2 = make_printable(planet2)
        result.append(('{} and {} are in conjunction.'.format(planet1, planet2), score))
    for planet1,planet2,offset in cast['aspects']['opposition']:
        offset = 180-offset
        score = score_opposition(planet1,planet2,offset)
        planet1 = make_printable(planet1).capitalize()
        planet2 = make_printable(planet2)
        result.append(('{} and {} are in opposition.'.format(planet1, planet2), score))
    return result

def plot_score():
    import matplotlib.pyplot as plt
    from pandas import Series
    ts = {}

    for day in range(1, 30):
        for hour in range(0, 24, 1):
#        for minute in range(0, 60):
            cast_time = datetime(2016, 11, day, hour)
            scores = get_astrology_score(cast_time)
            total = 0
            for reason,score in scores:
                total += score
            scores = sorted(scores, key=lambda x: x[1])
            if len(scores) > 1:
                print(str(cast_time).ljust(20), str(round(total,3)).ljust(10), scores[0], scores[1])
            elif scores:
                print(str(cast_time).ljust(20), str(round(total,3)).ljust(10), scores[0])
            ts[cast_time] = total
    ts = Series(ts)
    ts.plot()
    plt.show()
