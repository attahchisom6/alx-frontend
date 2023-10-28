from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.route('/static', strict_slashes=False)
def show_static_files():
    return render_template('19-index.html')

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve(port=5000)
