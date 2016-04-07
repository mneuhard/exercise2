

import psycopg2
import sys

word = ""
if len(sys.argv) > 1:
        number_1 = sys.argv[1]
	number_2 = sys.argv[2]

# connect to the database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#select data from  the database
cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount where count between  %s and  %s order by count desc", (number_1,number_2))


for (word, count) in cur:
        print "Total number of occurences of %s: %s", (word, count)
