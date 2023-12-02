#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__,template_folder='templates')


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/search/<state>/<city>/<zip>', methods=['GET'])
def search_location(state, city, zip):
    # Process the values (you can perform any logic or use them as needed)
    

    # Return the result as a response
    return render_template('pages/output.html', state=state, city=city, zip=zip)








#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#
# Default port:

if __name__ == '__main__':
    app.run()

