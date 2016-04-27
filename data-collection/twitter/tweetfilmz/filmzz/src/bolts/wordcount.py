from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        id = tup.values[0]
        title = tup.values[1]
        tweet = tup.values[2]
        # Increment the local count
        self.counts[title] += 1
        self.emit([title, self.counts[title]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (title, self.counts[title]))
