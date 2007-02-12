Summary:	Minimal XML library
Summary(pl.UTF-8):   Minimalna biblioteka XML
Name:		libmxml
Version:	0.9.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mxml/%{name}-%{version}.tar.gz
# Source0-md5:	1e166b6cec4b0843eeaf19b86a23d9d1
URL:		http://mxml.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal XML is a library meant for extrememly fast and non-validating
xml parsing.

%description -l pl.UTF-8
Minimal XML jest biblioteką z przeznaczeniem do ekstremalnie szybkiego
i niewalidującego parsowania xml.

%package devel
Summary:	Header files for libmxml
Summary(pl.UTF-8):   Pliki nagłówkowe dla libmxml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmxml.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libmxml.

%package static
Summary:	Static libmxml library
Summary(pl.UTF-8):   Statyczna biblioteka libmxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmxml library.

%description static -l pl.UTF-8
Statyczna biblioteka libmxml.

%prep
%setup -q

%build
sed -i -e "s:\"-O2\":\$OPTFLAGS:" configure.in

%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-docs \
	--enable-shared

%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libmxml.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
