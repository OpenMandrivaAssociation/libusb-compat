%define major 0
%define libname %mklibname usb-compat %major
%define devellibname %mklibname -d usb-compat %major
%define sdevellibname %mklibname -s -d usb-compat %major

%define oldlibusb_version 0.1.12-14
%define oldlibusb_api     0.1
%define oldlibusb_major   4

Summary: A library which allows userspace access to USB devices
Name: libusb-compat
Version: 0.1.0
Release: %mkrel 4
Source0: http://downloads.sourceforge.net/libusb/libusb-compat-0.1/libusb-compat-0.1.0/%name-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-
URL: http://libusb.wiki.sourceforge.net/Libusb1.0
BuildRequires: doxygen usb1-devel

%description
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %libname
Summary: %summary
Group:	System/Libraries
Requires: pkgconfig
Obsoletes:  %{mklibname usb %oldlibusb_api %oldlibusb_major} > %version
Provides:  %{mklibname usb %oldlibusb_api %oldlibusb_major} = %version
Provides:  %{mklibname usb %oldlibusb_api %oldlibusb_major} = %oldlibusb_version
Provides:  %{mklibname usb %oldlibusb_api }  = %oldlibusb_version
Provides:  %{mklibname usb} = %oldlibusb_version
%if "%{?_lib}" == "lib64"
Provides:  libusb = %oldlibusb_version
%endif

%description -n %libname
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %devellibname
Summary: Development files for libusb
Group:	Development/C
Requires: %{libname} = %{version}
Obsoletes: %{mklibname usb -d} 
Provides: %{mklibname usb -d}
Provides: libusb-devel = %version, usb-devel = %version, usb-compat-devel
Provides: %{mklibname usb %oldlibusb_api %oldlibusb_major -d} = %oldlibusb_version
Obsoletes: %{mklibname usb %oldlibusb_api -d} < %oldlibusb_version
Provides: %{mklibname usb %oldlibusb_api -d} = %oldlibusb_version
%if "%{?_lib}" == "lib64"
Provides: libusb-devel = %oldlibusb_version
Provides: devel(libusb-0.1(64bit))
%else
Provides: devel(libusb-0.1)
%endif
Requires: pkgconfig

%description -n %devellibname
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb0.

%package -n %sdevellibname
Summary: Static development files for libusb
Group:	Development/C
Requires: %{libname}-devel = %{version}
Provides: usb-static-devel = %version

%description -n %sdevellibname
This package contains static libraries to develop applications that use
libusb0.

%prep
%setup -q

%build
%configure2_5x
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# move libs to /%_lib for UPS shutdown
mkdir -p %{buildroot}/%_lib
pushd %{buildroot}%{_libdir}
mv *.so.* ../../%_lib/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS
/%{_lib}/*.so.*

%files -n %devellibname
%defattr(-,root,root)
%doc examples/*.c
%{_libdir}/pkgconfig/libusb.pc
%{_includedir}/*
%{_libdir}/*.so
%_bindir/*

%files -n %sdevellibname
%defattr(-,root,root)
%{_libdir}/*.a



