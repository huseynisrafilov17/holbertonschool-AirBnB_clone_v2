#!/usr/bin/python3
from models.__init__ import storage
from models.state import State
from flask import Flask, render_template

states = storage.all(State).values()
new_states = sorted(states, key=lambda x: x.name)
print(new_states[1].cities)
