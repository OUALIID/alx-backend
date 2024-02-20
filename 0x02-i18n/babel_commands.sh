#!/bin/bash

# Extract messages to messages.pot
pybabel extract -F babel.cfg -o messages.pot .

# Initialize English translation
pybabel init -i messages.pot -d translations -l en

# Initialize French translation
pybabel init -i messages.pot -d translations -l fr

# Compile translations
pybabel compile -d translations
