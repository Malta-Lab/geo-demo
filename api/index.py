from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://0bc845018c13a57e90.gradio.live")

if __name__ == "__main__":
  app.run()
