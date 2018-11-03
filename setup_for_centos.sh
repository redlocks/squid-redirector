#!/bin/bash

#chmod +x ./setup_for_centos
path_to_redirector = /usr/local/squid-redirector/
path_to_rsyslog_conf = /etc/rsyslog.d/
path_to_logrotate_conf = /etc/logrotate.d/
path_to_squid_conf = /etx/squid/squid.conf

chmod +x redirector.py && cp /redirector.py $path_to_redirector
cp /config.json $path_to_redirector
cp /rsyslog-redirector.conf $path_to_rsyslog_conf
cp /logrotate-redirector $path_to_logrotate_conf

echo "url_rewrite_children 4" >> $path_to_squid_conf
echo "url_rewrite_program /usr/local/squid-redirector/redirector.py /usr/local/squid-redirector/config.json" >> $path_to_squid_conf

service squid restart
