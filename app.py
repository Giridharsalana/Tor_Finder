import Torrsearch
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['POST' ,'GET'])

def search():
   if request.method == "POST":
      query = request.form['Query']
      Torrents = Torrsearch.Torrsearch(query)
      if Torrents == "No_Keyword":
         empty = True
      else:
         empty = False
      
      if Torrents == "Error_Connect":
         NoConnect = True
      else:
         NoConnect = False
      return render_template('index.html',Torr_list = Torrents, empty_flag = empty, No_Connect = NoConnect)
   return render_template('index.html')

@app.route('/about')
def About():
   return redirect('https://giridharsalana.netlify.app')

if __name__ == '__main__':
   app.run(debug = True)
