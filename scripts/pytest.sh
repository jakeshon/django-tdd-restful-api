#!/bin/bash

#cd ../src && python manage.py test --settings=superapi.settings.developments
#cd ../src && pytest -s posts/tests/test_models.py -x --pdb
cd ../src && pytest -s posts/tests/test_views.py -x --pdb

