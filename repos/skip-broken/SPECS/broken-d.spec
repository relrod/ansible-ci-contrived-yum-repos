Name:           broken-d
Version:        1.2.5
Release:        1%{?dist}
Summary:        A package for testing skip_broken in the dnf module

License:        PublicDomain

Requires:       broken-a

%description
Useless

%install
mkdir -p %{buildroot}%{_bindir}
echo c > %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
