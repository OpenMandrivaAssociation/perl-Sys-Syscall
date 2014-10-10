%define upstream_name    Sys-Syscall
%define upstream_version 0.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.25
Release:	2

Summary:	Perl module to access system calls that Perl doesn't normally provide access to
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Sys/Sys-Syscall-0.25.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Use epoll, sendfile, from Perl.

%prep
%setup -q -n Sys-Syscall-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.230.0-2mdv2011.0
+ Revision: 655219
- rebuild for updated spec-helper

* Mon Apr 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 536732
- update to 0.23

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 406183
- rebuild using %%perl_convert_version

* Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 0.22-3mdv2009.0
+ Revision: 230901
- rebuild
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 22 2007 Michael Scherer <misc@mandriva.org> 0.22-1mdv2008.0
+ Revision: 16869
- upadte to 0.22


* Tue May 02 2006 Michael Scherer <misc@mandriva.org> 0.21-1mdk
- New release 0.21

* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 0.20-1mdk
- First Mandriva package


