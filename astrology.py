import time
from datetime import datetime
import pytz
import ephem

symbols = {
    'planets':{
        'sun':'☉',
        'moon':'☽',
        'mercury':'☿',
        'venus':'♀',
        'earth':'🜨',
        'mars':'♂',
        'jupiter':'♃',
        'saturn':'♄',
        'uranus':'♅',
        'neptune':'♆',
        'pluto':'♇',
        'ceres':'⚳',
        'pallas':'⚴',
        'juno':'⚵',
        'vesta':'⚶',
        'hygiea':'⚕',
        'chiron':'⚷',
        'eris':'♁',
        'comet':'☄'
    },
    'constellations':{
        'aries':'♈',
        'taurus':'♉',
        'gemini':'♊',
        'cancer':'♋',
        'leo':'♌',
        'virgo':'♍',
        'libra':'♎',
        'scorpio':'♏',
        'scorpius':'♏',
        'ophiuchus':'⛎',
        'sagittarius':'♐',
        'capricorn':'♑',
        'aquarius':'♒',
        'pisces':'♓',
    },
    'aspects':{
        'conjunction':'☌',
        'semisextile':'⚺',
        'semi-square':'∠',
        'sextile':'⚹',
        'quintile':'Q',
        'square':'□',
        'trine':'△',
        'sesquiquadrate':'⚼',
        'biquintile':'bQ',
        'quincunx':'⚻',
        'opposition':'☍'
    },
    'lunar phases':{
        'new moon':'🌑',
        'crescent moon':'🌒',
        'first quarter moon':'🌓',
        'gibbous moon':'🌔',
        'full moon':'🌕',
        'disseminating moon':'🌖',
        'last quarter moon':'🌗',
        'balsamic moon':'🌘'
    },
    'angles':{
        'ascendant':'ASC',
        'midheaven':'MC',
        'ascending node':'☊',
        'descending node':'☋',
        'black moon lilith':'⚸',
        'retrograde motion':'℞',
        'lot of fortune':'⊗'
    }
}
white_on_black = True
if white_on_black:
    symbols['lunar phases'] = {
        'new moon':'🌕',
        'crescent moon':'🌖',
        'first quarter moon':'🌗',
        'gibbous moon':'🌘',
        'full moon':'🌑',
        'disseminating moon':'🌒',
        'last quarter moon':'🌓',
        'balsamic moon':'🌔'
    }

signs = {
        'aries':{'symbol':'♈', 'gloss':'The Ram', 'element':'fire', 'modality':'cardinal',
                'rules':'mars', 'rules_modern':'mars'},
        'taurus':{'symbol':'♉', 'gloss':'The Bull', 'element':'earth', 'modality':'fixed',
                'rules':'venus', 'rules_modern':'earth'},
        'gemini':{'symbol':'♊', 'gloss':'The Twins', 'element':'air', 'modality':'mutable',
                'rules':'mercury', 'rules_modern':'mercury'},
        'cancer':{'symbol':'♋', 'gloss':'The Crab', 'element':'water', 'modality':'cardinal',
                'rules':'moon', 'rules_modern':'moon'},
        'leo':{'symbol':'♌', 'gloss':'The Lion', 'element':'fire', 'modality':'fixed',
                'rules':'sun', 'rules_modern':'sun'},
        'virgo':{'symbol':'♍', 'gloss':'The Maiden', 'element':'earth', 'modality':'mutable',
                'rules':'mercury', 'rules_modern':'ceres'},
        'libra':{'symbol':'♎', 'gloss':'The Scales', 'element':'air', 'modality':'cardinal',
                'rules':'venus', 'rules_modern':'venus'},
        'scorpio':{'symbol':'♏', 'gloss':'The Scorpion', 'element':'water', 'modality':'fixed',
                'rules':'mars', 'rules_modern':'pluto'},
        'ophiuchus':{'symbol':'⛎', 'gloss':'Serpent-bearer', 'element':'???', 'modality':'???',
                'rules':'???', 'rules_modern':'???'},
        'sagittarius':{'symbol':'♐', 'gloss':'The Archer', 'element':'fire', 'modality':'mutable',
                'rules':'jupiter', 'rules_modern':'jupiter'},
        'capricorn':{'symbol':'♑', 'gloss':'The Mountain Sea-goat', 'element':'earth', 'modality':'cardinal',
                'rules':'saturn', 'rules_modern':'saturn'},
        'aquarius':{'symbol':'♒', 'gloss':'The Water-bearer', 'element':'air', 'modality':'fixed',
                'rules':'saturn', 'rules_modern':'uranus'},
        'pisces':{'symbol':'♓', 'gloss':'The Fish', 'element':'water', 'modality':'mutable',
                'rules':'jupiter', 'rules_modern':'neptune'}
}

