%define major	1
%define	libgsmme	%mklibname gsmme %{major}
%define	libgsmext	%mklibname gsmext %{major}
%define devname 	%mklibname %{name} -d

Summary: 	Library and utilities to access GSM mobile phones
Name: 	 	gsmlib
Version: 	1.11
Release: 	10
License:	GPLv2
Group:		Communications
Url:		http://www.pxh.de/fs/gsmlib/index.html
Source0:	%{name}-pre1.11-041028.tar.bz2
Patch0:		gsmlib-1.11-gcc41.patch
Patch1:		gsmlib-1.11-gcc43.patch
Patch2:		gsmlib-1.11-include-gcc34-fix.patch
Patch3:		gsmlib-1.11-linkfix.diff
BuildRequires:	bison
BuildRequires:	gettext

%description
This distribution contains a library to access GSM mobile phones through GSM
modems. Features include:
    * modification of phonebooks stored in the mobile phone or on the SIM card
    * reading and writing of SMS messages stored in the mobile phone
    * sending and reception of SMS messages 

Additionally, some simple command line programs are provided to use these
functionalities. 

%package -n 	%{libgsmme}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Obsoletes:	%{_lib}gsmlib1 < 1.11-6

%description -n %{libgsmme}
Dynamic libraries from %{name}.

%package -n 	%{libgsmext}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
Conflicts:	%{_lib}gsmlib1 < 1.11-6

%description -n %{libgsmext}
Dynamic libraries from %{name}.

%package -n 	%{devname}
Summary: 	Header files and static libraries from %{name}
Group: 		Development/C
Requires: 	%{libgsmme} >= %{version}
Requires: 	%{libgsmext} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%{_lib}gsmlib1-devel < 1.11-6

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q
%apply_patches

%build
export LIBS="-lstdc++"
# FIXME: gold linker dies with internal error in convert_types, at ../../gold/gold.h:192 on i586
%ifarch %{ix86}
export CC="%{__cc} -fuse-ld=bfd"
export CXX="%{__cxx} -fuse-ld=bfd"
mkdir -p BFD
ln -sf /usr/bin/ld.bfd BFD/ld
export PATH=$PWD/BFD:$PATH
%endif
%configure2_5x \
	--disable-static

%make
										
%install
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%doc README ABOUT-NLS COPYING ChangeLog NEWS TODO
%{_bindir}/gsm*
%{_mandir}/man1/gsm*
%{_mandir}/man7/gsm*
%{_mandir}/man8/gsm*

%files -n %{libgsmme}
%{_libdir}/libgsmme.so.%{major}*

%files -n %{libgsmext}
%{_libdir}/libgsmext.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so

