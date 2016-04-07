from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        # self.redis = StrictRedis()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
	# connect to the database
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	conn.autocommit = True

        # Increment the local count
        self.counts[word] += 1
	#insert data into the database
	cur = conn.cursor()
	
	#check to see if word is in the table, if so execute an update
	cur.execute("SELECT word, count from tweetwordcount where word = %s", (word,))
	if cur.fetchone() is not None:
		#do an update
		cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
	else:
		#do an insert
		cur.execute("INSERT INTO Tweetwordcount (word,count)  VALUES (%s, 1)", (word,));
		print('need for indent block')


	#if the word is not in the database execute an insert

        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
