from flask import Flask, render_template, request

import youtube_dl

app = Flask(__name__)

@app.route("/")

def index():

    return render_template("index.html")

@app.route("/download", methods=["POST"])

def download():

    url = request.form["url"]

    ydl_opts = {

        "format": "bestvideo[height<=480]+bestaudio/best[height<=480]",

        "outtmpl": "%(title)s.%(ext)s",

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=False)

        formats = info.get("formats", [])
        
        filesize = formats.filesize

    return render_template("download.html", formats=formats, url=url, filesize=filesize)

if __name__ == "__main__":

    app.run(debug=True)

