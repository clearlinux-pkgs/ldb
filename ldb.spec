#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ldb
Version  : 2.4.1
Release  : 82
URL      : https://www.samba.org/ftp/pub/ldb/ldb-2.4.1.tar.gz
Source0  : https://www.samba.org/ftp/pub/ldb/ldb-2.4.1.tar.gz
Summary  : An LDAP-like embedded database
Group    : Development/Tools
License  : X11
Requires: ldb-bin = %{version}-%{release}
Requires: ldb-lib = %{version}-%{release}
Requires: ldb-license = %{version}-%{release}
Requires: ldb-python = %{version}-%{release}
Requires: ldb-python3 = %{version}-%{release}
BuildRequires : cmocka-dev
BuildRequires : libtirpc-dev
BuildRequires : lmdb-dev
BuildRequires : openldap-dev
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : talloc-dev
BuildRequires : talloc-extras
BuildRequires : tdb-dev
BuildRequires : tdb-python3
BuildRequires : tevent-dev
BuildRequires : tevent-python3
Patch1: 0001-add-mock-disable-static-option.patch

%description
See http://code.google.com/p/waf/ for more information on waf
You can get a svn copy of the upstream source with:

%package bin
Summary: bin components for the ldb package.
Group: Binaries
Requires: ldb-license = %{version}-%{release}

%description bin
bin components for the ldb package.


%package dev
Summary: dev components for the ldb package.
Group: Development
Requires: ldb-lib = %{version}-%{release}
Requires: ldb-bin = %{version}-%{release}
Provides: ldb-devel = %{version}-%{release}
Requires: ldb = %{version}-%{release}

%description dev
dev components for the ldb package.


%package extras
Summary: extras components for the ldb package.
Group: Default

%description extras
extras components for the ldb package.


%package lib
Summary: lib components for the ldb package.
Group: Libraries
Requires: ldb-license = %{version}-%{release}

%description lib
lib components for the ldb package.


%package license
Summary: license components for the ldb package.
Group: Default

%description license
license components for the ldb package.


%package python
Summary: python components for the ldb package.
Group: Default
Requires: ldb-python3 = %{version}-%{release}

%description python
python components for the ldb package.


%package python3
Summary: python3 components for the ldb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ldb package.


%prep
%setup -q -n ldb-2.4.1
cd %{_builddir}/ldb-2.4.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637097923
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-modulesdir=/usr/lib64/ldb/modules \
--disable-rpath \
--disable-rpath-install
make  %{?_smp_mflags}  LDB_MODULESDIR=/usr/lib64/ldb/modules

%install
export SOURCE_DATE_EPOCH=1637097923
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ldb
cp %{_builddir}/ldb-2.4.1/third_party/popt/COPYING %{buildroot}/usr/share/package-licenses/ldb/61bb7a8ea669080cfc9e7dbf37079eae70b535fb
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/tdbbackup
rm -f %{buildroot}*/usr/bin/tdbdump
rm -f %{buildroot}*/usr/bin/tdbrestore
rm -f %{buildroot}*/usr/bin/tdbtool
rm -f %{buildroot}*/usr/lib64/ldb/libpytalloc-util.cpython-3*-x86-64-linux-gnu.so.2
rm -f %{buildroot}*/usr/lib64/ldb/libpytalloc-util.cpython-3*-x86-64-linux-gnu.so.2.2.0
rm -f %{buildroot}*/usr/lib64/ldb/modules/ldb/ldb.so
rm -f %{buildroot}*/usr/lib/python3*/site-packages/talloc.cpython-3*-x86_64-linux-gnu.so
rm -f %{buildroot}*/usr/lib/python3*/site-packages/__pycache__/tevent.cpython-3*.pyc
rm -f %{buildroot}*/usr/lib/python3*/site-packages/_tevent.cpython-3*-x86_64-linux-gnu.so
rm -f %{buildroot}*/usr/lib/python3*/site-packages/tevent.py

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ldbadd
/usr/bin/ldbdel
/usr/bin/ldbedit
/usr/bin/ldbmodify
/usr/bin/ldbrename
/usr/bin/ldbsearch

%files dev
%defattr(-,root,root,-)
/usr/include/ldb.h
/usr/include/ldb_errors.h
/usr/include/ldb_handlers.h
/usr/include/ldb_module.h
/usr/include/ldb_version.h
/usr/include/pyldb.h
/usr/lib64/libldb.so
/usr/lib64/pkgconfig/ldb.pc
/usr/lib64/pkgconfig/pyldb-util.cpython-310-x86_64-linux-gnu.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/libpyldb-util.cpython-310-x86-64-linux-gnu.so
/usr/lib64/libpyldb-util.cpython-310-x86-64-linux-gnu.so.2

%files lib
%defattr(-,root,root,-)
/usr/lib64/ldb/libldb-cmdline.so
/usr/lib64/ldb/libldb-key-value.so
/usr/lib64/ldb/libldb-mdb-int.so
/usr/lib64/ldb/libldb-tdb-err-map.so
/usr/lib64/ldb/libldb-tdb-int.so
/usr/lib64/ldb/modules/ldb/asq.so
/usr/lib64/ldb/modules/ldb/ldap.so
/usr/lib64/ldb/modules/ldb/mdb.so
/usr/lib64/ldb/modules/ldb/paged_searches.so
/usr/lib64/ldb/modules/ldb/rdn_name.so
/usr/lib64/ldb/modules/ldb/sample.so
/usr/lib64/ldb/modules/ldb/server_sort.so
/usr/lib64/ldb/modules/ldb/skel.so
/usr/lib64/ldb/modules/ldb/tdb.so
/usr/lib64/libldb.so.2
/usr/lib64/libldb.so.2.4.1
/usr/lib64/libpyldb-util.cpython-310-x86-64-linux-gnu.so.2.4.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ldb/61bb7a8ea669080cfc9e7dbf37079eae70b535fb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
