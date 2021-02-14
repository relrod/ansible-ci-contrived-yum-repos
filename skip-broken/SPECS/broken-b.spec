Name:           broken-b
Version:        1.2.3
Release:        1%{?dist}
Summary:        A package for testing skip_broken in the dnf module

License:        PublicDomain

Requires:       broken-a = 1.2.3

%description
Useless

%install
mkdir -p %{buildroot}%{_bindir}
echo b > %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
