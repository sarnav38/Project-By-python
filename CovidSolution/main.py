from flask import Flask,render_template,request
app = Flask(__name__)
import pickle

file =open('model.pkl','rb')
clf = pickle.load(file)
file.close()


@app.route('/', methods =["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        print(myDict)
        fever = float(myDict['Fever'])
        age = int(myDict['Age'])
        bodyPain = int(myDict['bodyPain'])
        runnyNoise = int(myDict['runnyNoise'])
        diffBreath = int(myDict['diffBreath'])
        inputFeatures = [fever,bodyPain,age,runnyNoise,diffBreath]
        infPro = clf.predict_proba([inputFeatures])[0][1]
        print(infPro)
        return render_template('show.html',inf =infPro)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)