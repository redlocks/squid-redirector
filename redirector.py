#!/usr/bin/scl enable rh-python35 -- python

from  json import load as jsl
from syslog import syslog
import sys

def get_urls_from_json(json_config_file=sys.argv[1]):
    with open(json_config_file) as file:
        return jsl(file)

def get_redirected_url(input_url):
    urls = get_urls_from_json()
    urls_to_redirect = urls.keys()
    splitted_input_url = input_url.replace('://', ' ').replace('/','').split()
    syslog(splitted_input_url[0])
    for url in urls_to_redirect:
        if url == splitted_input_url[1]:
            output_url = '{0}://{1}\n'.format(splitted_input_url[0], urls[url])
            syslog('Squid-redirector: URL [{0}] WAS REDIRECTED TO [{1}]'.format(input_url, output_url))
            return output_url
    return '\n'

def redirector():
    while True:
        in_url = sys.stdin.readline().strip()
        redirected_url = get_redirected_url(in_url)
        sys.stdout.write(redirected_url)
        sys.stdout.flush()
if __name__ == '__main__':
    redirector()
