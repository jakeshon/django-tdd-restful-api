#!/bin/bash

#cd ../src && python manage.py test --settings=superapi.settings.developments
cd ../src && pytest -s posts/tests/test_models.py 
