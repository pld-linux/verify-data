Summary:	Destructive device IO testing program
Summary(pl):	Wielow±tkowy tester I/O
Name:		verify-data
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://people.redhat.com/sct/src/verify-data/%{name}-%{version}.tar.bz2
# Source0-md5:	bf485bf820e693c79e6bd2a38702a128
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, destructive device IO testing program, designed to test
block device data integrity throughout the range of a large device.

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
