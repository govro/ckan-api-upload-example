#!/usr/bin/env python
import os
import urllib
import requests
import json
import pprint
import random

# Constants that have to be changed
AUTHORIZATION_CODE = '' or os.getenv('AUTHORIZATION_CODE')
CKAN_URL = '' or os.getenv('CKAN_URL')

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'name': 'something_unique-' + str(random.randint(0, 10000)), # take care the name should be always unique
    'notes': 'Tra la la',
    'owner_org': 'aadr',
}

# We'll use the package_create function to create a new dataset.
url = CKAN_URL + '/api/3/action/package_create'

# Creating a dataset requires an authorization header.
headers = {'Authorization': AUTHORIZATION_CODE,
           'Content-Type': 'application/x-www-form-urlencoded'}

# Make the HTTP request.
response = requests.post(url,
                         data=urllib.quote(json.dumps(dataset_dict)), # here, we are converting the dictionary into
                                                                      # '%7B%22notes%22%3A%20%22Tra%20la%20la%22%2C%20%22owner_org%22%3A%20%22aadr%22%2C%20%22name%22%3A%20%22something_unique-7625%22%7D'
                         headers=headers)
assert response.status_code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.content)
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)
