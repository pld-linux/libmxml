# NOTE:
# - for C++ continuation of _this_ libmxml, see libmxmlplus.spec
# - for another libmxml (mxml pkgconfig package), see mxml.spec
Summary:	Minimal XML library
Summary(pl.UTF-8):	Minimalna biblioteka XML
Name:		libmxml
Version:	0.9.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/mxml/%{name}-%{version}.tar.gz
# Source0-md5:	1e166b6cec4b0843eeaf19b86a23d9d1
Patch0:		%{name}-ac.patch
URL:		http://mxml.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal XML is a library meant for extrememly fast and non-validating
XML parsing.

%description -l pl.UTF-8
Minimal XML jest biblioteką z przeznaczeniem do ekstremalnie szybkiej
analizy XML bez kontroli poprawności.

%package devel
Summary:	Header files for libmxml
Summary(pl.UTF-8):	Pliki nagłówkowe dla libmxml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmxml.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libmxml.

%package static
Summary:	Static libmxml library
Summary(pl.UTF-8):	Statyczna biblioteka libmxml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmxml library.

%description static -l pl.UTF-8
Statyczna biblioteka libmxml.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_libdir}/libmxml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmxml.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmxml.so
%{_libdir}/libmxml.la
%{_includedir}/mxml.h
%{_includedir}/mxml_defs.h
%{_includedir}/mxml_file.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmxml.a
