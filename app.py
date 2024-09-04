from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    rss_url = 'aggregated_forex_feed.xml'
    feed = feedparser.parse(rss_url)
    news_items = []
    for entry in feed.entries:
        news_items.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })
    return render_template('index.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True)
