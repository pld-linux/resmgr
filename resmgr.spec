Summary:	Resource Manager
Summary(pl):	Zarz�dca zasob�w
Name:		resmgr
Version:	1.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.lst.de/pub/people/okir/resmgr/%{name}-%{version}.tar.bz2
# Source0-md5:	c231de6ca7d59265eeeccdfcb8090801
URL:		http://www.lst.de/~okir/resmgr/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this Resource Manager is to provide a common framework
for applications such as serial terminal emulators, CD writers,
scanner software, MIDI players.

%description -l pl
Celem tego zarz�dcy zasob�w jest dostarczenie wsp�lnego szkieletu dla
aplikacji takich jak emulatory terminali szeregowych, nagrywarki CD,
programy do skanowania, odtwarzacze MIDI.

%package devel
Summary:	Header files for resmgr library
Summary(pl):	Pliki nag��wkowe biblioteki resmgr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for resmgr library.

%description devel -l pl
Pliki nag��wkowe biblioteki resmgr.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	PAMDIR=$RPM_BUILD_ROOT/%{_lib}/security \
	SBINDIR=$RPM_BUILD_ROOT%{_sbindir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libresmgr.so.*.* libresmgr.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE INSTALL README TODO
%attr(755,root,root) %{_sbindir}/resmgr
%attr(755,root,root) %{_sbindir}/resmgrd
%attr(755,root,root) %{_libdir}/libresmgr.so.*.*
%attr(755,root,root) /%{_lib}/security/pam_resmgr.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/resmgr.conf
%{_mandir}/man1/resmgr.1*
%{_mandir}/man5/resmgr.conf.5*
%{_mandir}/man8/pam_resmgr.8*
%{_mandir}/man8/resmgrd.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libresmgr.so
%{_includedir}/resmgr.h
%{_mandir}/man3/resmgr.3*
