from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://f31f5b3016f9fcfa0e.gradio.live")

if __name__ == "__main__":
  app.run()
