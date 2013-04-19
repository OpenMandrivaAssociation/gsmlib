%define major 1
%define libname %mklibname %name %major

Summary: 	Library and utilities to access GSM mobile phones
Name: 	 	gsmlib
Version: 	1.11
Release: 	5.10
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
# FIXME: gold linker dies with internal error in convert_types, at ../../gold/gold.h:192 on i586
%ifarch %{ix86}
export CC="%{__cc} -fuse-ld=bfd"
%endif
%configure2_5x

%make
										
%install
%makeinstall

%find_lang %name

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.11-5.9mdv2011.0
+ Revision: 664930
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.11-5.8mdv2011.0
+ Revision: 605503
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.11-5.7mdv2010.1
+ Revision: 520116
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.11-5.6mdv2010.0
+ Revision: 425047
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.11-5.5mdv2009.1
+ Revision: 316957
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.11-5.4mdv2009.0
+ Revision: 264618
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.11-0.4mdv2009.0
+ Revision: 210050
- fix build
- added one gcc43 patch by gentoo

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.11-0.3mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 01 2007 Laurent Montel <lmontel@mandriva.com> 1.11-0.3mdv2007.0
+ Revision: 115862
- Rebuild
- Import gsmlib

* Tue Jun 13 2006 Helio Castro <helio@mandriva.com> 1.11-0.2mdk
- Fixed headers ( gcc4 patch )

* Tue Aug 30 2005 Austin Acton <austin@mandriva.org> 1.11-0.1mdk
- go to pre1.11-041028
- tweak the patch for gcc 4

* Wed Jun 09 2004 Austin Acton <austin@mandrake.org> 1.10-2mdk
- configure 2.5
- patch for new gcc (Christiaan Welvaart)

