# Flask API

Created an API using Python, Flask and SQL. It shows the US military bases in South Korea and how far they are from the Demilitarized Zone.

## Getting Started

1. Fork and clone this repository

2. Change into new directory

3. Install dependencies in your virtual environment

4. Install Pipenv with either Pip or Homebrew.

- Pip: `pip3 install pipenv`
- Homebrew: `brew install pipenv`

5. Create the virtual environment, `pipenv --three`

6. Run the virtual environment, `workon flask-api`

7. Install the dependencies `pipenv install flask`

## Required

click==8.1.2
Flask==2.1.1
importlib-metadata==4.11.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
Werkzeug==2.1.1
zipp==3.8.0

## Routes

`/militarybase/` GET request
Get all the bases that I added to the database

`/militarybase/<id>` GET request
Select single review by id

`/militarybase/` POST request
Create new entry

`/militarybase/<id>` DELETE request
Delete entry by id

## Contributing

Feel free to contribute by submitting an issue or pull request. Any and all input is appreciated.

## Add "Chingae" Navy Base to test the Add Operations

Input the following:

for base_name put " Chinhae ",

for branch_in_controll put " Navy ",

for location put " Jinhae-gu ",

for miles_from_dmv put " 150 "

## Author

Lyndon St.Luce

## Acknowledgements

I got my data from https://militarybases.com/overseas/south-korea/, Google Maps and Wikipedia.
