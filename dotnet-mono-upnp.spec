Summary:	Client/server libraries for UPnP
Name:		dotnet-mono-upnp
Version:	0.1.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/downloads/mono/mono-upnp/mono-upnp-%{version}.tar.gz
# Source0-md5:	76fc45684f3baf21134c06a68a75e51b
Patch0:		%{name}-use-mono-nunit.patch
Patch1:		%{name}-install.patch
URL:		https://github.com/mono/mono-upnp
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	dotnet-taglib-sharp-devel
BuildRequires:	mono-addins-devel
BuildRequires:	mono-csharp
BuildRequires:	mono-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mono.Upnp is a set of client/server libraries for the Universal Plug
'n Play specification.

%package devel
Summary:	Mono.Upnp development files
Summary(pl.UTF-8):	Pliki programistyczne Mono.Upnp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package provides development files for Mono.Upnp.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki programistyczne dla Mono.Upnp.

%prep
%setup -q -n mono-upnp-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md
%attr(755,root,root) %{_bindir}/mono-upnp-gtk
%attr(755,root,root) %{_bindir}/mono-upnp-simple-media-server
%{_prefix}/lib/mono-upnp

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/mono.ssdp.pc
%{_pkgconfigdir}/mono.upnp.dcp.mediaserver1.filesystem.pc
%{_pkgconfigdir}/mono.upnp.dcp.mediaserver1.gtkclient.pc
%{_pkgconfigdir}/mono.upnp.dcp.mediaserver1.pc
%{_pkgconfigdir}/mono.upnp.dcp.msmediareceiverregistrar1.pc
%{_pkgconfigdir}/mono.upnp.pc
