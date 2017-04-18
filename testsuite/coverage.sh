#!/bin/bash
# Generate a coverage report

# Usage: ./coverage.sh [--user] [testsuite_options]
# if --user, use gnatpython installed in user site

root=`dirname $0`

export COVERAGE_PROCESS_START=`pwd`/coverage.rc
export COVERAGE_DIR=`pwd`

rm -f .coverage*

if [ "$PYTHON" = "" ]; then
   PYTHON=python
fi

python=`which $PYTHON`
mkdir -p sitecustomize
export PYTHONPATH=`pwd`/sitecustomize:$PYTHONPATH

cat <<EOF > sitecustomize/sitecustomize.py
import coverage; coverage.process_startup()
EOF

cat <<EOF > coverage.rc
[run]
cover_pylib = True
parallel = True
EOF


$root/run-testsuite $@

STYLE_CHECKER_DIR="$root/../asclib"
STYLE_CHECKER_MODULES=`find $STYLE_CHECKER_DIR -name '*.py' -print`
coverage combine
coverage report $STYLE_CHECKER_MODULES
coverage html $STYLE_CHECKER_MODULES
perl -pi -e "s;$STYLE_CHECKER_DIR/;;" htmlcov/*
