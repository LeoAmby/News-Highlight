from flask import render_template
from . import main

@main.app_errohandler(404)
def four_Ow_four(error):

    '''
    Function for rendering the 404 error page
    '''
    title = 'Error 404'
    return render_template('fourOwfour.html, title = title'),404