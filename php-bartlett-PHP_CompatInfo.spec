%define		pearname	PHP_CompatInfo
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Find out the minimum version and the extensions required for a piece of code to run
Name:		php-bartlett-PHP_CompatInfo
Version:	2.26.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://bartlett.laurent-laville.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	ca6f0922e26119157efb891cd51d6c66
URL:		http://bartlett.laurent-laville.org/package/PHP_CompatInfo/
BuildRequires:	php-channel(bartlett.laurent-laville.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(reflection)
Requires:	php(spl)
Requires:	php-bartlett-PHP_Reflect <= 1.99.0
Requires:	php-channel(bartlett.laurent-laville.org)
Requires:	php-libxml
Requires:	php-pear
Requires:	php-pear-Console_CommandLine >= 1.2.0
Suggests:	php-pear-Net_Growl
Suggests:	php-phpunit-PHPUnit
Suggests:	php-phpunit-PHP_Timer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%(pear config-get cfg_dir 2>/dev/null || ERROR)/%{pearname}

# exclude optional dependencies
%define		_noautoreq_pear Net/Growl.* PHPUnit.* PHP/Timer.*

%description
PHP_CompatInfo will parse a file/folder/array to find out the minimum
version and extensions required for it to run. CLI version has many
reports (extension, interface, class, function, constant) to display
and ability to show content of dictionary references.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/PHP_CompatInfo/*
%{php_pear_dir}/.registry/.channel.*/*.reg
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pear/PHP_CompatInfo/phpcompatinfo.xml.dist
#%attr(755,root,root) %{_bindir}/phpcompatinfo
%{php_pear_dir}/Bartlett/PHP/CompatInfo.php
%{php_pear_dir}/Bartlett/PHP/CompatInfo
%{php_pear_dir}/data/PHP_CompatInfo
