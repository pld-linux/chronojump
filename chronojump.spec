Summary:	ChronoJump - system for measurement, management and statistics of the jump events
Summary(pl.UTF-8):	ChronoJump - system do pomiarów, zarządzania i statystyk skoków
Name:		chronojump
Version:	2.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
# release file (misses some files in many releases)
Source0:	https://download.gnome.org/sources/chronojump/2.3/%{name}-%{version}.tar.xz
# Source0-md5:	1dd65cc57bd32916c64e7f3d4e483a7f
# in case of missing files, use git
#Source0:	https://gitlab.gnome.org/GNOME/chronojump/-/archive/%{version}/%{name}-%{version}.tar.bz2
## Source0-md5:	3b6015b5a5ab3360bbb61ac94f4945c5
URL:		https://chronojump.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2
BuildRequires:	mono-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	python >= 2
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	mono >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ChronoJump is a complete system for measurement, management and
statistics of sport short-time tests. Chronojump is used by trainers,
teachers and students.

%description -l pl.UTF-8
ChronoJump to kompletny system do pomiarów, zarządzania i statystyk
krótkotrwałych zdarzeń sportowych. Jest używany przez trenerów,
nauczycieli oraz uczniów.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	chronopic-firmware/chronopic-firmwarecord/chronopic-firmwarecord.in

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' src/chronojump-importer/chronojump_importer.py

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I build/m4 -I build/m4/shave -I build/m4/shamrock
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/chronojump/*.la
# too common name
%{__rm} $RPM_BUILD_ROOT%{_bindir}/test-delete.py

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/chronojump/*.pdf

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md manual/chronojump_manual_en.pdf
%lang(es) %doc manual/chronojump_manual_es.pdf
%attr(755,root,root) %{_bindir}/chronojump
%attr(755,root,root) %{_bindir}/chronojump-test-accuracy
%attr(755,root,root) %{_bindir}/chronojump-test-jumps
%attr(755,root,root) %{_bindir}/chronojump-test-stream
%attr(755,root,root) %{_bindir}/chronojump_importer.py
%attr(755,root,root) %{_bindir}/chronojump_mini
%attr(755,root,root) %{_bindir}/chronopic-firmwarecord
%dir %{_libdir}/chronojump
%attr(755,root,root) %{_libdir}/chronojump/libchronopic.so*
%{_libdir}/chronojump/Chronojump.exe
%{_libdir}/chronojump/Chronojump.exe.mdb
%{_libdir}/chronojump/Chronojump_Mini.exe
%{_libdir}/chronojump/Chronojump_Mini.exe.mdb
%{_libdir}/chronojump/python
%{_datadir}/chronojump
%{_desktopdir}/chronojump.desktop
%{_iconsdir}/hicolor/scalable/apps/chronojump_icon.svg
