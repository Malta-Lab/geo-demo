from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://23de18b7f2f5840799.gradio.live")

if __name__ == "__main__":
  app.run()
