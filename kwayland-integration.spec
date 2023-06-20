#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kwayland-integration
Version  : 5.27.6
Release  : 81
URL      : https://download.kde.org/stable/plasma/5.27.6/kwayland-integration-5.27.6.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.6/kwayland-integration-5.27.6.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.6/kwayland-integration-5.27.6.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kwayland-integration-data = %{version}-%{release}
Requires: kwayland-integration-lib = %{version}-%{release}
Requires: kwayland-integration-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kidletime-dev
BuildRequires : kwayland-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : qtbase-dev
BuildRequires : qtbase-staticdev
BuildRequires : wayland-protocols-dev plasma-wayland-protocols-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kwayland-integration package.
Group: Data

%description data
data components for the kwayland-integration package.


%package lib
Summary: lib components for the kwayland-integration package.
Group: Libraries
Requires: kwayland-integration-data = %{version}-%{release}
Requires: kwayland-integration-license = %{version}-%{release}

%description lib
lib components for the kwayland-integration package.


%package license
Summary: license components for the kwayland-integration package.
Group: Default

%description license
license components for the kwayland-integration package.


%prep
%setup -q -n kwayland-integration-5.27.6
cd %{_builddir}/kwayland-integration-5.27.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687291989
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
export SOURCE_DATE_EPOCH=1687291989
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwayland-integration
cp %{_builddir}/kwayland-integration-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kwayland-integration-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kwayland-integration-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kwayland-integration-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kwayland-integration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kwayland-integration-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kwindowsystem.kwayland.categories

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so
/usr/lib64/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland-integration/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kwayland-integration/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kwayland-integration/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwayland-integration/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kwayland-integration/e458941548e0864907e654fa2e192844ae90fc32
