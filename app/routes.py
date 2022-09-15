from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
    <html>
        <head><title>Front Page</head></title>
        <body>
            <h2>Hello Word!</h2>
        </body>
    </html>
    '''