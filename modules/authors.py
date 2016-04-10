#!/usr/bin/python
# coding=utf-8

from flask import Blueprint, current_app, request

from flask.ext.api import status
from modules import mongo
from modules.authentication import auth

prefix_module = 'authors'
authors = Blueprint(prefix_module, __name__)


@authors.route('/names')
@auth.login_required
def GetAuthorsName():
    authors_container = mongo.db.phrases.distinct('author')
    if not authors_container:
        return {'status': 'Error', 'message': 'We could not found authors'}, status.HTTP_404_NOT_FOUND

    authors_container = sorted(authors_container)
    return {'satus': 'OK', 'authors': authors_container}
