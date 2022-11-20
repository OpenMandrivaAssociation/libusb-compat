# libusb-compat is used by sdl2, which is used by various games
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define api 0.1
%define major 4
%define libname	%mklibname usb-compat %{api} %{major}
%define devname	%mklibname -d usb-compat %{api}
%define lib32name	%mklib32name usb-compat %{api} %{major}
%define dev32name	%mklib32name -d usb-compat %{api}
%bcond_without bootstrap

Summary:	A library which allows userspace access to USB devices
Name:		libusb-compat
Version:	0.1.8
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libusb.info/
Source0:	https://github.com/libusb/libusb-compat-0.1/archive/v%{version}/%{name}-%{version}.tar.gz
%if ! %{with bootstrap}
BuildRequires:	doxygen 
%endif
BuildRequires:	pkgconfig(libusb-1.0)
%if %{with compat32}
BuildRequires:	devel(libusb-1.0)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	%{summary} (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
A compatibility layer allowing applications written for libusb-0.1 to work
with libusb-1.0. libusb-compat-0.1 attempts to look, feel, smell and walk
like libusb-0.1.

%package -n %{dev32name}
Summary:	Development files for libusb-0.1 (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb-0.1.
%endif

%prep
%autosetup -p1 -n %{name}-0.1-%{version}
[ -e configure ] || ./bootstrap.sh

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure \
	--libdir=/%{_lib}

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libusb-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/pkgconfig/libusb.pc
%{_prefix}/lib/libusb.so
%endif
