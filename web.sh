#!/bin/bash

home=/var/www/static/disney/

# because pipe redirect will clean the file before invoke the command,
# if command runs for a long time, the file will keep empty. This method
# work around it.
python `dirname $0`/web.py year > $home/year_new.json
mv $home/year_new.json $home/year.json

python `dirname $0`/web.py day > $home/latest_new.json

today=`date +%Y-%m-%d`
cp $home/latest_new.json $home/latest.json
mv $home/latest_new.json $home/${today}.json
