#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksquares
Version  : 23.04.1
Release  : 53
URL      : https://download.kde.org/stable/release-service/23.04.1/src/ksquares-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/ksquares-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/ksquares-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: ksquares-bin = %{version}-%{release}
Requires: ksquares-data = %{version}-%{release}
Requires: ksquares-license = %{version}-%{release}
Requires: ksquares-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KSquares is an implementation of the game squares (http://en.wikipedia.org/wiki/Dots_and_Boxes)

%package bin
Summary: bin components for the ksquares package.
Group: Binaries
Requires: ksquares-data = %{version}-%{release}
Requires: ksquares-license = %{version}-%{release}

%description bin
bin components for the ksquares package.


%package data
Summary: data components for the ksquares package.
Group: Data

%description data
data components for the ksquares package.


%package doc
Summary: doc components for the ksquares package.
Group: Documentation

%description doc
doc components for the ksquares package.


%package license
Summary: license components for the ksquares package.
Group: Default

%description license
license components for the ksquares package.


%package locales
Summary: locales components for the ksquares package.
Group: Default

%description locales
locales components for the ksquares package.


%prep
%setup -q -n ksquares-23.04.1
cd %{_builddir}/ksquares-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685598511
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685598511
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksquares
cp %{_builddir}/ksquares-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ksquares/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/ksquares-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ksquares/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ksquares-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ksquares/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/ksquares-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/ksquares/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/ksquares-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksquares/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang ksquares
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/ksquares
/usr/bin/ksquares

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.ksquares.desktop
/usr/share/config.kcfg/ksquares.kcfg
/usr/share/icons/hicolor/128x128/apps/ksquares.png
/usr/share/icons/hicolor/16x16/apps/ksquares.png
/usr/share/icons/hicolor/22x22/apps/ksquares.png
/usr/share/icons/hicolor/32x32/apps/ksquares.png
/usr/share/icons/hicolor/48x48/apps/ksquares.png
/usr/share/icons/hicolor/64x64/apps/ksquares.png
/usr/share/metainfo/org.kde.ksquares.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/ksquares/configure-display.png
/usr/share/doc/HTML/ca/ksquares/gameboard.png
/usr/share/doc/HTML/ca/ksquares/index.cache.bz2
/usr/share/doc/HTML/ca/ksquares/index.docbook
/usr/share/doc/HTML/ca/ksquares/newgame.png
/usr/share/doc/HTML/de/ksquares/index.cache.bz2
/usr/share/doc/HTML/de/ksquares/index.docbook
/usr/share/doc/HTML/en/ksquares/configure-display.png
/usr/share/doc/HTML/en/ksquares/gameboard.png
/usr/share/doc/HTML/en/ksquares/index.cache.bz2
/usr/share/doc/HTML/en/ksquares/index.docbook
/usr/share/doc/HTML/en/ksquares/newgame.png
/usr/share/doc/HTML/es/ksquares/index.cache.bz2
/usr/share/doc/HTML/es/ksquares/index.docbook
/usr/share/doc/HTML/et/ksquares/index.cache.bz2
/usr/share/doc/HTML/et/ksquares/index.docbook
/usr/share/doc/HTML/fr/ksquares/index.cache.bz2
/usr/share/doc/HTML/fr/ksquares/index.docbook
/usr/share/doc/HTML/it/ksquares/index.cache.bz2
/usr/share/doc/HTML/it/ksquares/index.docbook
/usr/share/doc/HTML/ja/ksquares/index.cache.bz2
/usr/share/doc/HTML/ja/ksquares/index.docbook
/usr/share/doc/HTML/nl/ksquares/index.cache.bz2
/usr/share/doc/HTML/nl/ksquares/index.docbook
/usr/share/doc/HTML/pt/ksquares/index.cache.bz2
/usr/share/doc/HTML/pt/ksquares/index.docbook
/usr/share/doc/HTML/pt_BR/ksquares/index.cache.bz2
/usr/share/doc/HTML/pt_BR/ksquares/index.docbook
/usr/share/doc/HTML/sv/ksquares/index.cache.bz2
/usr/share/doc/HTML/sv/ksquares/index.docbook
/usr/share/doc/HTML/uk/ksquares/configure-display.png
/usr/share/doc/HTML/uk/ksquares/gameboard.png
/usr/share/doc/HTML/uk/ksquares/index.cache.bz2
/usr/share/doc/HTML/uk/ksquares/index.docbook
/usr/share/doc/HTML/uk/ksquares/newgame.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksquares/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ksquares/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/ksquares/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/ksquares/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/ksquares/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f ksquares.lang
%defattr(-,root,root,-)

