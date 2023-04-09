# template: default
%global gem_name gapic-common

Name: rubygem-%{gem_name}
Version: 0.12.0
Release: 1%{?dist}
Summary: Common code for GAPIC-generated API clients
License: Apache-2.0
URL: https://github.com/googleapis/gapic-generator-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby >= 2.6
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Common code for GAPIC-generated API clients.


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
%exclude %{gem_instdir}/.yardopts
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/RELEASING.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
* Fri Sep 30 2022 Eric D. Helms <ericdhelms@gmail.com> 0.12.0-1
- Add rubygem-gapic-common generated by gem2rpm using the default template
