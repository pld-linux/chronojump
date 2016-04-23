Summary:	ChronoJump - system for measurement, management and statistics of the jump events
Summary(pl.UTF-8):	ChronoJump - system do pomiarów, zarządzania i statystyk skoków
Name:		chronojump
Version:	1.6.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/chronojump/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	e9c11132e2981a22e746a223e239c69b
URL:		http://chronojump.org/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer0.10-devel >= 0.10
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	mono-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	python >= 2
BuildRequires:	sed >= 4.0
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

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' chronopic-firmware/chronopic-firmwarecord/chronopic-firmwarecord.in

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/chronojump/*.la

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
%doc AUTHORS ChangeLog README manual/{chronojump_crash,chronojump_manual_en,troubleshooting}.pdf
%lang(es) %doc manual/chronojump_manual_es.pdf
%attr(755,root,root) %{_bindir}/chronojump
%attr(755,root,root) %{_bindir}/chronojump-test-accuracy
%attr(755,root,root) %{_bindir}/chronojump-test-jumps
%attr(755,root,root) %{_bindir}/chronojump-test-stream
%attr(755,root,root) %{_bindir}/chronojump_mini
%attr(755,root,root) %{_bindir}/chronopic-firmwarecord
%dir %{_libdir}/chronojump
%attr(755,root,root) %{_libdir}/chronojump/libcesarplayer.so*
%attr(755,root,root) %{_libdir}/chronojump/libchronopic.so*
%{_libdir}/chronojump/Chronojump.exe
%{_libdir}/chronojump/Chronojump.exe.mdb
%{_libdir}/chronojump/Chronojump_Mini.exe
%{_libdir}/chronojump/Chronojump_Mini.exe.mdb
%{_libdir}/chronojump/CesarPlayer.dll
%{_libdir}/chronojump/CesarPlayer.dll.config
%{_libdir}/chronojump/CesarPlayer.dll.mdb
%{_libdir}/chronojump/chronojumpServer.dll
%{_libdir}/chronojump/chronojumpServer.dll.mdb
%{_libdir}/chronojump/python
%{_datadir}/chronojump
%{_desktopdir}/chronojump.desktop
%{_iconsdir}/hicolor/scalable/apps/chronojump_icon.svg
