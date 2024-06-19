from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return redirect("https://303df21c191ba69efc.gradio.live")

if __name__ == "__main__":
  app.run()
