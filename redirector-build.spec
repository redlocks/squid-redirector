Name: redirector
Version: 1.0
Release: 1
Summary: redirector for squid
License: GPL
Source: redirector-1.0.tar.gz
#Source0: redirector.py
#Source1: 00-redirector.conf
#Source2: redirector 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.x86_64
Requires: rsyslog
Requires: logrotate
Requires: squid
#Requires: python3
%define _unpackaged_files_terminate_build 0
%description
python redirector for flask

%prep
%setup -q 

%build


%install

rm -rf $RPM_BUILD_ROOT





%{__install} -Dm 0644 redirector.py $RPM_BUILD_ROOT/usr/local/redirector/redirector.py



%{__install} -Dm 0644 00-redirector.conf $RPM_BUILD_ROOT/etc/rsyslog.d/00-redirector.conf
%{__install} -Dm 0644 redirector $RPM_BUILD_ROOT/etc/logrotate.d/redirector

%files
%defattr(-,root,root)
/usr/local/redirector/redirector.py
/etc/rsyslog.d/00-redirector.conf
/etc/logrotate.d/redirector

%clean

rm -rf $RPM_BUILD_ROOT

%post
echo "url_rewrite_children 3" >> /etc/squid/squid.conf
echo "url_rewrite_program /usr/local/redirector.py" >> /etc/squid/squid.conf
chmod +x /usr/local/redirector/redirector.py
