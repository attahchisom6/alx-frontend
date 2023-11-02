from flask import Flask, render_template
from livereload import Server

app = Flask(__name__, template_folder="/data/data/com.termux/files/home/alx-frontend/0x02-CSS_advanced")
# app = Flask(__name__)

@app.route('/static', strict_slashes=False)
def show_static_files():
    return render_template('index.html')

def run():
    if __name__ == "__main__":
        """server = Server(app.wsgi_app)
        try:
            server.serve(port=5000)
        finally:
            kill(server.watcher.watched_paths)
        """
        app.run(host="0.0.0.0", port=5000, debug=True)


run()
