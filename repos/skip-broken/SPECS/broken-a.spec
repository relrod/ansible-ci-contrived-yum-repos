Name:           broken-a
Version:        %{?_pkgversion}%{!?_pkgversion:1.2.3}
Release:        1%{?dist}
Summary:        A package for testing skip_broken in the dnf module

License:        PublicDomain

%if "%{version}" == "2.0.0"
Requires:       nonexistent-package
%endif

%if "%{version}" == "1.2.3.4"
Requires:       nonexistent-package
%endif

%description
Useless

%install
mkdir -p %{buildroot}%{_bindir}
echo a > %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
