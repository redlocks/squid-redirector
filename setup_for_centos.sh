#!/bin/bash

#проверка установленного пайтона, сквида, если нет - установить
#chmod +x ./setup_for_centos
path_to_redirector = /usr/local/squid-redirector/
path_to_rsyslog_conf = /etc/rsyslog.d/
path_to_logrotate_conf = /etc/logrotate.d/
path_to_squid_conf = /etx/squid/squid.conf

chmod +x redirector.py && cp /redirector.py $path_to_redirector
cp /config.json $path_to_redirector
cp /rsyslog-redirector.conf $path_to_rsyslog_conf
cp /logrotate-redirector $path_to_logrotate_conf

echo "url_rewrite_children 5" >> $path_to_squid_conf
# Number of instances of the above program that should run concurrently.
# 5 is good enough but you should go for 10 at least. Anything below 5 would not work properly.
echo "url_rewrite_program /usr/local/squid-redirector/redirector.py /usr/local/squid-redirector/config.json" >> $path_to_squid_conf

service squid restart
