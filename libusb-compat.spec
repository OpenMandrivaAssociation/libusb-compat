
%define api 0.1
%define major 4
%define libname %mklibname usb-compat %api %major
%define devellibname %mklibname -d usb-compat %api
%define sdevellibname %mklibname -s -d usb-compat %api

%define oldlibusb_version 0.1.12-14

Summary:	A library which allows userspace access to USB devices
Name:		libusb-compat
Version:	0.1.4
Release:	4
Source0:	http://downloads.sourceforge.net/libusb/libusb-compat-0.1/libusb-compat-0.1.0/%name-%{version}.tar.bz2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libusb.wiki.sourceforge.net/Libusb1.0
BuildRequires:	doxygen 
BuildRequires:	usb1-devel
Patch1:			libusb-0.1-ansi.patch

%description
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{_lib}usb0.1_4 = %oldlibusb_version
Obsoletes:	%{_lib}usb0.1_4 < %oldlibusb_version
# old provides from libusb0.1_4
Provides:	libusb = %oldlibusb_version
Provides:	libusb0.1 = %oldlibusb_version
# wrong name for a short period in cooker
Obsoletes:	%{_lib}usb-compat0 < 0.1.0-6

%description -n %{libname}
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %{devellibname}
Summary:	Development files for libusb-0.1
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{_lib}usb-devel = %oldlibusb_version
Obsoletes:	%{_lib}usb-devel < %oldlibusb_version
Obsoletes:	%{_lib}usb0.1_4-devel < %oldlibusb_version
# wrong name for a short period in cooker:
Obsoletes:	%{_lib}usb-compat0-devel < 0.1.0-6
Provides:	libusb-devel = %oldlibusb_version
Provides:	libusb0.1-devel = %oldlibusb_version
Provides:	usb-compat-devel = %{version}-%{release}
Provides:	usb0.1-devel = %{version}-%{release}

%description -n %{devellibname}
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb-0.1.

%package -n %{sdevellibname}
Summary:	Static development files for libusb-0.1
Group:		Development/C
Requires:	%{devellibname} = %{version}
Provides:	libusb-static-devel = %oldlibusb_version
Provides:	libusb0.1-static-devel = %oldlibusb_version
Obsoletes:	%{_lib}usb-static-devel < %oldlibusb_version
Obsoletes:	%{_lib}usb1.0_4-static-devel < %oldlibusb_version
# wrong name for a short period in cooker:
Obsoletes:	%{_lib}usb-compat0-static-devel < 0.1.0-6

%description -n %{sdevellibname}
This package contains static libraries to develop applications that use
libusb0.

%prep
%setup -q
%patch1 -p1

%build
%configure2_5x \
	--libdir=/%_lib

%make

%install
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/libusb-config

# static library is not needed in /lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/libusb.a %{buildroot}%{_libdir}
# add a symlink just in case libtool expects it to be there due to it
# being referenced in the .la file
ln -s %{_libdir}/libusb.a %{buildroot}/%{_lib}/libusb.a
# move pkgconfig
mv %buildroot/%_lib/pkgconfig %buildroot/%_libdir/

%files -n %{libname}
/%{_lib}/libusb-%{api}.so.%{major}*

%files -n %{devellibname}
%doc AUTHORS COPYING README NEWS
%doc examples/*.c
%{_libdir}/pkgconfig/libusb.pc
%{_includedir}/usb.h
/%_lib/libusb.so
%{multiarch_bindir}/libusb-config
%_bindir/libusb-config

%files -n %{sdevellibname}
/%_lib/libusb.a
%{_libdir}/libusb.a



