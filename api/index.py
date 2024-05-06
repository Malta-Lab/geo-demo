from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://654e67d17291290a57.gradio.live")

if __name__ == "__main__":
  app.run()
