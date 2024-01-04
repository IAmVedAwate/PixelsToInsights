from flask import Flask, render_template, request, redirect
import video_to_imgs as vi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        ylink = request.form['ylink']
        vi.video_to_img(ylink)
        return render_template("index3.html")

if __name__ == '__main__':
    app.run(debug=True)
