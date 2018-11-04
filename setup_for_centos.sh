#!/bin/bash

#chmod +x ./setup_for_centos


yum -q list installed squid &>/dev/null && echo "squid is nstalled" || yum -y install squid
yum -q list installed centos-release-scl &>/dev/null && echo "centos-release-scl is installed" || yum -y install centos-release-scl
yum -q list installed rh-python36 &>/dev/null && echo "rh-python36 is nstalled" || yum -y install rh-python36

path_to_redirector=/usr/local/squid-redirector/
path_to_rsyslog_conf=/etc/rsyslog.d/
path_to_logrotate_conf=/etc/logrotate.d/
path_to_squid_conf=/etc/squid/squid.conf

chmod +x redirector.py && cp redirector.py $path_to_redirector
cp config.json $path_to_redirector
cp redirector_rsyslog.conf $path_to_rsyslog_conf
cp redirector_logrotate $path_to_logrotate_conf

echo "url_rewrite_children 5" >> $path_to_squid_conf
# Number of instances of the above program that should run concurrently.
# 5 is good enough but you should go for 10 at least. Anything below 5 would not work properly.
echo "url_rewrite_program /usr/local/squid-redirector/redirector.py /usr/local/squid-redirector/config.json" >> $path_to_squid_conf

service squid restart
