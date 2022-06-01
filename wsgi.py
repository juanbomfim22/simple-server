"""App entry point."""
from server import create_app
from livereload import Server

app = create_app()
app.debug = True

if __name__ == "__main__":
    # server = Server(app.wsgi_app)
    # server.serve()
    app.run(host="0.0.0.0", debug=True)
