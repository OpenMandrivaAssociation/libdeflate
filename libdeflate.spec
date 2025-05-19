%global optflags %{optflags} -O3

%define api 0

%define libname %mklibname deflate %{api}
%define devname %mklibname -d deflate %{api}

Summary:	Fast implementation of DEFLATE, gzip, and zlib
Name:		libdeflate
Version:	1.24
Release:	1
License:	MIT
Group:		System/Libraries
URL:		https://github.com/ebiggers/libdeflate
Source0:	https://github.com/ebiggers/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	ninja
BuildRequires:	cmake

%description
libdeflate is a library for fast, whole-buffer DEFLATE-based compression and
decompression, supporting DEFLATE, gzip, and zlib.


%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
C library providing a GtkWidget to display maps.
This package contains the shared library files.

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for libdeflate.

%package utils
Summary:	Binaries from libdeflate
Group:		Archiving/Compression
Requires:	%{libname} = %{EVRD}

%description utils
Binaries from libdeflate.

%prep
%autosetup -p1

%build
%cmake \
	-DLIBDEFLATE_BUILD_STATIC_LIB=OFF \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

%files -n %{libname}
%doc NEWS.md README.md
%license COPYING
%{_libdir}/libdeflate.so.%{api}*

%files -n %{devname}
%{_includedir}/libdeflate.h
%{_libdir}/libdeflate.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/libdeflate/

%files utils
%{_bindir}/libdeflate-gzip
%{_bindir}/libdeflate-gunzip
