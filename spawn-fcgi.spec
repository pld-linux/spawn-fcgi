Summary:	spawn fcgi-process directly
Name:		spawn-fcgi
Version:	1.1.0
Release:	1
License:	Artistic
Group:		Applications
Source0:	http://www.incremental.de/products/lighttpd/download/%{name}-%{version}.tar.gz
# Source0-md5:	c0c298132db154008ea138f3a0329bb2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spawn-fcgi is used to spawn fcgi-process directly without the help of a
webserver or the programm itself.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt ChangeLog
%attr(755,root,root) %{_sbindir}/*
