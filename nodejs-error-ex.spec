%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# we have older version of coffee-script in fedora
%global enable_tests 0
%global module_name error-ex
%global gittag0 1.2.0

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        %{gittag0}
Release:        5%{?dist}
Summary:        Easy error subclassing and stack customization

License:        MIT
URL:            https://github.com/Qix-/node-error-ex
Source0:        https://github.com/Qix-/node-%{module_name}/archive/%{gittag0}.tar.gz#/%{module_name}-%{gittag0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}coffee-script
BuildRequires: %{?scl_prefix}coveralls
BuildRequires: %{?scl_prefix}nodejs-istanbul
BuildRequires: %{?scl_prefix}mocha
BuildRequires: %{?scl_prefix}npm(should)
%endif

%description
%{summary}.

%prep
%setup -q -n node-%{module_name}-%{gittag0}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha --compilers coffee:coffee-script/register
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.2.0-5
- rebuilt

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 1.2.0-4
- Enable scl macros

* Fri Sep 25 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.1-1
- Initial packaging
