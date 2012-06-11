from flask import Flask, jsonify, render_template, request
import Pyplinkseq

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
  vars = Pyplinkseq.var_fetch("", 10)
  return render_template('index.html', vars=vars)


if __name__ == '__main__':
  Pyplinkseq.set_project("/Users/hammer/Dropbox/codebox/clinical-genomics/pseq-project-one")
  app.run()
