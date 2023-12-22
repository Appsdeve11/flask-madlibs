from flask import Flask, render_template, request
from story import Story

app = Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        words = []
        for word in story.prompts:
            value = request.form.get(word)
            words.append(value)
        filled_story = story.generate(words)
        return render_template('result.html', filled_story=filled_story)
    return render_template('index.html', prompts=story.prompts)