Summary:	Destructive device IO testing program
Summary(pl.UTF-8):   Wielowątkowy, destruktywny tester I/O
Name:		verify-data
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://people.redhat.com/sct/src/verify-data/%{name}-%{version}.tar.bz2
# Source0-md5:	a159aeea19b056c96b63e9254df4d0d1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, destructive device IO testing program, designed to test
block device data integrity throughout the range of a large device.

%description -l pl.UTF-8
Prosty, destruktywny program do testowania urządzeń I/O zaprojektowany
do testowania integralności danych na urządzeniach blokowych na całym
zakresie dużego urządzenia.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install verify-data $RPM_BUILD_ROOT%{_bindir}
install verify-data.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
