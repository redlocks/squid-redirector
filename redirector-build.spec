Name: redirector
Version: 1.0
Release: 1
Summary: A simple redirector for squid
License: GPL
Source: redirector-1.0.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.x86_64

Requires: rsyslog
Requires: logrotate
Requires: squid
Requires: centos-release-scl
Requires: rh-python36
%define _unpackaged_files_terminate_build 0

%description
This package installs a squid-redirector and a configuration file for it in /usr/local/redirector/,
config for the rsyslog and logrotate, indicates the redirector in squid.conf

%prep
%setup -q 

%build


%install
rm -rf $RPM_BUILD_ROOT
%{__install} -Dm 0644 redirector.py $RPM_BUILD_ROOT/usr/local/redirector/redirector.py
%{__install} -Dm 0644 config.json $RPM_BUILD_ROOT/usr/local/redirector/config.json
%{__install} -Dm 0644 redirector_rsyslog.conf $RPM_BUILD_ROOT/etc/rsyslog.d/redirector_rsyslog.conf
%{__install} -Dm 0644 redirector_logrotate $RPM_BUILD_ROOT/etc/logrotate.d/redirector_logrotate

%files
%defattr(-,root,root)
/usr/local/redirector/redirector.py
/usr/local/redirector/config.json
/etc/rsyslog.d/redirector_rsyslog.conf
/etc/logrotate.d/redirector_logrotate

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "url_rewrite_children 5" >> /etc/squid/squid.conf
echo "url_rewrite_program /usr/local/redirector.py /usr/local/redirector/config.json" >> /etc/squid/squid.conf
chmod +x /usr/local/redirector/redirector.py
