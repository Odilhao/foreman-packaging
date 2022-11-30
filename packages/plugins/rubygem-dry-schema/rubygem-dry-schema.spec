# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name dry-schema
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.6.2
Release: 1%{?dist}
Summary: Coercion and validation for data structures
Group: Development/Languages
License: MIT
URL: https://dry-rb.org/gems/dry-schema
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 2
Requires: %{?scl_prefix}rubygem(dry-configurable) >= 0.8
Requires: %{?scl_prefix}rubygem(dry-configurable) < 1
Requires: %{?scl_prefix}rubygem(dry-configurable) >= 0.8.3
Requires: %{?scl_prefix}rubygem(dry-core) >= 0.5
Requires: %{?scl_prefix}rubygem(dry-core) < 1
Requires: %{?scl_prefix}rubygem(dry-core) >= 0.5
Requires: %{?scl_prefix}rubygem(dry-initializer) >= 3.0
Requires: %{?scl_prefix}rubygem(dry-initializer) < 4
Requires: %{?scl_prefix}rubygem(dry-logic) >= 1.0
Requires: %{?scl_prefix}rubygem(dry-logic) < 2
Requires: %{?scl_prefix}rubygem(dry-types) >= 1.5
Requires: %{?scl_prefix}rubygem(dry-types) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
dry-schema provides a DSL for defining schemas with keys and rules that should
be applied to
values. It supports coercion, input sanitization, custom types and localized
error messages
(with or without I18n gem). It's also used as the schema engine in
dry-validation.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/config
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/dry-schema.gemspec

%changelog
* Tue May 31 2022 Dirk Goetz <dirk.goetz@netways.de> 1.6.2-1
- Add rubygem-dry-schema generated by gem2rpm using the scl template
