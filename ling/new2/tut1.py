from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'Maths' :50, 'Cultural' :45, 'Chemistry' :44, 'CTPS' :42, 'English' :28}
    return render_template('hello.html', result = dict)

if __name__ == "__main__":
    app.run()
