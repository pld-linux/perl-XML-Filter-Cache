#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-Cache
Summary:	XML::Filter::Cache - a SAX2 recorder/playback mechanism
Summary(pl):	XML::Filter::Cache - mechanizm nagrywania/odtwarzania SAX2
Name:		perl-XML-Filter-Cache
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2590e2a28c5741aa8cd14503e0ea767e
Patch0:		%{name}-weird_test_failure.patch
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

%description -l pl
To jest bardzo prosty modu³ filtra dla zdarzeñ SAX2. Domy¶lnie
buforuje on zdarzenia w du¿ym pliku binarnym na dysku (aktualnie pliki
bufora s± zwykle o wiele wiêksze ni¿ oryginalny XML, ale autor tym siê
zajmie), ale backend przechowywania danych jest wymienny. Do
wykonywania freeze/thaw u¿ywana jest klasa Storable i aktualnie nie
jest zamienna, poniewa¿ po prostu nie ma lepszego narzêdzia do tego
celu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

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
