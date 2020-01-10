%define SYSINFO_DISTRO fedora

Name:           kio_sysinfo
Version:        20090930
Release:        6%{?dist}
Summary:        KIO slave which shows basic system information

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.kde.org/
Source0:        http://ktown.kde.org/~lukas/kio_sysinfo/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  kdelibs-devel >= 4
BuildRequires:  kde-filesystem >= 4
BuildRequires:  cmake
BuildRequires:  dbus-devel giflib-devel pcre-devel
BuildRequires:  gettext

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description
This is a sysinfo:/ KIO slave, which shows basic system information often 
requested by users.


%prep
%setup -q

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} -DSYSINFO_DISTRO:STRING=%{SYSINFO_DISTRO} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
mkdir %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kio_sysinfo

%clean
rm -rf %{buildroot}


%files -f kio_sysinfo.lang
%defattr(-,root,root,-)
%doc README COPYING
%{_kde4_libdir}/kde4/kio_sysinfo.so
%{_kde4_libdir}/kde4/libksysinfopart.so
%{_kde4_datadir}/applications/kde4/kfmclient_sysinfo.desktop
%{_kde4_datadir}/kde4/apps/sysinfo/
%{_kde4_datadir}/kde4/services/ksysinfopart.desktop
%{_kde4_datadir}/kde4/services/sysinfo.protocol
%{_kde4_datadir}/mime/packages/x-sysinfo.xml


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090930-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090930-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090930-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090930-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Ville Skyttä <ville.skytta@iki.fi> - 20090930-2
- Own the /usr/share/kde4/apps/sysinfo dir.

* Wed Sep 30 2009 Lukáš Tinkl <ltinkl@redhat.com> - 20090930-1
- fix mounting devices using Solid, HTML template fixes

* Fri Aug 28 2009 Lukáš Tinkl <ltinkl@redhat.com> - 20090828-1
- new upstream version with a couple of small fixes
  (most notably the empty disk Label fix)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090620-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Lukáš Tinkl <ltinkl@redhat.com> - 20090620-1
- new upstream version
- drop patches
- added battery status
- updated translations

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090216-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Jaroslav Reznik <jreznik@redhat.com> 20090216-2
- gettext requires
- conversion patch

* Mon Feb 16 2009 Jaroslav Reznik <jreznik@redhat.com> 20090216-1
- owns about directory
- new version

* Wed Nov 21 2008 Jaroslav Reznik <jreznik@redhat.com> 20081121-1
- initial package
- use SYSINFO_DISTRO
