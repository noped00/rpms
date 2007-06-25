# $Id$
# Authority: dag

Summary: Tasks to-do list
Name: tasks
Version: 0.8
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://pimlico-project.org/tasks.html

Source: http://pimlico-project.org/sources/tasks/tasks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, intltool, libsexy-devel, gtk2-devel
BuildRequires: evolution-data-server-devel >= 1.2.0
BuildRequires: desktop-file-utils

%description
Tasks is a simple To Do list application that eschews complicated features
for a lean interface and functionality that just does the right thing.

It has a simple interface with little cruft around the list of tasks, is
ported to the OpenMoko framework, and there are plans for focused ports to
other frameworks (such as Maemo as used on the Nokia N800).

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -p"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
touch %{_datadir}/icons/hicolor
/usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch %{_datadir}/icons/hicolor
/usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/tasks
%{_datadir}/applications/tasks.desktop
%{_datadir}/icons/hicolor/*/apps/tasks.png
%{_datadir}/icons/hicolor/*/apps/tasks.svg
%{_datadir}/tasks/

%changelog
* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
