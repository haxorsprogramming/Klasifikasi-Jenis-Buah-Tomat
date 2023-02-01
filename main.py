from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from helper.getConfig import getConfig

import pandas as pd
import numpy as np

baseUrl = getConfig("BASE_URL")
port = getConfig("PORT")

tomat_class = ['tomat_ceri', 'tomat_anggur', 'tomat_hijau', 'tomat_sayur']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = getConfig("UPLOAD_FOLDER")




