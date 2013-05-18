# -*- coding: UTF-8 -*-

from collections import defaultdict
import random

#http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w > r:
         return c
      upto += w
   assert False, "Shouldn't get here"


class Markov(object):
    def __init__(self, prefix_size=1, data=None):
        self.prefix_size = prefix_size
        self.stats = defaultdict(lambda: defaultdict(int))
        if data:
            self.learn(data)

    def learn(self, data):
        for i, value in enumerate(data):
            for j in range(1, self.prefix_size + 1):
                prefix = tuple(data[max(0, i - j):i])
                self.stats[prefix][value] += 1

    def _next(self, prefix=()):
        return weighted_choice(self.stats[prefix].items())

    def chain(self, length=1, prefix=[]):
        for i in range(length):
            prefix.append(self._next(tuple(prefix[-self.prefix_size:])))
        return prefix

def predict(previous, length=1, prefix_size=2):
    return Markov(prefix_size, previous).chain(length, previous)


text = open('tcc.txt').read()
m = Markov(2, text.split())
print ' '.join(m.chain(1000, ['a']))
