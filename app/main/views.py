from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .. import db


