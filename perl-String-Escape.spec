#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Escape
Summary:	String::Escape - registry of string functions, including backslash escapes
Summary(pl.UTF-8):	String::Escape - zestaw funkcji do obróbki łańcuchów, w tym cytowania przy pomocy odwrotnego ukośnika
Name:		perl-String-Escape
Version:	2002.001
Release:	4
# same as perl (README says Artistic)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	764ff01a8f96632af1742e9637defaf6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The String::Escape Perl module provides a flexible calling interface
to some frequently-performed string conversion functions, including
applying and removing C/Unix-style backslash escapes like \n and \t,
wrapping and removing double-quotes, and truncating to fit within a
desired length.

%description -l pl.UTF-8
Moduł Perla String::Escape udostępnia elastyczny interfejs wywołań
pewnych często używanych funkcji konwersji łańcuchów tekstowych,
uwzględniając funkcje do stosowania i usuwania C/uniksowych cytowań za
pomocą odwrotnego ukośnika, jak \n i \t, dodawanie i usuwanie
cudzysłowów i skracanie, aby zmieścić się w określonej długości.

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
