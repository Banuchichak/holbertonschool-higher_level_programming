#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    # Məlumatın URL-encoded formatına salınması
    data = urllib.parse.urlencode(values)
    # Məlumatın baytlara çevrilməsi
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
