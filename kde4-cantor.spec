%define		_state		stable
%define		orgname		cantor

Summary:	K Desktop Environment - Frontend to Mathematical Software
Name:		cantor
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	910a2e814df1a61d77f0be06c6a9f1ab
URL:		http://www.kde.org/
BuildRequires:	R
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libspectre-devel
Obsoletes:	kde4-kdeedu-cantor < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
a front-end to powerful mathematics and statistics packages. Cantor
integrates them into the KDE Platform and provides a nice,
worksheet-based, graphical user interface.

%package devel
Summary:	cantor development files
Summary(pl.UTF-8):	Pliki dla programistów cantor
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
cantor development files.

%description devel -l pl.UTF-8
Pliki dla programistów cantor.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cantor
%attr(755,root,root) %{_bindir}/cantor_rserver
%attr(755,root,root) %{_libdir}/kde4/cantor_creatematrixassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_differentiateassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_eigenvaluesassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_eigenvectorsassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_integrateassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_invertmatrixassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_maximabackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_nullbackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_plot2dassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_plot3dassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_rbackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_runscriptassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_sagebackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_solveassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_advancedplotassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_helppanelplugin.so
%attr(755,root,root) %{_libdir}/kde4/cantor_octavebackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_variablemanagerplugin.so
%attr(755,root,root) %{_libdir}/kde4/libcantorpart.so
%attr(755,root,root) %{_libdir}/libcantorlibs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcantorlibs.so.?
%attr(755,root,root) %{_libdir}/libcantor_config.so
%{_desktopdir}/kde4/cantor.desktop
%{_datadir}/apps/cantor
%{_datadir}/config.kcfg/cantor.kcfg
%{_datadir}/config.kcfg/cantor_libs.kcfg
%{_datadir}/config.kcfg/maximabackend.kcfg
%{_datadir}/config.kcfg/sagebackend.kcfg
%{_datadir}/config.kcfg/rserver.kcfg
%{_datadir}/config/cantor*.knsrc
%{_iconsdir}/hicolor/16x16/apps/cantor.png
%{_iconsdir}/hicolor/32x32/apps/cantor.png
%{_iconsdir}/hicolor/48x48/apps/cantor.png
%{_iconsdir}/hicolor/48x48/apps/maximabackend.png
%{_iconsdir}/hicolor/48x48/apps/rbackend.png
%{_iconsdir}/hicolor/48x48/apps/sagebackend.png
%{_iconsdir}/hicolor/*x*/apps/octavebackend.png
%dir %{_datadir}/kde4/services/cantor
%{_datadir}/kde4/services/cantor/cantor_part.desktop
%{_datadir}/kde4/services/cantor/creatematrixassistant.desktop
%{_datadir}/kde4/services/cantor/differentiateassistant.desktop
%{_datadir}/kde4/services/cantor/eigenvaluesassistant.desktop
%{_datadir}/kde4/services/cantor/eigenvectorsassistant.desktop
%{_datadir}/kde4/services/cantor/integrateassistant.desktop
%{_datadir}/kde4/services/cantor/invertmatrixassistant.desktop
%{_datadir}/kde4/services/cantor/maximabackend.desktop
%{_datadir}/kde4/services/cantor/nullbackend.desktop
%{_datadir}/kde4/services/cantor/plot2dassistant.desktop
%{_datadir}/kde4/services/cantor/plot3dassistant.desktop
%{_datadir}/kde4/services/cantor/rbackend.desktop
%{_datadir}/kde4/services/cantor/runscriptassistant.desktop
%{_datadir}/kde4/services/cantor/sagebackend.desktop
%{_datadir}/kde4/services/cantor/solveassistant.desktop
%{_datadir}/kde4/servicetypes/cantor_assistant.desktop
%{_datadir}/kde4/servicetypes/cantor_backend.desktop
%{_datadir}/kde4/services/cantor/advancedplotassistant.desktop
%{_datadir}/kde4/services/cantor/helppanelplugin.desktop
%{_datadir}/kde4/services/cantor/octavebackend.desktop
%{_datadir}/kde4/services/cantor/variablemanagerplugin.desktop
%{_datadir}/kde4/servicetypes/cantor_panelplugin.desktop
%{_datadir}/config.kcfg/octavebackend.kcfg

%files devel
%defattr(644,root,root,755)
%{_includedir}/cantor
%attr(755,root,root) %{_libdir}/libcantorlibs.so
