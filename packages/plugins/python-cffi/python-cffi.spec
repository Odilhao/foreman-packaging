%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name cffi

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python calling C code

License:        MIT
URL:            http://cffi.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pycparser
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  libffi-devel
BuildRequires:  gcc


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-pycparser

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Fix PEP 639 license field (RHEL 9 setuptools does not support SPDX string format)
sed -i 's/^license = "\(.*\)"/license = {text = "\1"}/' pyproject.toml
sed -i '/^license-files/d' pyproject.toml
# Remove bundled egg-info
rm -rf src/%{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%exclude %{_bindir}/cffi-gen-src
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/_cffi_backend.cpython-3*-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Aug 13 2026 Odilon Sousa <osousa@redhat.com> - 2.1.1-1
- Initial package.
