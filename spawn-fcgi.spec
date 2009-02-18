Summary:	Spawn fcgi-process directly
Summary(pl.UTF-8):	Bezpośrednie uruchamianie procesów fcgi
Name:		spawn-fcgi
Version:	1.6.0
Release:	1
License:	BSD
Group:		Networking/Daemons/HTTP
Source0:	%{name}.tar.bz2
# Source0-md5:	dd760c6834744cc571b194a0853dc7b3
URL:		http://redmine.lighttpd.net/projects/spawn-fcgi
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	%{_prefix}/sbin

%description
spawn-fcgi is used to spawn fcgi-process directly without the help of
a webserver or the programm itself.

%description -l pl.UTF-8
spawn-fcgi służy do uruchamiania procesów fcgi bezpośrednio, bez
pomocy serwera WWW ani samego programu.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_sbindir}/spawn-fcgi
%{_mandir}/man1/spawn-fcgi.1*
