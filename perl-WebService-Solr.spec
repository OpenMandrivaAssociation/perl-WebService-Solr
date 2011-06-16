%define upstream_name    WebService-Solr
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Module to interface with the Solr (Lucene) webservice
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Page)
BuildRequires: perl(Data::Pageset)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl-libwww-perl
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Mock::LWP)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(XML::Generator)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(XML::Easy::Element)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
WebService::Solr is a client library for Apache Lucene's Solr; an
enterprise-grade indexing and searching platform.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


