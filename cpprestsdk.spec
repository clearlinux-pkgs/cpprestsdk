#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cpprestsdk
Version  : 2.10.13
Release  : 9
URL      : https://github.com/Microsoft/cpprestsdk/archive/v2.10.13.tar.gz
Source0  : https://github.com/Microsoft/cpprestsdk/archive/v2.10.13.tar.gz
Source1  : https://github.com/zaphoyd/websocketpp/archive/0.8.1.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT Zlib
Requires: cpprestsdk-data = %{version}-%{release}
Requires: cpprestsdk-lib = %{version}-%{release}
Requires: cpprestsdk-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-scons
BuildRequires : glibc-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libbrotlidec)
BuildRequires : pkgconfig(libbrotlienc)
BuildRequires : zlib-dev
Patch1: 0001-Add-basic-pkgconfig-file.patch

%description
## Welcome!
The C++ REST SDK is a Microsoft project for cloud-based client-server communication in native code using a modern asynchronous C++ API design. This project aims to help C++ developers connect to and interact with services.

%package data
Summary: data components for the cpprestsdk package.
Group: Data

%description data
data components for the cpprestsdk package.


%package dev
Summary: dev components for the cpprestsdk package.
Group: Development
Requires: cpprestsdk-lib = %{version}-%{release}
Requires: cpprestsdk-data = %{version}-%{release}
Provides: cpprestsdk-devel = %{version}-%{release}
Requires: cpprestsdk = %{version}-%{release}

%description dev
dev components for the cpprestsdk package.


%package lib
Summary: lib components for the cpprestsdk package.
Group: Libraries
Requires: cpprestsdk-data = %{version}-%{release}
Requires: cpprestsdk-license = %{version}-%{release}

%description lib
lib components for the cpprestsdk package.


%package license
Summary: license components for the cpprestsdk package.
Group: Default

%description license
license components for the cpprestsdk package.


%prep
%setup -q -n cpprestsdk-2.10.13
cd ..
%setup -q -T -D -n cpprestsdk-2.10.13 -b 1
mkdir -p Release/libs/websocketpp
cp -r %{_topdir}/BUILD/websocketpp-0.8.1/* %{_topdir}/BUILD/cpprestsdk-2.10.13/Release/libs/websocketpp
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1558715420
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ../Release -DWERROR=0
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1558715420
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cpprestsdk
cp Release/tests/common/UnitTestpp/COPYING %{buildroot}/usr/share/package-licenses/cpprestsdk/Release_tests_common_UnitTestpp_COPYING
cp license.txt %{buildroot}/usr/share/package-licenses/cpprestsdk/license.txt
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
install cpprest.pc %{buildroot}/usr/lib64/pkgconfig/
mkdir -p %{buildroot}/usr/share/cmake/Modules
mv %{buildroot}/usr/lib64/cpprestsdk/* %{buildroot}/usr/share/cmake/Modules/
rmdir %{buildroot}/usr/lib64/cpprestsdk
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/cpprest/astreambuf.h
/usr/include/cpprest/asyncrt_utils.h
/usr/include/cpprest/base_uri.h
/usr/include/cpprest/containerstream.h
/usr/include/cpprest/details/SafeInt3.hpp
/usr/include/cpprest/details/basic_types.h
/usr/include/cpprest/details/cpprest_compat.h
/usr/include/cpprest/details/fileio.h
/usr/include/cpprest/details/http_constants.dat
/usr/include/cpprest/details/http_helpers.h
/usr/include/cpprest/details/http_server.h
/usr/include/cpprest/details/http_server_api.h
/usr/include/cpprest/details/nosal.h
/usr/include/cpprest/details/resource.h
/usr/include/cpprest/details/web_utilities.h
/usr/include/cpprest/filestream.h
/usr/include/cpprest/http_client.h
/usr/include/cpprest/http_compression.h
/usr/include/cpprest/http_headers.h
/usr/include/cpprest/http_listener.h
/usr/include/cpprest/http_msg.h
/usr/include/cpprest/interopstream.h
/usr/include/cpprest/json.h
/usr/include/cpprest/oauth1.h
/usr/include/cpprest/oauth2.h
/usr/include/cpprest/producerconsumerstream.h
/usr/include/cpprest/rawptrstream.h
/usr/include/cpprest/streams.h
/usr/include/cpprest/uri.h
/usr/include/cpprest/uri_builder.h
/usr/include/cpprest/version.h
/usr/include/cpprest/ws_client.h
/usr/include/cpprest/ws_msg.h
/usr/include/pplx/pplx.h
/usr/include/pplx/pplxcancellation_token.h
/usr/include/pplx/pplxconv.h
/usr/include/pplx/pplxinterface.h
/usr/include/pplx/pplxlinux.h
/usr/include/pplx/pplxtasks.h
/usr/include/pplx/pplxwin.h
/usr/include/pplx/threadpool.h
/usr/lib64/libcpprest.so
/usr/lib64/pkgconfig/cpprest.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcpprest.so.2.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cpprestsdk/Release_tests_common_UnitTestpp_COPYING
/usr/share/package-licenses/cpprestsdk/license.txt
