#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Escape
Summary:	String::Escape - registry of string functions, including backslash escapes
Summary(pl):	String::Escape - zestaw funkcji do obróbki ³añcuchów, w tym cytowania przy pomocy odwrotnego uko¶nika
Name:		perl-String-Escape
Version:	2002.001
Release:	3
# same as perl (README says Artistic)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	764ff01a8f96632af1742e9637defaf6
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Escape Perl module provides a flexible calling interface
to some frequently-performed string conversion functions, including
applying and removing C/Unix-style backslash escapes like \n and \t,
wrapping and removing double-quotes, and truncating to fit within a
desired length.

%description -l pl
Modu³ Perla String::Escape udostêpnia elastyczny interfejs wywo³añ
pewnych czêsto u¿ywanych funkcji konwersji ³añcuchów tekstowych,
uwzglêdniaj±c funkcje do stosowania i usuwania C/uniksowych cytowañ za
pomoc± odwrotnego uko¶nika, jak \n i \t, dodawanie i usuwanie
cudzys³owów i skracanie, aby zmie¶ciæ siê w okre¶lonej d³ugo¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/String/Escape.pm
%{_mandir}/man3/*
