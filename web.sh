#!/bin/bash

python `dirname $0`/web.py year > /var/www/static/disney/year.json

today=`date +%Y-%m-%d`
python `dirname $0`/web.py day > /var/www/static/disney/latest.json
cp /var/www/static/disney/latest.json /var/www/static/disney/${today}.json
