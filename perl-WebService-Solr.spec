%define upstream_name    WebService-Solr
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Module to interface with the Solr (Lucene) webservice

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/petdance/webservice-solr
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/WebService-Solr-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
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
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

