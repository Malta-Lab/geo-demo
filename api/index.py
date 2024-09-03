from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://6e047d33eb553e5da8.gradio.live")

if __name__ == "__main__":
  app.run()
