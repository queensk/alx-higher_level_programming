#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" - X GET -d ./header -o ./output; if grep -q "200 ok" ./header; then cat ./output;fi
