%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Escape
Summary:	String::Escape perl module
Summary(pl):	Modu³ perla String::Escape
Name:		perl-String-Escape
Version:	2002.001
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Escape - Registry of string functions, including backslash
escapes.

%description -l pl
Modu³ perla String::Escape - zestaw funkcji do obróbki ci±gów znaków,
w tym cytowania przy pomocy odwrotnych uko¶ników.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/String/Escape.pm
%{_mandir}/man3/*
