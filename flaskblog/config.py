import os
import json


class Config:
    SECRET_KEY = '877d95adca69627c3bb1f4c942ba07cd'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kitkavm@gmail.com'
    MAIL_PASSWORD = 'M,C.z@-g#>8\:H5Tt&4io?3s.'
