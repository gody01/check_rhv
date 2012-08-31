Name:		nagios-plugins-rhev3
Version:	1.0
Release:	2%{?dist}
Summary:	RHEV monitoring plugin for Nagios/Icinga

Group:		Applications/System
License:	GPLv2+
URL:		https://labs.ovido.at/monitoring
Source0:	check_rhev3-%{version}.tar.gz
BuildRoot:	%{_tmppath}/check_rhev3-%{version}-%{release}-root

Requires:	perl-Crypt-SSLeay
Requires:	perl-libwww-perl
Requires:	perl-XML-Simple

%description
This plugin for Icinga/Nagios is used to monitor a variety of
a RHEV environement including datacenters, clusters, hosts,
vms, vm pools and storage domains.

%prep
%setup -q -n check_rhev3-%{version}

%build
%configure --prefix=%{_libdir}/nagios/plugins \
	   --with-nagios-user=nagios \
	   --with-nagios-group=nagios \
	   --with-pnp-dir=%{_datadir}/nagios/html/pnp4nagios

make all


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS=""

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0755,nagios,nagios)
%{_libdir}/nagios/plugins/check_rhev3
%{_datadir}/nagios/html/pnp4nagios/templates/check_rhev3.php
%doc README INSTALL NEWS ChangeLog COPYING



%changelog
* Fri Aug 31 2012 Rene Koch <r.koch@ovido.at> 1.0-2
- Removed BuildArch: noarch

* Wed Aug 27 2012 Rene Koch <r.koch@ovido.at> 1.0-1
- Initial build.

