
# Purpose: Create a Flask app and define the necessary API routes

from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from models import (SearchTerm, Campaign, AdGroup)

# Initialize Flask app with SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def main_page():
    return "<html><head></head><body>A RESTful API in Flask using SQLAlchemy. For more info on usage, go to <a href>https://github.com/mgreenw/flask-restapi-example</a>.</body></html>"

# Search Value Routes
@app.route('/api/v1/search_value/<id>')
def show_value_by(id):
    try:
        search_terms = SearchTerm.query.filter_by(id=id).first()
        return jsonify(search_terms.serialize)
    except:
        return not_found("Search value doesn't exist")


@app.route('/api/v1/search_value', methods=['POST'])
def create_value():
    search_terms = SearchTerm(request.get_json()[search_terms])
    db.session.add(search_terms)
    db.session.commit()
    return jsonify({'search_terms': search_terms.serialize}), 201

#Alias Routes
@app.route('/api/v1/search_values/<id>')
def show_value(id):
    try:
        search_term = SearchTerm.query.filter_by(id=id).first_or_404()
        return jsonify(id=SearchTerm.search_term_id)
    except:
        return not_found("Search value does not exist.")

@app.route('/api/v1/search_values', methods=['POST'])
def create_review():
    request_json = request.get_json()
    if not request.is_json or 'doctor_id' not in request_json or 'description' not in request_json:
        return bad_request('Missing required data.')
    doctor_id = request_json['doctor_id']

    # If the search_term_id is invalid, generate the appropriate 400 message
    try:
        search_term = SearchTerm(doctor_id=SearchTerm.search_term_id, description=request_json['search_term'])
        db.session.add(search_term)
        db.session.commit()
    except:
        return bad_request('Given search_term_id does not exist.')
    return jsonify({'search_term': search_term.serialize}), 201


# Custom Error Helper Functions
def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response
