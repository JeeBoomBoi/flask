from flask import Flask, render_template, make_response, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def cooky():
    count = int(request.cookies.get('visit-count', 0))
    count += 1
    message = 'You have visited this page ' + str(count) + ' times'

    resp = make_response(message)
    resp.set_cookie('visit-count', str(count))
    return resp

app.run()
