Summary:	Spawn fcgi-process directly
Summary(pl):	Bezpo¶rednie uruchamianie procesów fcgi
Name:		spawn-fcgi
Version:	1.2.0
Release:	1
License:	Artistic
Group:		Applications
Source0:	http://www.incremental.de/products/lighttpd/download/%{name}-%{version}.tar.gz
# Source0-md5:	6bda08629f3f88dc9a4ff24185bb31bc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spawn-fcgi is used to spawn fcgi-process directly without the help of
a webserver or the programm itself.

%description -l pl
spawn-fcgi s³u¿y do uruchamiania procesów fcgi bezpo¶rednio, bez
pomocy serwera WWW ani samego programu.

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
