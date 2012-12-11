%define upstream_name    WebService-Solr
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Module to interface with the Solr (Lucene) webservice
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Page)
BuildRequires:	perl(Data::Pageset)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(HTTP::Headers)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::Mock::LWP)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(XML::Generator)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(XML::Easy::Element)
BuildArch:	noarch

%description
WebService::Solr is a client library for Apache Lucene's Solr; an
enterprise-grade indexing and searching platform.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011
+ Revision: 690332
- update to new version 0.15

* Thu Jun 16 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 685628
- update to new version 0.14

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 674962
- new version

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1
+ Revision: 654382
- update to new version 0.12

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 624957
- Add explicit dependencies
- import perl-WebService-Solr

