# Copyright 2018 Cray Inc. All Rights Reserved.

Name: haproxy-installer-crayctldeploy
License: Cray Software License Agreement
Summary: haproxy deployment ansible role
Group: System/Management
Version: 0.2.0
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2
Vendor: Cray Inc.
Requires: cray-crayctl
Requires: kubernetes-crayctldeploy

# Project level defines TODO: These should be defined in a central location; DST-892
%define afd /opt/cray/crayctl/ansible_framework
%define roles %{afd}/roles
%define playbooks %{afd}/main
%define modules %{afd}/library

%description
This is an Ansible role for the deployment of haproxy in front of etcd.

%prep
%setup -q

%build

%install
install -m 755 -d %{buildroot}%{roles}/

# All roles
cp -r roles/* %{buildroot}%{afd}/roles/


%clean
rm -rf %{buildroot}%{roles}/*

%files
%defattr(-, root, root)

%{roles}

%changelog
