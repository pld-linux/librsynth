Summary:	Package for Klatt-style speech synthesis
Summary(pl):	Pakiet do syntezy mowy metod± Klatta
Name:		librsynth
Version:	2.2.0
Release:	1
License:	Free (?)
Group:		Libraries
Source0:	http://www.ling.uni-potsdam.de/~moocow/projects/spsyn/%{name}-%{version}.tar.gz
Patch0:		%{name}-build.patch
URL:		http://www.ling.uni-potsdam.de/~moocow/projects/spsyn/
BuildRequires:	autoconf
BuildRequires:	gdbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librsynth is an adaptation of Nick Ing-Simmons' "rsynth" package for
Klatt-style speech synthesis.
	
%description -l pl
librsynth to adaptacja pakietu "rsynth" Nicka Ing-Simmonsa s³u¿±cego
do syntezy mowy metod± Klatta.

%package devel
Summary:	librsynth header files
Summary(pl):	Pliki nag³ówkowe librynth
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for librsynth library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki librsynth.

%package static
Summary:	librsynth static library
Summary(pl):	Statyczna biblioteka librsynth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of librsynth library.

%description static -l pl
Statyczna wersja biblioteki librsynth.

%prep
%setup -q
%patch -p1

%build
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes README doc/README.{WWW,linux,rsynth} doc/*.doc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/librsynth.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
