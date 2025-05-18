from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app=Flask(__name__) #esaa flaskis aplikacia
app.config["SECRET_KEY"]= "es veli gamoiyeneba imistvis rom moxmareblis mier shemotanili informacia iyos daculi"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/// database.dab" #bazizs konfiguracia gavwere tu romel monacemta bazas vixmart da ra qvia mis fails
db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view="login"