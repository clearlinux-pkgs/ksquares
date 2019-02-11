#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ksquares
Version  : 18.12.2
Release  : 3
URL      : https://download.kde.org/stable/applications/18.12.2/src/ksquares-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/ksquares-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/ksquares-18.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: ksquares-bin = %{version}-%{release}
Requires: ksquares-data = %{version}-%{release}
Requires: ksquares-license = %{version}-%{release}
Requires: ksquares-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n ksquares-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549891349
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549891349
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksquares
cp COPYING %{buildroot}/usr/share/package-licenses/ksquares/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/ksquares/COPYING.DOC
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
/usr/share/package-licenses/ksquares/COPYING
/usr/share/package-licenses/ksquares/COPYING.DOC

%files locales -f ksquares.lang
%defattr(-,root,root,-)

