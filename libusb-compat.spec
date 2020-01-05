%define api 0.1
%define major 4
%define libname	%mklibname usb-compat %{api} %{major}
%define devname	%mklibname -d usb-compat %{api}
%bcond_without bootstrap

Summary:	A library which allows userspace access to USB devices
Name:		libusb-compat
Version:	0.1.5
Release:	19
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libusb.wiki.sourceforge.net/Libusb1.0
Source0:	http://downloads.sourceforge.net/libusb/libusb-compat-0.1/libusb-compat-0.1.0/%{name}-%{version}.tar.bz2
Patch1:		libusb-0.1-ansi.patch
%if ! %{with bootstrap}
BuildRequires:	doxygen 
%endif
BuildRequires:	pkgconfig(libusb-1.0)

%description
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %{devname}
Summary:	Development files for libusb-0.1
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	usb-compat-devel = %{version}-%{release}

%description -n %{devname}
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb-0.1.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--libdir=/%{_lib}

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/pkgconfig %{buildroot}/%{_libdir}/

%files -n %{libname}
/%{_lib}/libusb-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING README NEWS
%doc examples/*.c
%{_bindir}/libusb-config
%{_includedir}/usb.h
%{_libdir}/pkgconfig/libusb.pc
/%{_lib}/libusb.so
