%define api 0

%define libname %mklibname deflate %{api}
%define devname %mklibname -d deflate %{api}

Name:          libdeflate
Version:       1.14
Release:       1
Summary:       Fast implementation of DEFLATE, gzip, and zlib
License:       MIT
URL:           https://github.com/ebiggers/libdeflate
Source0:       https://github.com/ebiggers/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make

%description
libdeflate is a library for fast, whole-buffer DEFLATE-based compression and
decompression, supporting DEFLATE, gzip, and zlib.


%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
C library providing a GtkWidget to display maps.
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for libdeflate.

%package utils
Summary:       Binaries from libdeflate
License:       MIT
Requires:	%{libname} = %{version}-%{release}

%description utils
Binaries from libdeflate.


%prep
%autosetup
sed -r -i 's/-O2 -fomit-frame-pointer -std=c99/-std=c99/' Makefile

%build
%make_build CFLAGS="%optflags -fpic -pie -g" USE_SHARED_LIB=1 LIBDIR=%{_libdir} PREFIX=%{_prefix}

%install
%make_install CFLAGS="%optflags -fpic -pie -g" USE_SHARED_LIB=1 LIBDIR=%{_libdir} PREFIX=%{_prefix}
rm %{buildroot}/%{_libdir}/*.a

%files -n %{libname}
%doc NEWS.md README.md
%license COPYING
%{_libdir}/libdeflate.so.%{api}*

%files -n %{devname}
%{_includedir}/libdeflate.h
%{_libdir}/libdeflate.so
%{_libdir}/pkgconfig/*

%files utils
%{_bindir}/libdeflate-gzip
%{_bindir}/libdeflate-gunzip
