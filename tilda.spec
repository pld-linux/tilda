Summary:	Tilda - a drop-down terminal
Summary(pl.UTF-8):	Tilda - wyskakujący terminal
Name:		tilda
Version:	0.9.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/tilda/%{name}-%{version}.tar.gz
# Source0-md5:	b44ebe04fdfd312e9ddc5e0ed77f4289
Patch0:		%{name}-glade.patch
Patch1:		%{name}-desktop.patch
URL:		http://freshmeat.net/projects/tilda/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.0.0
BuildRequires:	intltool
BuildRequires:	libconfuse-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
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
%patch -P0 -p1
%patch -P1 -p1

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

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/tilda.desktop
%{_pixmapsdir}/tilda.png
