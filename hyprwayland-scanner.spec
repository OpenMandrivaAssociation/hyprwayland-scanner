Name:           hyprwayland-scanner
Version:        0.4.2
Release:        1
Summary:        A Hyprland implementation of wayland-scanner, in and for C++
Group:          Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(pugixml)

%description
%{summary}.

%package        devel
Summary:        A Hyprland implementation of wayland-scanner, in and for C++

%description    devel
%{summary}.
%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files devel
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/
