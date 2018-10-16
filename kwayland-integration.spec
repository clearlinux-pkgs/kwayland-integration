#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kwayland-integration
Version  : 5.14.1
Release  : 4
URL      : https://download.kde.org/stable/plasma/5.14.1/kwayland-integration-5.14.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.1/kwayland-integration-5.14.1.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.1/kwayland-integration-5.14.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kwayland-integration-data = %{version}-%{release}
Requires: kwayland-integration-lib = %{version}-%{release}
Requires: kwayland-integration-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n kwayland-integration-5.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539704258
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539704258
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwayland-integration
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kwayland-integration/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/kwindowsystem.kwayland.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWaylandPlugin.so
/usr/lib64/qt5/plugins/kf5/org.kde.kwindowsystem.platforms/KF5WindowSystemKWaylandPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland-integration/COPYING.LIB
