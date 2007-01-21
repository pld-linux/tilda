Summary:	Tilda - a drop-down terminal
Summary(pl):	Tilda - wyskakuj±cy terminal
Name:		tilda
Version:	0.9.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/tilda/%{name}-%{version}.tar.gz
# Source0-md5:	773d47e3985f7e778b662a38b053c1df
URL:		http://tilda.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.0.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libconfuse-devel
BuildRequires:	pkgconfig >= 1:0.12.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	vte-devel >= 0.11.12
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a drop-down terminal.

%description -l pl
Tilda to wyskakuj±cy terminal.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	localedir=%{_datadir}/locale

rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/tilda.desktop
%{_pixmapsdir}/tilda.png
