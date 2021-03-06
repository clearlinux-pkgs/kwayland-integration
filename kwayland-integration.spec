#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kwayland-integration
Version  : 5.22.1
Release  : 47
URL      : https://download.kde.org/stable/plasma/5.22.1/kwayland-integration-5.22.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.22.1/kwayland-integration-5.22.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.22.1/kwayland-integration-5.22.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kwayland-integration-data = %{version}-%{release}
Requires: kwayland-integration-lib = %{version}-%{release}
Requires: kwayland-integration-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kidletime-dev
BuildRequires : kwayland-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kwayland-integration-5.22.1
cd %{_builddir}/kwayland-integration-5.22.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623811986
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
export SOURCE_DATE_EPOCH=1623811986
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwayland-integration
cp %{_builddir}/kwayland-integration-5.22.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kwayland-integration-5.22.1/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/kwayland-integration-5.22.1/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/kwayland-integration-5.22.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/kwayland-integration-5.22.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland-integration/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kwindowsystem.kwayland.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/kguiaddons/kmodifierkey/kmodifierkey_wayland.so
/usr/lib64/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemKWaylandPlugin.so
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWaylandPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland-integration/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kwayland-integration/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kwayland-integration/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwayland-integration/e458941548e0864907e654fa2e192844ae90fc32
