from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://d28d8fab3eea0e2c4c.gradio.live")

if __name__ == "__main__":
  app.run()
