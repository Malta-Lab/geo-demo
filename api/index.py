from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://006440476821675ade.gradio.live")

if __name__ == "__main__":
  app.run()
