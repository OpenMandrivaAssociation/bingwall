%define oname   BingWall
%define gitdate 20200417

Name:           bingwall
Version:        1
Release:        0.%{gitdate}.1
Summary:        Bing wallpaper of the day application based on Qt libs for Gnome desktop
License:        MIT
Group:          Graphical desktop
URL:            https://github.com/keshavbhatt/BingWall
# No release tag/tarball yet, just git.
#Source0:        https://github.com/keshavbhatt/BingWall/releases
Source0:        %{oname}-%{gitdate}.tar.xz

BuildRequires:  qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  qmake5
BuildRequires:  rpm-helper
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5OpenGL)

%description
Bing wallpaper of the day application for Gnome desktop based on Qt libraries.
BingWall - Little utility to browse/download/setting bing's wallpaper of the day to Gnome desktop
eatures
-Allows list bing wallpaper of the day for 10 Countries (All supported by bing API).
-Simple to use neat interface.
-Allow Downloading of wallpapers and saving them to a browsable location.
-Downloaded wallpapers are accessible from with the application.
-Dark Theme.

%prep
%setup -q -n %{oname}-{gitdate}

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/bing-wall
%{_datadir}/applications/%{name}.desktop
