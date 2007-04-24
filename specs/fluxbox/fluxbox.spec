# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

Summary: Window Manager based on Blackbox
Name: fluxbox
Version: 0.9.15.1
Release: 1
License: MIT
Group: User Interface/Desktops
URL: http://fluxbox.sourceforge.net/

Source0: http://dl.sf.net/fluxbox/fluxbox-%{version}.tar.bz2
Source1: fluxbox-xdg-menu.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, imlib2-devel
%{!?_without_fontconfig:BuildRequires: fontconfig-devel}
%{?_with_modxorg:BuildRequires: libICE-devel, libSM-devel, libX11-devel, libXext-devel, libXft-devel, libXinerama-devel, libXpm-devel, libXrandr-devel, libXrender-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
Requires: python-xdg, artwiz-aleczapka-fonts

%description
Fluxbox is yet another windowmanager for X. It's based on the Blackbox 0.61.1
code. Fluxbox looks like blackbox and handles styles, colors, window placement
and similar thing exactly like blackbox (100% theme/style compatibility). 

%prep
%setup

%{__cat} <<EOF >fluxbox.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Fluxbox
Comment=Very small and fast window manager
Exec=startfluxbox
Terminal=False
TryExec=fluxbox

[Window Manager]
SessionManaged=true
EOF

%build
%configure \
	--x-includes="%{_includedir}" \
%{?_with_modxorg:--x-libraries="%{_libdir}"} \
%{!?_with_modxorg:--x-libraries="%{_prefix}/X11R6/%{_lib}"} \
	--enable-gnome \
	--enable-imlib2 \
	--enable-kde \
	--enable-nls \
	--enable-xft \
	--enable-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 fluxbox.desktop %{buildroot}%{_datadir}/xsessions/fluxbox.desktop
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/fluxbox-xdg-menu

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/*.1*
%{_bindir}/*
%{_datadir}/fluxbox/
%{_datadir}/xsessions/fluxbox.desktop

%changelog
* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 0.9.15.1-1
- Initial package. (using DAR)
