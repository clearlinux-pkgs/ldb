#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ldb
Version  : 1.5.1
Release  : 5
URL      : https://www.samba.org/ftp/pub/ldb/ldb-1.5.1.tar.gz
Source0  : https://www.samba.org/ftp/pub/ldb/ldb-1.5.1.tar.gz
Summary  : An LDAP-like embedded database
Group    : Development/Tools
License  : X11
Requires: ldb-bin
Requires: ldb-lib
Requires: ldb-license
BuildRequires : lmdb-dev
BuildRequires : openldap-dev
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : tdb-dev
Patch1: 0001_fix_default_install_path.patch
Patch2: 0002_fix_waf_options.patch
Patch3: waf.patch

%description
See http://code.google.com/p/waf/ for more information on waf
You can get a svn copy of the upstream source with:

%package bin
Summary: bin components for the ldb package.
Group: Binaries
Requires: ldb-license

%description bin
bin components for the ldb package.


%package dev
Summary: dev components for the ldb package.
Group: Development
Requires: ldb-lib
Requires: ldb-bin
Provides: ldb-devel

%description dev
dev components for the ldb package.


%package lib
Summary: lib components for the ldb package.
Group: Libraries
Requires: ldb-license

%description lib
lib components for the ldb package.


%package license
Summary: license components for the ldb package.
Group: Default

%description license
license components for the ldb package.


%prep
%setup -q -n ldb-1.5.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535906060
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1535906060
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ldb
cp third_party/popt/COPYING %{buildroot}/usr/share/doc/ldb/third_party_popt_COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/modules/ldb/asq.so
/usr/modules/ldb/ldap.so
/usr/modules/ldb/ldb.so
/usr/modules/ldb/mdb.so
/usr/modules/ldb/paged_results.so
/usr/modules/ldb/paged_searches.so
/usr/modules/ldb/rdn_name.so
/usr/modules/ldb/sample.so
/usr/modules/ldb/server_sort.so
/usr/modules/ldb/skel.so
/usr/modules/ldb/tdb.so

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
/usr/include/*.h
/usr/lib/libldb.so
/usr/lib64/pkgconfig/ldb.pc

%files lib
%defattr(-,root,root,-)
/usr/lib/ldb/libcmocka-ldb.so
/usr/lib/ldb/libldb-cmdline.so
/usr/lib/ldb/libldb-key-value.so
/usr/lib/ldb/libldb-mdb-int.so
/usr/lib/ldb/libldb-tdb-err-map.so
/usr/lib/ldb/libldb-tdb-int.so
/usr/lib/ldb/libpopt-ldb.so
/usr/lib/ldb/libtalloc.so.2
/usr/lib/ldb/libtalloc.so.2.1.14
/usr/lib/ldb/libtevent.so.0
/usr/lib/ldb/libtevent.so.0.9.37
/usr/lib/libldb.so.1
/usr/lib/libldb.so.1.5.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/ldb/third_party_popt_COPYING
