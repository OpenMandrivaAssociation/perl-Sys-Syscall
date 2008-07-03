%define realname   Sys-Syscall

Name:		perl-%{realname}
Version:    0.22
Release:    %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl module to access system calls that Perl doesn't normally provide access to
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sys/Sys-Syscall-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch: noarch

%description
Use epoll, sendfile, from Perl.

%prep
%setup -q -n Sys-Syscall-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

