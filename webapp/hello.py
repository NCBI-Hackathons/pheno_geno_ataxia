from flask import Flask, render_template, request
app = Flask(__name__)
import os

@app.route('/')
def input():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def analysis():
   if request.method == 'POST':
      result = request.form
      cravat = "cravat " + result.get('dataFile') + " -t text -d " + result.get('familyID')
      #THREADED
      os.system(cravat)
      annovar = None
      os.system(annovar)
      #/END THREADS
      return render_template('ran.html', program = "All", familyID = result.get('familyID'))

@app.route('/result',methods = ['POST', 'GET'])
def anovar():
   if request.method == 'POST':
      result = request.form
      command = "cravat " + result.get('dataFile') + " -t text -d " + result.get('familyID')
      os.system(command)
      return render_template('ran.html', program = "Anovar", familyID = result.get('familyID'))


if __name__ == '__main__':
   app.run(debug = True)
