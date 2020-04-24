'''
	-This file process all the froms responses
	for the admin, and the guest users.
	
	-The methods name is consist of the forms methods names
	plus the work Process.
	example: addMatchForm + Process = addMathcFormProcess 
'''
from flask import Blueprint, jsonify, url_for
from flaskr.forms import addMatchForm, addGoalsForm, assignCardForm, changeFieldForm

processesApp = Blueprint('processes', __name__)

@processesApp.route("/addMatchFormProcess", methods=["POST"])
def addMatchFormProcess():
	form = addMatchForm()
	if form.validate_on_submit():
		#send a success message for the admin
		#and insert the data to the database
		return jsonify(success="The data have been inserted")
	#send an error message for the admin that include
	#all the possible errors
	return jsonify(error=form.errors)

@processesApp.route("/addGoalsFormProcess", methods=["POST"])
def addGoalsFormProcess():
	form = addGoalsForm()
	if form.validate_on_submit():
		#send a success message for the admin
		#and insert the data to the database
		return jsonify(success="The data have been inserted")
	#send an error message for the admin that include
	#all the possible errors
	return jsonify(error=form.errors)

@processesApp.route("/assignCardFormProcess", methods=["POST"])
def assignCardFormProcess():
	form = assignCardForm()
	if form.validate_on_submit():
		#send a success message for the admin
		#and insert the data to the database
		return jsonify(success="The data have been inserted")
	#send an error message for the admin that include
	#all the possible errors
	return jsonify(error=form.errors)

@processesApp.route("/changeFieldFormProcess", methods=["POST"])
def changeFieldFormProcess():
	form = changeFieldForm()
	if form.validate_on_submit():
		#send a success message for the admin
		#and insert the data to the database
		return jsonify(success="The data have been inserted")
	#send an error message for the admin that include
	#all the possible errors
	return jsonify(error=form.errors)

