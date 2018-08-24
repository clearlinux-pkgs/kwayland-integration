#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kwayland-integration
Version  : 5.13.4
Release  : 1
URL      : https://download.kde.org/stable/plasma/5.13.4/kwayland-integration-5.13.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.13.4/kwayland-integration-5.13.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kwayland-integration-lib
Requires: kwayland-integration-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kidletime-dev
BuildRequires : kwayland-dev
BuildRequires : kwindowsystem-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
No detailed description available

%package lib
Summary: lib components for the kwayland-integration package.
Group: Libraries
Requires: kwayland-integration-license

%description lib
lib components for the kwayland-integration package.


%package license
Summary: license components for the kwayland-integration package.
Group: Default

%description license
license components for the kwayland-integration package.


%prep
%setup -q -n kwayland-integration-5.13.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535149074
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535149074
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kwayland-integration
cp COPYING.LIB %{buildroot}/usr/share/doc/kwayland-integration/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWaylandPlugin.so
/usr/lib64/qt5/plugins/kf5/org.kde.kwindowsystem.platforms/KF5WindowSystemKWaylandPlugin.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kwayland-integration/COPYING.LIB
