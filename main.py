"""
@Author: Neeraj Venugopal
@Date: 27th February 2018
This is the main Python Server Code

"""

# Using Flask framework and not Django :P

from flask import Flask, request, render_template

application = Flask(__name__)

@application.route("/")
def webPageStartup():
    return render_template("home.html")

if __name__ == "__main__":
    application.run()