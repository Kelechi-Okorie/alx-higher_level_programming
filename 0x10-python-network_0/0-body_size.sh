#!/usr/bin/bash
# makes a http request using curl and displays size of the body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
