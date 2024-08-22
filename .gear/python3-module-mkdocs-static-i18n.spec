%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs-static-i18n
%define mod_name mkdocs_static_i18n

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.3
Release: alt1

Summary: MkDocs i18n plugin using static translation markdown files
License: MIT
Group: Development/Python3
Url: https://github.com/ultrabug/mkdocs-static-i18n
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel), python3(hatchling)

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
%endif

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 22 2024 Maria Alexeeva <alxvmr@altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus.

