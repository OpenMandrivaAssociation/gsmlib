%define major 1
%define libname %mklibname %name %major

Summary: 	Library and utilities to access GSM mobile phones
Name: 	 	gsmlib
Version: 	1.11
Release: 	%mkrel 5.8
License:	GPL
Group:		Communications
URL:		http://www.pxh.de/fs/gsmlib/index.html
Source0:	%{name}-pre1.11-041028.tar.bz2
Patch0:		gsmlib-1.11-gcc41.patch
Patch1:		gsmlib-1.11-gcc43.patch
Patch2:		gsmlib-1.11-include-gcc34-fix.patch
Patch3:		gsmlib-1.11-linkfix.diff
BuildRequires:	gettext
BuildRequires:	bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This distribution contains a library to access GSM mobile phones through GSM
modems. Features include:
    * modification of phonebooks stored in the mobile phone or on the SIM card
    * reading and writing of SMS messages stored in the mobile phone
    * sending and reception of SMS messages 

Additionally, some simple command line programs are provided to use these
functionalities. 

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export LIBS="-lstdc++"

%configure2_5x

%make
										
%install
rm -rf %{buildroot}

%makeinstall

%find_lang %name

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ABOUT-NLS COPYING ChangeLog NEWS TODO
%{_bindir}/gsm*
%{_mandir}/man1/gsm*
%{_mandir}/man7/gsm*
%{_mandir}/man8/gsm*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/%name/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
