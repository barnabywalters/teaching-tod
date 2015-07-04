# coding: utf-8

import libfile
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
	return '<strong>{}</strong>'.format(libfile.say_hello())


@app.route('/<name>')
def named(name):
	return '<strong>{}</strong>'.format(libfile.say_hello(name))


if __name__ == '__main__':
	app.run()