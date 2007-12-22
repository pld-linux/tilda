Summary:	Tilda - a drop-down terminal
Summary(pl.UTF-8):	Tilda - wyskakujący terminal
Name:		tilda
Version:	0.9.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/tilda/%{name}-%{version}.tar.gz
# Source0-md5:	c497f82f180e128a1e6f301c6b2463d9
Patch0:		%{name}-glade_file.patch
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

%description -l pl.UTF-8
Tilda to wyskakujący terminal.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry
install tilda.glade $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/tilda.desktop
%{_pixmapsdir}/tilda.png
