# -*- coding: UTF-8 -*-

from collections import defaultdict

class Markov(object):
    def __init__(self, prefix_size=1, data=None):
        self.prefix_size = prefix_size
        if data is not None:
            self.learn(data) 

    def learn(self, data):
        self.stats = defaultdict(lambda: defaultdict(int))
        for i, value in enumerate(data):
            for j in range(1, self.prefix_size + 1):
                prefix = tuple(data[max(0, i - j):i])
                self.stats[prefix][value] += 1

    def _next(self, prefix=()):
        return max(self.stats[prefix], key=lambda x: self.stats[prefix][x]) 

    def chain(self, length=1, prefix=[]):
        for i in range(length):
            prefix.append(self._next(tuple(prefix[-self.prefix_size:])))
        return prefix

def predict(previous, length=1, prefix_size=2):
    return Markov(prefix_size, previous).chain(length, previous)


text = open('memorias.txt').read()
m = Markov(2, text.split())
print ' '.join(m.chain(100, ['a']))
