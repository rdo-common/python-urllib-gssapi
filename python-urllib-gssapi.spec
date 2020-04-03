%global sname urllib-gssapi
%global s_name urllib_gssapi

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-%{sname}
Version:        1.0.1
Release:        11%{?dist}
Summary:        A GSSAPI/SPNEGO authentication handler for urllib/urllib2

License:        ASL 2.0
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/releases/download/v%{version}/%{s_name}-%{version}.tar.gz
BuildArch:      noarch

# Patches
BuildRequires:  git-core

%global _description\
urllib_gssapi is a backend for urllib.  It provides GSSAPI/SPNEGO\
authentication to HTTP servers.  urllib_gssapi replaces urllib_kerberos and\
behaves in the same ways.

%description %_description

%if %{with python2}
%package -n python2-%{sname}
Summary:        %summary
BuildRequires:  python2-devel
BuildRequires:  python-gssapi
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools
Requires:       python-gssapi
%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname} %_description
%endif

%if %{with python3}
%package -n python3-%{sname}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-gssapi
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
Requires:       python3-gssapi
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description
%endif

%prep
%autosetup -S git -n %{s_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%check
%if %{with python2}
%{__python2} setup.py nosetests
%endif
%if %{with python3}
%{__python3} setup.py nosetests
%endif

%if %{with python2}
%files -n python2-%{sname}
%doc README.md
%license COPYING
%{python2_sitelib}/%{s_name}*
%endif
%if %{with python3}
%files -n python3-%{sname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{s_name}*
%endif

%changelog
* Fri Apr 03 2020 Javier Peña <jpena@redhat.com> - 1.0.1-11
- Adapted for RDO, made it build for python 2 and 3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.1-5
- Drop python2 subpackage
- Resolves: #1655258

* Mon Sep 24 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.1-4
- Drop requirement on python-requests
- Resolves: #1631938

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.7

* Fri Feb 23 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.1-1
- New upstream release (v1.0.0)
- Adds COPYING and removes shebang
- Resolves: #1546835

* Mon Feb 19 2018 Robbie Harwood <rharwood@redhat.com> - 1.0.0-1
- New upstream release (v1.0.0)
