from flask import Flask
from flask import render_template
import os.path

app = Flask(__name__)
path="howmanyopen.txt"

@app.route("/")
def open_page():
    letezik=os.path.isfile(path)
    if letezik==False:
        f=open(path,"w")
        f.write("0")
        f.close()
    f=open(path,"r")
    szoveg=f.readline()
    f.close()
    x=int(szoveg)
    x=x+1
    f=open(path,"w")
    f.write(str(x))
    f.close()
    return render_template('index.html')
@app.route("/open")
def howmany():
    letezik=os.path.isfile(path)
    if letezik==False:
        f=open(path,"w")
        f.write("0")
        f.close()
    f=open(path,"r")
    szoveg=f.readline()
    f.close()
    x=int(szoveg)
    return "<p>A weboldalt "+str(x)+" alkalommal nyitották meg.</p>"
@app.route("/reset")
def reset():
    f=open(path,"w")
    f.write("0")
    f.close()
    return "<p>Az oldal számlálóját alaphelyzetbe állítottam.!</p>"