%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Escape
Summary:	String-Escape perl module
Summary(pl):	Modu� perla String-Escape
Name:		perl-String-Escape
Version:	1998.1204
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-Escape - Registry of string functions, including backslash
escapes.

%description -l pl
Modu� perla String-Escape.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/String/Escape.pm
%{_mandir}/man3/*
