



from phue import Bridge


import logging


b = Bridge('192.168.2.3')
b.connect()
b.get_api()

logging.basicConfig(
    filename='/Users/pips/PycharmProjects/phuelogging/twitter_effect.txt',
    level=logging.INFO,
)

# neem mijn lampen in een array
mijn_lampen = []             # word nog gevuld
alle_lampen = []             # word nog gevuld


# print namen van alle lampen
lights = b.lights
for l in lights:
    alle_lampen.append(l.name)
alle_lampen.sort()

for l in lights:
    if "Rob" not in l.name:
        continue
    else:
        mijn_lampen.append(l.name)
