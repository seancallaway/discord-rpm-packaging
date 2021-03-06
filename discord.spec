%global         debug_package %{nil}
%global         __strip /bin/true
%global         __requires_exclude libffmpeg.so

Name:           discord
Version:        0.0.4
Release:        1%{?dist}
Summary:        All-in-one voice and text chat for gamers

# License Information: https://bugzilla.rpmfusion.org/show_bug.cgi?id=4441#c14
License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils%{_isa}
BuildRequires:  sed%{_isa}

Requires:       glibc%{_isa}
Requires:       alsa-lib%{_isa}
Requires:       GConf2%{_isa}
Requires:       libnotify%{_isa}
Requires:       nspr%{_isa} >= 4.13
Requires:       nss%{_isa} >= 3.27
Requires:       libX11%{_isa} >= 1.6
Requires:       libXtst%{_isa} >= 1.2
Requires:       libappindicator%{_isa}
Requires:       libcxx%{_isa}

%description
Linux Release for Discord, a free proprietary VoIP application designed for
gaming communities.

%prep
%autosetup -n Discord

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_libdir}/discord
mkdir -p %{buildroot}/%{_datadir}/applications

cp -r * %{buildroot}/%{_libdir}/discord/
ln -sf %{_libdir}/discord/Discord %{buildroot}/%{_bindir}/
desktop-file-install                            \
--set-icon=%{_libdir}/discord/discord.png       \
--set-key=Exec --set-value=%{_bindir}/Discord   \
--delete-original                               \
--dir=%{buildroot}/%{_datadir}/applications     \
discord.desktop

%files
%defattr(-,root,root)
%{_libdir}/discord/
%{_bindir}/Discord
%{_datadir}/applications/discord.desktop


%changelog
* Wed Jan 31 2018 Sean Callaway <seancallaway@fedoraproject.org> 0.0.4-1
- Update to 0.0.4

* Tue Dec 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.3-1
- Update to 0.0.3
- Now using desktop-file-install.
- Removed unneeded requirements.

* Wed Aug 16 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.2-1
- Update to 0.0.2
- Spec file cleanup.

* Thu Jan 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.1-1
- Initial build using version 0.0.1
