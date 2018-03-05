#!/bin/bash

set -e

if [ -z $1 ]; then
    echo -e "\n\n\tusage: sleeper.sh time_to_sleep\n\n\n"
    exit 1
fi

echo "sleeping for $1"
sleep $1

exit 0
