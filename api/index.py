from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://25c04d80154c5d10df.gradio.liv")

if __name__ == "__main__":
  app.run()
