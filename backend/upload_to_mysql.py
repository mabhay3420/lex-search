import json

# import mysql.connector
from creds import MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE
import MySQLdb
from tqdm import tqdm

print(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE)
# Replace the connection details with your own MySQL credentials
conn = MySQLdb.connect(
    user=MYSQL_USERNAME,
    passwd=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    db=MYSQL_DATABASE,
    ssl_mode="VERIFY_IDENTITY",
    ssl={"ca": "/etc/ssl/cert.pem"},
)

# delte LEX_TRANSCRIPTS table
with conn.cursor() as cur:
    cur.execute("DROP TABLE LEX_TRANSCRIPTS")
    conn.commit()

# Create the table in the database if it doesn't exist
with conn.cursor() as cur:
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS LEX_TRANSCRIPTS(
        id INT AUTO_INCREMENT PRIMARY KEY,
        episode INT,
        chunk INT,
        start_time VARCHAR(32),
        end_time VARCHAR(32),
        content TEXT
    )
    """
    )
    conn.commit()

# Read the JSON data
with open("data/merged_transcripts.json", "r") as f:
    json_data = json.load(f)

# print(len(json_data))
# print(json_data[:2])
# Iterate through the JSON data and insert it into the database
# use a fancy tqdm progress bar

transcript_list = []
for chunks in tqdm(json_data):
    episode = chunks.get("episodeNumber", None)
    chunk = chunks.get("chunk", None)

    # now we have a transcript field
    # e.g.
    # "transcript": {
    #     "start": "00:00.000",
    #     "end": "00:56.560",
    #     "content": "The following is a conversation with Vitalik Buterin, his second time on the podcast. Vitalik is the cofounder of Ethereum and one of the most influential people in cryptocurrency and technology broadly defined. Quick mention of our sponsors, Athletic Greens, Magic Spoon, Indeed, Four Sigmatic, and BetterHelp. Check them out in the description to support this podcast. As a side note, let me say that Ethereum, Bitcoin, and many other cryptocurrencies have been taking a wild ride of prices going up and down in the past few months. To me, the prices were never as important as the ideas, both technical and philosophical. Cryptocurrency has the potential to empower billions of people to participate in the global economy in a way that resists the manipulation by centralized power. Also with smart contracts, layer two technologies,"
    # }

    # parset the start, end, and content
    data = chunks.get("transcript", None)
    start = data.get("start", None)
    end = data.get("end", None)
    content = data.get("content", None)

    transcript_list.append((episode, chunk, start, end, content))
    # print(episode_number, chunk, start, end, content)
    # break

    # with conn.cursor() as cur:
    #     cur.execute(
    #         """
    #     INSERT INTO LEX_TRANSCRIPTS (episode, chunk, start_time, end_time, content)
    #     VALUES (%s, %s,%s, %s, %s)""",
    #         (episode, chunk, start, end, content),
    #     )
    #     conn.commit()
    # break

# Define the SQL statement and parameter placeholders
insert_sql = "INSERT INTO LEX_TRANSCRIPTS (episode, chunk, start_time, end_time, content) VALUES (%s, %s, %s, %s, %s)"
batch_size = 1000
# Execute the SQL statement and commit the changes
# Insert the data in batches with a progress bar
for i in tqdm(range(0, len(transcript_list), batch_size)):
    batch = transcript_list[i:i+batch_size]
    with conn.cursor() as cursor:
        cursor.executemany(insert_sql, batch)
        conn.commit()

# # get all rows from the table
# with conn.cursor() as cur:
#     cur.execute("SELECT * FROM LEX_TRANSCRIPTS")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)


# delte LEX_TRANSCRIPTS table
# with conn.cursor() as cur:
#     cur.execute("DROP TABLE LEX_TRANSCRIPTS")
#     conn.commit()
# Close the connection
conn.close()
