#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-Cache
Summary:	XML::Filter::Cache - a SAX2 recorder/playback mechanism
Summary(pl.UTF-8):	XML::Filter::Cache - mechanizm nagrywania/odtwarzania SAX2
Name:		perl-XML-Filter-Cache
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2590e2a28c5741aa8cd14503e0ea767e
Patch0:		%{name}-weird_test_failure.patch
URL:		http://search.cpan.org/dist/XML-Filter-Cache/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-SAX >= 0.08
BuildRequires:	perl-XML-SAX-Writer >= 0.39
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple filter module for SAX2 events. By default it
caches events into a big binary file on disk (the cache files are
generally much larger than the original XML at the moment, but I'll
work on that), but the storage backend is pluggable. It uses Storable
to do the freeze/thaw thing, and at the moment this is not pluggin
replaceable, simply because there's no better tool for the task at
hand.

%description -l pl.UTF-8
To jest bardzo prosty moduł filtra dla zdarzeń SAX2. Domyślnie
buforuje on zdarzenia w dużym pliku binarnym na dysku (aktualnie pliki
bufora są zwykle o wiele większe niż oryginalny XML, ale autor tym się
zajmie), ale backend przechowywania danych jest wymienny. Do
wykonywania freeze/thaw używana jest klasa Storable i aktualnie nie
jest zamienna, ponieważ po prostu nie ma lepszego narzędzia do tego
celu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p0

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
%{perl_vendorlib}/XML/*/*
%{_mandir}/man3/*
