from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://63530c368cb14294ec.gradio.live")

if __name__ == "__main__":
  app.run()
