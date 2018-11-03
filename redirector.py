#!/usr/bin/scl enable rh-python36 -- python

from  json import load as jsl
from syslog import syslog
import sys

def get_urls_from_json(json_config_file=sys.argv[1]):#получаем конфигурационный файл из аргументов командной строки
    with open(json_config_file) as file:
        return jsl(file)# загружаем данные в json load и возвращаем

def get_redirected_url(input_url):
    urls = get_urls_from_json()#Получаем url из файла конфигурации в виде ключ:значение
    urls_to_redirect = urls.keys()#url которые необходимо редиректить
    splitted_input_url = input_url.replace('://', ' ').replace('/','').split()# так как url приходит на вход в виде: URL ip-address/fqdn ident method то отбрасываем все ненужное
    for url in urls_to_redirect:#проходим по всем url для редиректа
        if url == splitted_input_url[1]:#смотрим является ли url редиректным
            output_url = '{0}://{1}\n'.format(splitted_input_url[0], urls[url])#изменяем url в соответствии с правилом в конфиге
            syslog('Squid-redirector: URL [{0}] WAS REDIRECTED TO [{1}]'.format(input_url, output_url))#логируем смену url в syslog
            return output_url
    return '\n'#если url не для редиректа, возвращаем пустую строку

def redirector():
    while True:
        in_url = sys.stdin.readline().strip()#считываем url из стандартного потока ввода
        redirected_url = get_redirected_url(in_url)#получаем измененный url
        sys.stdout.write(redirected_url)#пишем измененный url в ствндартный поток вывода
        sys.stdout.flush()#очищаем поток
if __name__ == '__main__':
    redirector()

