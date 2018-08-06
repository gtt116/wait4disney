#/bin/bash
cd `dirname $0`

venv/bin/disney-fetch
venv/bin/disney-publish day
venv/bin/disney-publish year
