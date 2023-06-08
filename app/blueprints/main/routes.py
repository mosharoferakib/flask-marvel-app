from flask import Flask, render_template
from . import bp
import requests


@bp.route('/')
def home():
    return render_template('index.jinja',title='home')

