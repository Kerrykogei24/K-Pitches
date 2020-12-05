from .forms import UpdateProfile, PitchForm,CommentForm
from flask_login import login_required, current_user
from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .. import db,photos
import datetime

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

# Getting reviews by category
    interview_piches = Pitch.get_pitches('interview')
    product_piches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')


    title = 'Home - Welcome to The best Pitches Review Website Online'

    return render_template ('index.html', title = title, interview = interview_piches, product = product_piches, promotion = promotion_pitches)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches_count,date = user_joined)