#!/bin/bash
# Sends an OPTIONS request to a URL and displays all accepted HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d' ' -f2-
