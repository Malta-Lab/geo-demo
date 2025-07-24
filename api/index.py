from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://c296a3fe23aee53a63.gradio.live")

if __name__ == "__main__":
  app.run()
