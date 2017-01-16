
verbs = raw_input("enter verbs: ").split()

pronouns = 'ich du er/sie wir ihr sie/Sie'.split()

import random

cache = {}

while True:
    k = (random.choice(pronouns), random.choice(verbs))
    r = cache.get(k)
    if r == ():
        continue
    if r:
        answer = raw_input("%s %s: " % k)
        if answer == r:
            cache[k] = ()
        else:
            print "Wrong, its %s" % r
    else:
        answer = raw_input("%s %s (first): " % k)
        cache[k] = answer


