%global sname urllib-gssapi
%global s_name urllib_gssapi

Name:           python-%{sname}
Version:        1.0.1
Release:        3%{?dist}
Summary:        A GSSAPI/SPNEGO authentication handler for urllib/urllib2

License:        ASL 2.0
URL:            https://github.com/pythongssapi/%{sname}
Source0:        https://github.com/pythongssapi/%{sname}/releases/download/v%{version}/%{s_name}-%{version}.tar.gz
BuildArch:      noarch

# Patches

BuildRequires:  git-core

BuildRequires:  python2-devel
BuildRequires:  python2-gssapi
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-gssapi
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools


%global _description\
urllib_gssapi is a backend for urllib.  It provides GSSAPI/SPNEGO\
authentication to HTTP servers.  urllib_gssapi replaces urllib_kerberos and\
behaves in the same ways.

%description %_description

%package -n python2-%{sname}
Summary:        %summary
Requires:       python2-gssapi
Requires:       python2-requests
%{?python_provide:%python_provide python2-%{sname}}
%description -n python2-%{sname} %_description

%package -n python3-%{sname}
Summary:        %summary
Requires:       python3-gssapi
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{sname}}
%description -n python3-%{sname} %_description


%prep
%autosetup -S git -n %{s_name}-%{version}


%build
%py2_build
%py3_build


%install
# must be python3 first
%py3_install
%py2_install


%check
%{__python2} setup.py nosetests
%{__python3} setup.py nosetests


%files -n python2-%{sname}
%doc README.md
%license COPYING
%{python2_sitelib}/%{s_name}*


%files -n python3-%{sname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{s_name}*


%changelog
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
