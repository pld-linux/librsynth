Summary:	Package for Klatt-style speech synthesis
Summary(pl):	Pakiet do syntezy mowy metod� Klatta
Name:		librsynth
Version:	2.2.0
%define	beep_v	1.0
%define	cmu_v	0.6
Release:	3
License:	Free (?)
Group:		Libraries
Source0:	http://www.ling.uni-potsdam.de/~moocow/projects/spsyn/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.cs.cmu.edu/project/fgdata/dict/cmudict.%{cmu_v}.gz
Source2:	ftp://svr-ftp.eng.cam.ac.uk/pub/comp.speech/dictionaries/beep-%{beep_v}.tar.gz
Patch0:		%{name}-build.patch
URL:		http://www.ling.uni-potsdam.de/~moocow/projects/spsyn/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librsynth is an adaptation of Nick Ing-Simmons' "rsynth" package for
Klatt-style speech synthesis.
	
%description -l pl
librsynth to adaptacja pakietu "rsynth" Nicka Ing-Simmonsa s�u��cego
do syntezy mowy metod� Klatta.

%package devel
Summary:	librsynth header files
Summary(pl):	Pliki nag��wkowe librynth
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for librsynth library.

%description devel -l pl
Pliki nag��wkowe dla biblioteki librsynth.

%package static
Summary:	librsynth static library
Summary(pl):	Statyczna biblioteka librsynth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of librsynth library.

%description static -l pl
Statyczna wersja biblioteki librsynth.

%package dict-beep
Summary:	British English Example Pronounciations dictionary
Summary(pl):	BEEP - przyk�adowy s�ownik wymowy dla brytyjskiej odmiany angielskiego
Version:	%{beep_v}
License:	non-commercial, for research only
Group:		Applications/Dictionaries
Requires:	%{name}

%description dict-beep
British English Example Pronounciations dictionary for librsynth.

%description dict-beep -l pl
BEEP (British English Example Pronounciations) - przyk�adowy s�ownik
wymowy dla brytyjskiej odmiany j�zyka angielskiego do librsynth.

%package dict-cmu
Summary:	Carnegie Mellon Pronouncing Dictionary (American English)
Summary(pl):	S�ownik wymowy Carnegie Mellon (ameryka�ska odmiana angielskiego)
Version:	%{cmu_v}
License:	Free
Group:		Applications/Dictionaries
Requires:	%{name}

%description dict-cmu
Carnegie Mellon Pronouncing Dictionary (American English) for
librsynth.

%description dict-cmu -l pl
S�ownik wymowy Carnegie Mellon (dla ameryka�skiej odmiany j�zyka
angielskiego) do librsynth.

%prep
%setup -q -a2
%patch -p1

gzip -dc %{SOURCE1} > dict/cmudict
mv -f beep/beep-%{beep_v} dict/beep

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--with-aDict=dict/cmudict \
	--with-bDict=dict/beep

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
%dir %{_libdir}/dict

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/librsynth.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files dict-beep
%defattr(644,root,root,755)
%{_libdir}/dict/bDict.db

%files dict-cmu
%defattr(644,root,root,755)
%{_libdir}/dict/aDict.db
