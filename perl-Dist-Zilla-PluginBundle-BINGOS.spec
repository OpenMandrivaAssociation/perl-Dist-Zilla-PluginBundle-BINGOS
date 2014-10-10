%define upstream_name    Dist-Zilla-PluginBundle-BINGOS
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	BeLike::BINGOS when you build your dists
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Plugin::ChangelogFromGit)
BuildRequires:	perl(Dist::Zilla::Plugin::GithubMeta)
BuildRequires:	perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:	perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires:	perl(Moose)
BuildArch:	noarch

%description
This is a the Dist::Zilla manpage PluginBundle. It is roughly equivalent to
the following dist.ini:

  [@Basic]

  [MetaJSON]
  [PodSyntaxTests]
  [PodCoverageTests]

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
%doc META.yml LICENSE README META.json Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

