Summary:	Package for Klatt-style speech synthesis
Summary(pl):	Pakiet do syntezy mowy metod± Klatta
Name:		librsynth
Version:	2.2.1
%define	beep_v	1.0
%define	cmu_v	0.6
Release:	3
License:	Free (?)
Group:		Libraries
Source0:	http://www.ling.uni-potsdam.de/~moocow/projects/spsyn/%{name}-%{version}.tar.gz
# Source0-md5:	accfaa3566fd6944e15d1864a36a3391
Source1:	ftp://ftp.cs.cmu.edu/project/fgdata/dict/cmudict.%{cmu_v}.gz
# Source1-md5:	56010b97507d1bd85e3519707b3511cc
Source2:	ftp://svr-ftp.eng.cam.ac.uk/pub/comp.speech/dictionaries/beep-%{beep_v}.tar.gz
# Source2-md5:	9f0f6f7a8c3f0910caa29d69846fec8a
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

%package dict-beep
Summary:	British English Example Pronounciations dictionary
Summary(pl):	BEEP - przyk³adowy s³ownik wymowy dla brytyjskiej odmiany angielskiego
Version:	%{beep_v}
License:	non-commercial, for research only
Group:		Applications/Dictionaries
Requires:	%{name}

%description dict-beep
British English Example Pronounciations dictionary for librsynth.

%description dict-beep -l pl
BEEP (British English Example Pronounciations) - przyk³adowy s³ownik
wymowy dla brytyjskiej odmiany jêzyka angielskiego do librsynth.

%package dict-cmu
Summary:	Carnegie Mellon Pronouncing Dictionary (American English)
Summary(pl):	S³ownik wymowy Carnegie Mellon (amerykañska odmiana angielskiego)
Version:	%{cmu_v}
License:	Free
Group:		Applications/Dictionaries
Requires:	%{name}

%description dict-cmu
Carnegie Mellon Pronouncing Dictionary (American English) for
librsynth.

%description dict-cmu -l pl
S³ownik wymowy Carnegie Mellon (dla amerykañskiej odmiany jêzyka
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
%doc Changes doc/README.{WWW,linux,rsynth} doc/*.doc
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