planets_classical = {
        'sun':{'symbol':'☉',        'dignity':'♌',  'detriment':'♒',  'exaltation':'♈', 'fall':'♎'},
        'moon':{'symbol':'☽',       'dignity':'♋',  'detriment':'♑',  'exaltation':'♉', 'fall':'♏'},
        'mercury':{'symbol':'☿',    'dignity':'♍♊', 'detriment':'♓♐', 'exaltation':'♒', 'fall':'♌'},
        'venus':{'symbol':'♀',      'dignity':'♎♉', 'detriment':'♏♈', 'exaltation':'♓', 'fall':'♍'},
        'mars':{'symbol':'♂',       'dignity':'♏♈', 'detriment':'♎♉', 'exaltation':'♑', 'fall':'♋'},
        'jupiter':{'symbol':'♃',    'dignity':'♓♐', 'detriment':'♍♊', 'exaltation':'♋', 'fall':'♑'},
        'saturn':{'symbol':'♄',     'dignity':'♒♑', 'detriment':'♌♋', 'exaltation':'♎', 'fall':'♈'}
}

class colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[2m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'

def Ceres():
    readable = 'Ceres, e, 10.607, 80.702, 71.274, 2.7685, 0.21396, 0.0780, 287.265, 10/1/1989, 2000.0, 3.32, 0.11'
    return ephem.readdb(readable.replace(' ',''))
def Pallas():
    return ephem.readdb('Pallas,e,34.804,173.323,309.796,2.7703,0.21375,0.2347,273.779,10/1/1989,2000.0,4.13,0.15')
def Juno():
    return ephem.readdb('Juno,e,12.991,170.542,246.787,2.6692,0.22601,0.2575,205.808,11/5/1990,2000.0,5.31,0.30')
def Vesta():
    return ephem.readdb('Vesta,e,7.139,104.015,149.986,2.3607,0.27174,0.0906,152.190,11/5/1990,2000.0,3.16,0.34')
def Hygiea():
    return ephem.readdb('Hygiea,e,3.840,283.833,315.832,3.1365,0.17743,0.1202,104.089,11/5/1990,2000.0,5.37,0.15')
def Eris():
    #warning: hand-compiled
    readable = 'Eris, e, 44.176, 35.890, 151.315, 67.662, 0.00177, 0.442, 204.63, 6/31/2016, 2007.0, -1.2, 0.6'
    return ephem.readdb(readable.replace(' ',''))

def Chiron():
    #warning: hand-compiled
    readable = 'Chiron, e, 6.932, 208.65, 339.58, 13.7, 0.2, 0.3832, 359.5, 17/31/1996, 2000.0, 3.32, 0.11'
    return ephem.readdb(readable.replace(' ',''))

ecliptic_traditional = ('aries','taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces')

ecliptic_modern = ('aries','taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpius', 'ophiuchus', 'sagittarius', 'capricornus', 'aquarius', 'pisces')

def get_sign(degrees, modern=False):
    if modern:
        print('Hah! There is only one TRUE astrology! May Sagittarius strike you down with his bow!')
    idx = int(degrees/30)
    return ecliptic_traditional[idx]

moon_sequence = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘']

symbol_lookup = {}
for section in symbols.values():
    for name,symbol in section.items():
        symbol_lookup[symbol] = name

print('planets:       ', ' '.join(symbols['planets'].values()))
print('constellations:', ' '.join(symbols['constellations'].values()))
print('aspects:       ', ' '.join(symbols['aspects'].values()))
print('lunar phases:  ', ' '.join(symbols['lunar phases'].values()))
print('angles:        ', ' '.join(symbols['angles'].values()))

def animate_moon():
    print('\n')
    idx = 0
    for i in range(0,15):
        print('\t\t\t\t\t' + moon_sequence[idx], end='\r')
        idx = (idx + 1) % len(moon_sequence)
        time.sleep(0.15)

def major_planetary_signs(birth):
    bodies = (
        ('sun',ephem.Sun()),
        ('moon',ephem.Moon()),
        ('mercury',ephem.Mercury()),
        ('venus',ephem.Venus()),
        ('mars',ephem.Mars()),
        ('jupiter',ephem.Jupiter()),
        ('saturn',ephem.Saturn()),
        ('uranus',ephem.Uranus()),
        ('neptune',ephem.Neptune()),
        ('pluto',ephem.Pluto())
    )
    return planetary_signs(birth, bodies)

def minor_planetary_signs(birth):
    bodies = (
        ('ceres',Ceres()),
        ('pallas',Pallas()),
        ('vesta',Vesta()),
        ('juno',Juno()),
        ('hygiea',Hygiea()),
        ('eris',Eris()),
        ('chiron',Chiron())
    )
    return planetary_signs(birth, bodies)

def planetary_signs(birth, bodies):
    signs = []
    for name,body in bodies:
        body.compute(birth)
        degrees,minutes,seconds = str(ephem.Ecliptic(body).lon).split(':')
        degrees = int(degrees) + int(minutes)/60 + float(seconds)/(60*60)
        #print(name, Ecliptic(body).lon, degrees)
        signs.append((name,get_sign(degrees),(degrees)))
    return signs

def planetary_constellations(birth):
    bodies = (
        ('sun',ephem.Sun()),
        ('moon',ephem.Moon()),
        ('mercury',ephem.Mercury()),
        ('venus',ephem.Venus()),
        ('mars',ephem.Mars()),
        ('jupiter',ephem.Jupiter()),
        ('saturn',ephem.Saturn()),
        ('uranus',ephem.Uranus()),
        ('neptune',ephem.Neptune()),
        ('pluto',ephem.Pluto()),
        ('ceres',Ceres()),
        ('pallas',Pallas()),
        ('vesta',Vesta()),
        ('juno',Juno()),
        ('hygiea',Hygiea()),
        ('eris',Eris()),
        ('chiron',Chiron())
    )
    constellations = {}
    for name,body in bodies:
        body.compute(birth)
        #print(name.capitalize() + symbols['planets'][name] + ' :', constellation(body)[1])
        constellations[name] = ephem.constellation(body)[1].lower()
    return constellations

def abs_diff(a, b):
    result = abs(float(a)-float(b))
    if result > 180:
        return result-180
    return result

def power_relationships(planets):
    results = {'dignity':[], 'detriment':[], 'exaltation':[], 'fall':[]}
    for planet,sign,deg in planets:
        if planet in planets_classical:
            symbol = symbols['constellations'][sign]
            for power in results.keys():
                if symbol in planets_classical[planet][power]:
                    results[power].append((planet,sign,deg))
    return results

def aspect_relationships(planets, diff=10):
    results = {'conjunction':[], 'opposition':[]}
    for i in range(len(planets)):
        planet,sign,deg = planets[i]
        for j in range(i+1,len(planets)):
            p,s,d = planets[j]
            if abs_diff(deg, d) < diff:
                results['conjunction'].append((planet, p, abs_diff(deg,d)))
            elif abs_diff(deg, d) > (180 - diff/2):
                results['opposition'].append((planet, p, abs_diff(deg,d)))
    return results

def ascendent(birth, tz):
    fixed = (
        ('aries', ephem.FixedBody()),
        ('taurus', ephem.FixedBody()),
        ('gemini', ephem.FixedBody()),
        ('cancer', ephem.FixedBody()),
        ('leo', ephem.FixedBody()),
        ('virgo', ephem.FixedBody()),
        ('libra', ephem.FixedBody()),
        ('scorpio', ephem.FixedBody()),
        ('sagittarius', ephem.FixedBody()),
        ('capricorn', ephem.FixedBody()),
        ('aquarius', ephem.FixedBody()),
        ('pisces', ephem.FixedBody())
    )
    #create markers for the constellations at equally spaced ecliptic longitude
    for i in range(len(fixed)):
        sign = fixed[i][1]
        ec = ephem.Ecliptic(ephem.degrees(str(i*30)), ephem.degrees('0'))
        eq = ephem.Equatorial(ec)
        sign._ra, sign._dec = eq.ra, eq.dec
        sign.compute(birth)
    #find the most recently risen sign
    last_sign = None
    closest_sign_name = ''
    closest_sign = None
    closest_dist = 100
    closest_sign_idx = -1
    for i in range(len(fixed)):
        name,sign = fixed[i]
        if birth.date - birth.previous_rising(sign) < closest_dist:
            closest_dist = birth.date - birth.previous_rising(sign)
            closest_sign_name = name
            closest_sign = sign
            closest_sign_idx = i
        if not last_sign:
            last_sign = sign
        #print(name, birth.previous_rising(sign), birth.previous_rising(sign) - birth.previous_rising(last_sign))
        last_sign = sign
    #compute the fraction the sign has risen
    next_sign_name,next_sign = fixed[(closest_sign_idx+1)%12]
    time_up = birth.date - birth.previous_rising(closest_sign)
    until_next = birth.next_rising(next_sign) - birth.previous_rising(closest_sign)
    #print(closest_sign_name, next_sign_name, until_next, time_up, 30*time_up/until_next)
    return closest_sign_name,str(int(30*time_up/until_next))

def signedPlanet(planet, sign):
    color = colors.NORMAL
    if signs[sign]['element'] == 'earth':
        color = colors.GREEN
    if signs[sign]['element'] == 'air':
        color = colors.YELLOW
    if signs[sign]['element'] == 'fire':
        color = colors.RED
    if signs[sign]['element'] == 'water':
        color = colors.BLUE
    return color + planet.capitalize() + ' ' + colors.BOLD + symbols['constellations'][sign] + colors.NORMAL

def lunarPhase(birth):
    '''
    'new moon':'🌑',
    'crescent moon':'🌒',
    'first quarter moon':'🌓',
    'gibbous moon':'🌔',
    'full moon':'🌕',
    'disseminating moon':'🌖',
    'last quarter moon':'🌗',
    'balsamic moon':'🌘'
    '''
    moon = ephem.Moon()
    moon.compute(birth)
    if moon.phase < 0.2:
        symbol = symbols['lunar phases']['new moon']
    elif moon.phase > 99.8:
        symbol = symbols['lunar phases']['full moon']
    else:
        if ephem.next_full_moon(birth.date) > ephem.next_new_moon(birth.date):
            #moon is waning
            if moon.phase < 33:
                symbol = symbols['lunar phases']['balsamic moon']
            elif moon.phase < 66:
                symbol = symbols['lunar phases']['last quarter moon']
            else:
                symbol = symbols['lunar phases']['disseminating moon']
        else:
            #moon is waxing
            if moon.phase < 33:
                symbol = symbols['lunar phases']['crescent moon']
            elif moon.phase < 66:
                symbol = symbols['lunar phases']['first quarter moon']
            else:
                symbol = symbols['lunar phases']['gibbous moon']
    return symbol

def symbolfy(name):
    if name in symbols['planets']:
        return name.capitalize() + ' ' + symbols['planets'][name]
    if name in symbols['constellations']:
        return name.capitalize() + ' ' + symbols['constellations'][name]
    if name in symbols['aspects']:
        return name.capitalize() + ' ' + symbols['aspects'][name]
    if name in symbols['angles']:
        return name.capitalize() + ' ' + symbols['angles'][name]
    return name.capitalize()

def now_cast(city_name=None, cast_time=None, timezone=None, to_console=True, diff=1):
    if not cast_time:
        cast_time = datetime.now()
    if not timezone:
        if to_console:
            animate_moon()
            print('Global horoscope for {}\n'.format(cast_time))
        birth = ephem.Observer()
        birth.date = ephem.Date(cast_time)

        planets = major_planetary_signs(birth)
        planets.extend(minor_planetary_signs(birth))
        constellations = planetary_constellations(birth)

        sun_sign = planets[0][1]

        if to_console:
            print('{}\n{} ({}, {})\n'.format(sun_sign.upper(), signs[sun_sign]['gloss'], signs[sun_sign]['element'], signs[sun_sign]['modality']))


        #print out formatted string for each planet with sign and degrees
            template = '{0:10}:  {1:14} {2:5}° ({3:3}°)  {4:14}'
            print('{0:15}   {1:14} {2:5}°  {3:3}°   {4:14} '.format('Planet','Sign','Rel.','Ab.', 'Constellation'))
            print('\n'.join([template.format(symbolfy(planet), symbolfy(sign), int(deg)%30, int(deg), symbolfy(constellations[planet])) for planet,sign,deg in planets]))

            print('')
        aspects = aspect_relationships(planets, diff=diff)
        if to_console:
            for aspect in ['conjunction','opposition']:
                if len(aspects[aspect]) > 0:
                    print(aspect.capitalize() + ': ', ', '.join(['{0} {1} {2} ({3:.2f}°)'.format(p1.capitalize(), symbols['aspects'][aspect], p2.capitalize(), (diff)) for p1,p2,diff in aspects[aspect]]))
            print('')
            print('Lunar phase: {} ({})'.format(lunarPhase(birth), symbol_lookup[lunarPhase(birth)]))


            print('')
            print('_' * 50 + '\n')
    else:
        place = city(city_name)

        horoscope(city_name, place, cast_time, timezone)
    if not to_console:
        return {'planets':planets, 'constellations': constellations, 'aspects': aspects, 'phase': lunarPhase(birth), 'powers':power_relationships(planets)}

def horoscope(name, birth, date, timezone):
    animate_moon()

    tz = pytz.timezone(timezone)
    birth_utc = tz.localize(date).astimezone(pytz.utc)
    birth.date = ephem.Date(birth_utc)

    print('_' * 50 + '\n')
    print(f'horoscope for {name}:\nlat,lon: {birth.lat}, {birth.lon}\ndate and time (24hr): {tz.localize(birth.date.datetime()  )}\n')

    planets = major_planetary_signs(birth)
    planets.extend(minor_planetary_signs(birth))
    constellations = planetary_constellations(birth)

    sun_sign = planets[0][1]
    print('{}\n{} ({}, {})\n'.format(sun_sign.upper(), signs[sun_sign]['gloss'], signs[sun_sign]['element'], signs[sun_sign]['modality']))

    #print out formatted string for each planet with sign and degrees
    template = '{0:10}:  {1:14} {2:5}° ({3:3}°)  {4:14}'
    print('{0:10}   {1:14} {2:5}°  {3:3}°   {4:14} '.format('Planet','Sign','Rel.','Ab.', 'Constellation'))
    print('\n'.join([template.format(symbolfy(planet), symbolfy(sign), int(deg)%30, int(deg), symbolfy(constellations[planet])) for planet,sign,deg in planets]))

    asc = ascendent(birth, tz)
    #print(asc)

    print('\nWARNING: ascendent computations could be off by as much as 3°\nASC:', asc[0].capitalize() + ' ' + symbols['constellations'][asc[0]] + ' ' + str(int(asc[1])%30) + '°' + ' (' + asc[1] + '°)')

    #divvy up houses
    house_start = int(asc[1])
    for i in range(1,13):
        house = []
        house_end = (house_start + 30) % 360
        for planet,sign,deg in planets:
            if house_start < house_end:
                if house_start <= int(deg) and int(deg) < house_end:
                    house.append((planet,sign,int(deg)))
            elif house_start <= int(deg) or int(deg) < house_end:
                house.append((planet,sign,int(deg)))
        house.sort(key=lambda x: x[2])
        print('House #{}: ({}) {}'.format(i, house_start, ' '.join(['{} {}°'.format(signedPlanet(planet, sign), (deg%30)) for planet,sign,deg in house])))
        house_start = house_end

    print('')
    powers = power_relationships(planets)
    for power in ['dignity', 'detriment', 'exaltation', 'fall']:
        if len(powers[power]) > 0:
            print(power.capitalize() + ': ', ', '.join([signedPlanet(p,s) for p,s,d in powers[power]]))
    print('')
    aspects = aspect_relationships(planets)
    for aspect in ['conjunction','opposition']:
        if len(aspects[aspect]) > 0:
            print(aspect.capitalize() + ': ', ', '.join([p1.capitalize() + ' ' + symbols['aspects'][aspect] + ' ' + p2.capitalize() for p1,p2,_ in aspects[aspect]]))
    print('')
    print('Lunar phase: {} ({})'.format(lunarPhase(birth), symbol_lookup[lunarPhase(birth)]))


    print('')
    print('_' * 50 + '\n')

if __name__ == "__main__":
    # now_cast()
    selection = input('''
Select an option:
1: Horoscope
2: Nowcast
''')
    if selection == '2':
        now_cast()
    if selection == '1':
        name = input("What is this person's name? ")
        datestring = input('''What day was this person born? (Please use the format YYYY-MM-DD) ''')
        timestring = input('''What time? (Please use the format 24HH:MM) ''')
        try:
            dt = datetime(*[int(el) for el in datestring.split('-')], *[int(el) for el in timestring.split(':')])
        except Exception as e:
            print("Flagrant error :(", str(e))
        city = input("What city were they born at or near? (If no city, just hit enter) ")
        try:
            birth_city = ephem.city(city)
        except Exception as e:
            if len(city) > 1:
                print("Couldn't find city", city)
            print("You'll have to enter latitude and longitude")
            lat = input("Enter latitude: ")
            lon = input("Enter longitude: ")
            birth_city = ephem.Observer()
            birth_city.lon = lon
            birth_city.lat = lat
        common_tzs = {
            1: 'US/Eastern',
            2: 'US/Pacific',
            3: 'Europe/Berlin',
            4: 'Europe/London',
            5: 'US/Mountain',
            6: 'US/Central'
        }
        common_tzs_stringified = "\n".join([f'{key}: {val}' for key,val in common_tzs.items()])
        tz = input(f'''Were they born in one of these timezones? Type a number, or enter the correct timezone
{common_tzs_stringified}
''')
        if tz not in pytz.all_timezones:
            try:
                tz = common_tzs[int(tz)]
            except Exception as e:
                print("You sure this timezone exists?", tz)
        horoscope(name, birth_city, dt, tz)
