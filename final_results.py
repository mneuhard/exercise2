import psycopg2
import sys

word = ""
if len(sys.argv) > 1:
	word = sys.argv[1]

# Write codes to increment the word count in Postgres
# connect to the database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
conn.autocommit = True

#select data from  the database
cur = conn.cursor()
if word != "":
	cur.execute("SELECT word, count from tweetwordcount where word = %s", (word,))
else: 
        cur.execute("SELECT word, count from tweetwordcount")

for (word, count) in cur:
	print "Total number of occurences of %s: %s", (word, count)
