Name:		rpm-javamacros
Version:	1.0
Release:	1
Summary:	RPM macros for dealing with Java files
Group:		Development/Java
License:	GPLv3
Source0:	jmod.deps
Source1:	jmod.attr
Requires:	java-13-openjdk
BuildArch:	noarch

%description
RPM macros for dealing with Java files

%prep

%build

%install
mkdir -p %{buildroot}%{_rpmconfigdir}/fileattrs
install -c -m 755 %{S:0} %{buildroot}%{_rpmconfigdir}/
install -c -m 644 %{S:1} %{buildroot}%{_rpmconfigdir}/fileattrs/

%files
%{_rpmconfigdir}/jmod.deps
%{_rpmconfigdir}/fileattrs/jmod.attr
