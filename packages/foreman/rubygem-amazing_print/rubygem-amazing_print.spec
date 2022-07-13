# template: default
%global gem_name amazing_print

Name: rubygem-%{gem_name}
Version: 1.4.0
Release: 1%{?dist}
Summary: Pretty print Ruby objects with proper indentation and colors
License: MIT
URL: https://github.com/amazing-print/amazing_print
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Great Ruby debugging companion: pretty print Ruby objects to visualize their
structure. Supports custom object formatting via plugins.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/Appraisals
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Wed Jul 13 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.4.0-1
- Update to 1.4.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-2
- Rebuild against rh-ruby27

* Mon May 18 2020 Michael Moll <mmoll@mmoll.at> - 1.1.0-1
- Add rubygem-amazing_print generated by gem2rpm using the scl template

