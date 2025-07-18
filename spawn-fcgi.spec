Summary:	Spawn fcgi-process directly
Summary(pl.UTF-8):	Bezpośrednie uruchamianie procesów fcgi
Name:		spawn-fcgi
Version:	1.6.4
Release:	2
License:	BSD
Group:		Networking/Daemons/HTTP
Source0:	http://www.lighttpd.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	bf269849995ab8b3a8989779fa5818aa
# Patch to chown & chmod the created unix socket even when run as a regular user.
Patch0:		%{name}-socket_chown.patch
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
%setup -q
#%%patch0 -p1 update or drop

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
%doc AUTHORS COPYING NEWS README doc/run-*
%attr(755,root,root) %{_sbindir}/spawn-fcgi
%{_mandir}/man1/spawn-fcgi.1*
