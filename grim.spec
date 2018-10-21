%global provider        github
%global provider_tld    com
%global project         emersion
%global repo            grim
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          97202f22003200edcc3fb5966ddc9b19cfe1c6f9
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           grim
Version:        0.0.1
Release:        4.git%{shortcommit}%{?dist}
Summary:        Grab images from a Wayland compositor.
License:        MIT
URL:            https://%{provider_prefix}

Source:         https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

Requires:       libwayland-client
Requires:       cairo
Requires:       libjpeg
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  cairo-devel
BuildRequires:  wayland-devel
BuildRequires:  libjpeg-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  scdoc

%description
%{summary}.

%prep
%setup -q -n %{repo}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/grim
%{_mandir}/man1/grim.1.gz

%changelog
* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-4.git97202f2
- Fix dependency

* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-3.git97202f2
- Fix dependency

* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-2.git97202f2
- Fix dependency

* Sun Oct 21 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-1.git97202f2
- Initial package
