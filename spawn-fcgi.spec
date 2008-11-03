Summary:	Spawn fcgi-process directly
Summary(pl.UTF-8):	Bezpośrednie uruchamianie procesów fcgi
Name:		spawn-fcgi
Version:	1.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://cgit.stbuehler.de/gitosis/spawn-fcgi/snapshot/%{name}-932809088d5da036e1c46b5d615a1dfcebb5cef0.tar.bz2
# Source0-md5:	74753cc8541b6a7a858535071c3404a8
URL:		http://cgit.stbuehler.de/gitosis/spawn-fcgi/
BuildRequires:	glib2-devel
#BuildRequires:	waf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# use local waf
%define		__waf	./waf

%description
spawn-fcgi is used to spawn fcgi-process directly without the help of
a webserver or the programm itself.

%description -l pl.UTF-8
spawn-fcgi służy do uruchamiania procesów fcgi bezpośrednio, bez
pomocy serwera WWW ani samego programu.

%prep
%setup -q -n %{name}

%build
%waf configure \
	--prefix=%{_prefix}

%waf build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

%waf install \
	--destdir=$RPM_BUILD_ROOT

cp -a spawn-fcgi.1 $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/spawn-fcgi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %{_sbindir}/spawn-fcgi
%{_mandir}/man1/spawn-fcgi.1*
