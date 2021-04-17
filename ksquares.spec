#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ksquares
Version  : 20.12.3
Release  : 27
URL      : https://download.kde.org/stable/release-service/20.12.3/src/ksquares-20.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.3/src/ksquares-20.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.3/src/ksquares-20.12.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: ksquares-bin = %{version}-%{release}
Requires: ksquares-data = %{version}-%{release}
Requires: ksquares-license = %{version}-%{release}
Requires: ksquares-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n ksquares-20.12.3
cd %{_builddir}/ksquares-20.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618692354
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1618692354
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksquares
cp %{_builddir}/ksquares-20.12.3/COPYING %{buildroot}/usr/share/package-licenses/ksquares/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/ksquares-20.12.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/ksquares/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang ksquares

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/package-licenses/ksquares/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/ksquares/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f ksquares.lang
%defattr(-,root,root,-)

