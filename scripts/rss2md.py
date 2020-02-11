# Fork from https://gist.github.com/rebornix/5363138

import feedparser
import html2markdown
from datetime import datetime

rss_url = "https://www.sans.org/instructors/rss-schedule/lodrina-cherne"

feed = feedparser.parse(rss_url )
filename = "index.md"
f = open(filename,'w')

#name = rss_url.split('/')[-1].replace('-', ' ').title()

post_title = "Teaching Schedule"
f.write('---\n')
f.write('title: ' + post_title + '\n')
process_date = str(datetime.now())
f.write('date: ' + process_date +'\n')
f.write('draft: false\n')
f.write('---\n')
#f.write ("## My teaching engagements\n")

items = feed["entries"]
for item in items:
    feed_title = str(item["title"]).split(",")[0]
    feed_link = str(item["link"])
    feed_description = html2markdown.convert(str(item["description"]))
    
    f.write ("### [" + feed_title + "]("+feed_link+")\n")
    f.write (feed_description+"\n")
    f.write ("\n")
