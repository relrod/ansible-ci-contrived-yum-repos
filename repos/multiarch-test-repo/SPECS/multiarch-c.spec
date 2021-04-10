Name:		multiarch-c
Version:	%{_pkgversion}
Release:	1%{?dist}
License:        PublicDomain
Summary:	A test package built for multiple architectures

%description
Test package.

%prep

%build

%install
mkdir -p %{buildroot}/%{_bindir}
echo 'echo %{name}' > %{buildroot}/%{_bindir}/%{name}
chmod +x %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
