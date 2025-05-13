from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://31d09b34e645692540.gradio.live")

if __name__ == "__main__":
  app.run()
