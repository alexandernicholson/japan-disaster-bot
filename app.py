###
## The goal of this file is to create a Slack bot which gets the latest post from a Mastodon instance to post to Slack.
## It can also translate the post from Japanese to English.
###

import sqlite3
import os
import requests
import json
from bs4 import BeautifulSoup

# Use an env variable to store the Slack API token.
webhook_url = os.environ['SLACK_WEBHOOK_URL']

# To make things super simple, we will use the Slack Incoming Webhooks API to post to Slack.
# https://api.slack.com/incoming-webhooks
def post_to_slack(message):
    webhook_url = os.environ['SLACK_WEBHOOK_URL'] or 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX'
    data = {'text': message}
    r = requests.post(webhook_url, data=json.dumps(data))

# Create the database if it doesn't exist.
if not os.path.exists('posts.db'):
    conn = sqlite3.connect('posts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE posts (
                    id integer primary key autoincrement,
                    internal_id text,
                    url text,
                    content text
                );
            ''')
    conn.commit()

# The posts are in a JSON format and at https://unnerv.jp/api/v1/accounts/1/statuses, so we need to fetch them with requests.
r = requests.get('https://unnerv.jp/api/v1/accounts/1/statuses')
data = json.loads(r.text)

conn = sqlite3.connect('posts.db')
c = conn.cursor()

for post in data:
    c.execute('SELECT * FROM posts WHERE internal_id=?', (post['id'],))
    if c.fetchone() is None:
        print(f'Posting {post["id"]} to Slack.')
        # Remove the HTML tags from the post content using Markdown.
        #post_to_slack(post['content'] + " " + post['url'])
        c.execute('INSERT INTO posts (internal_id, url, content) VALUES (?, ?, ?)', (post['id'], post['url'], post['content']))
        conn.commit()

conn.close()
