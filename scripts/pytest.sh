#!/bin/bash

cd ../src && python manage.py test --settings=superapi.settings.developments
