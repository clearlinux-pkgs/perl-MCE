#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MCE
Version  : 1.884
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-1.884.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-1.884.tar.gz
Summary  : 'Many-Core Engine for Perl providing parallel processing capabilities'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-MCE-license = %{version}-%{release}
Requires: perl-MCE-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## Many-Core Engine for Perl
This document describes MCE version 1.884.
Many-Core Engine (MCE) for Perl helps enable a new level of performance by
maximizing all available cores.

%package dev
Summary: dev components for the perl-MCE package.
Group: Development
Provides: perl-MCE-devel = %{version}-%{release}
Requires: perl-MCE = %{version}-%{release}

%description dev
dev components for the perl-MCE package.


%package license
Summary: license components for the perl-MCE package.
Group: Default

%description license
license components for the perl-MCE package.


%package perl
Summary: perl components for the perl-MCE package.
Group: Default
Requires: perl-MCE = %{version}-%{release}

%description perl
perl components for the perl-MCE package.


%prep
%setup -q -n MCE-1.884
cd %{_builddir}/MCE-1.884

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MCE
cp %{_builddir}/MCE-%{version}/Copying %{buildroot}/usr/share/package-licenses/perl-MCE/10a9a171b383cd4164956b76796943793854989d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MCE.3
/usr/share/man/man3/MCE::Candy.3
/usr/share/man/man3/MCE::Channel.3
/usr/share/man/man3/MCE::Channel::Mutex.3
/usr/share/man/man3/MCE::Channel::MutexFast.3
/usr/share/man/man3/MCE::Channel::Simple.3
/usr/share/man/man3/MCE::Channel::SimpleFast.3
/usr/share/man/man3/MCE::Channel::Threads.3
/usr/share/man/man3/MCE::Channel::ThreadsFast.3
/usr/share/man/man3/MCE::Child.3
/usr/share/man/man3/MCE::Core.3
/usr/share/man/man3/MCE::Core::Input::Generator.3
/usr/share/man/man3/MCE::Core::Input::Handle.3
/usr/share/man/man3/MCE::Core::Input::Iterator.3
/usr/share/man/man3/MCE::Core::Input::Request.3
/usr/share/man/man3/MCE::Core::Input::Sequence.3
/usr/share/man/man3/MCE::Core::Manager.3
/usr/share/man/man3/MCE::Core::Validation.3
/usr/share/man/man3/MCE::Core::Worker.3
/usr/share/man/man3/MCE::Examples.3
/usr/share/man/man3/MCE::Flow.3
/usr/share/man/man3/MCE::Grep.3
/usr/share/man/man3/MCE::Loop.3
/usr/share/man/man3/MCE::Map.3
/usr/share/man/man3/MCE::Mutex.3
/usr/share/man/man3/MCE::Mutex::Channel.3
/usr/share/man/man3/MCE::Mutex::Channel2.3
/usr/share/man/man3/MCE::Mutex::Flock.3
/usr/share/man/man3/MCE::Queue.3
/usr/share/man/man3/MCE::Relay.3
/usr/share/man/man3/MCE::Signal.3
/usr/share/man/man3/MCE::Step.3
/usr/share/man/man3/MCE::Stream.3
/usr/share/man/man3/MCE::Subs.3
/usr/share/man/man3/MCE::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MCE/10a9a171b383cd4164956b76796943793854989d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
