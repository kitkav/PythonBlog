import os
import secrets

from flaskblog import app, db, bcrypt, mail

#
# posts = [
#     {
#         'author': 'Kavit Doe',
#         'title': 'Blog Post 1',
#         'content': 'First post',
#         'date_posted': 'January 14, 2019'
#     },
#     {
#         'author': 'Kevin P',
#         'title': 'Blog Post 2',
#         'content': 'Second post',
#         'date_posted': 'January 12, 2019'
#     }
# ]
#
