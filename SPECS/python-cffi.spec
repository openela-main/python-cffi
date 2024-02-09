Name:           python-cffi
Version:        1.11.5
Release:        5%{?dist}
Summary:        Foreign Function Interface for Python to call C code
License:        MIT
URL:            http://cffi.readthedocs.org/
Source0:        https://pypi.io/packages/source/c/cffi/cffi-%{version}.tar.gz

BuildRequires:  libffi-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pycparser
BuildRequires:  python3-pytest

# Do not check .so files in the python_sitelib directory
# or any files in the application's directory for provides
%global __provides_exclude_from ^(%{python_sitearch}|%{python3_sitearch})/.*\\.so$

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%package -n python3-cffi
Summary:        Foreign Function Interface for Python 3 to call C code
Requires:       python3-pycparser
%{?python_provide:%python_provide python3-cffi}

%description -n python3-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.
%package doc
Summary:        Documentation for CFFI
BuildArch:      noarch
Requires:       python3-cffi = %{version}-%{release}

%description doc
Documentation for CFFI, the Foreign Function Interface for Python.

%prep
%setup -q -n cffi-%{version}

%build
%py3_build
cd doc
make html
rm build/html/.buildinfo

#Tests fail but only in mock.
#%check
#%{__python3} setup_base.py build_ext -f -i
#PYTHONPATH=build/lib.linux-* py.test-3 c/ testing/

%install
%py3_install \
    --record %{buildroot}%{python3_sitearch}/cffi-%{version}-py%{python3_version}.egg-info/installed-files.txt

%files -n python3-cffi
%doc PKG-INFO
%license LICENSE
%{python3_sitearch}/*

%files doc
%doc doc/build/html


%changelog
* Mon Oct 22 2018 Christian Heimes <cheimes@redhat.com> - 1.11.5-5
- Build doc package, resolves rhbz#1641665

* Thu Jun 07 2018 Troy Dawson <tdawson@redhat.com> - 1.11.5-4
- No python2 in RHEL8

* Fri May 25 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.11.5-3
- Disable tests to fix mock-only FTBFS.

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11.5-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Mar 02 2018 John Dulaney <jdulaney@Fedoraproject.org> - 1.11.2-1
- New release 1.11.5

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.11.2-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.11.2-1
- New release 1.11.0
- Fix %%check

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 1.11.0-2
- Cleanup spec file conditionals

* Sat Sep 23 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.11.0-1
- New release 1.11.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.10.0-1
- New release 1.10.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 John Dulaney <jdulaney@Fedoraproject.org> - 1.9.1-1
- Update to latest upstream 1.9.1

* Fri Jan 6 2017 Orion Poplawski <orion@cora.nwra.com> - 1.8.3-4
- Modernize spec

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.8.3-3
- Rebuild for Python 3.6
- Disable test dependencies

* Thu Nov 03 2016 John Dulaney <jdulaney@Fedoraproject.org> - 1.8.3-2
- Re-disable check

* Sun Sep 18 2016 John Dulaney <jdulaney@Fedoraproject.org> - 1.8.3-1
- Update to 1.8.3
- Reenable check

* Wed Sep 07 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Tue Aug 09 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.7.0-3
- Record installed files

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 23 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Thu Apr 28 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6.0-3
- Switch Source0 to using pypi.io

* Thu Apr 28 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6.0-2
- Update Source0 URL to account for pypi change

* Thu Apr 21 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1329203)

* Mon Feb 15 2016 John Dulaney <jdulaney@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2 (#1299272)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.5.0-1
- Update to 1.5.0 (#1299272)

* Mon Jan 11 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.4.2-2
- Move python-cffi => python2-cffi

* Tue Dec 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 (#1293504)

* Thu Dec 17 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.4.1-1
- Update to latest upstream release

* Fri Dec 11 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.3.1-1
- Update to latest upstream release

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.1.2-4
- Rebuilt for Python3.5 rebuild

* Wed Jul 15 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.1.2-3
- Modernize spec file
- add missing source

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 16 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.1.2-2
- Update to 1.1.2
- Fix license

* Tue Aug 19 2014 Eric Smith <spacewar@gmail.com> 0.8.6-1
- Update to latest upstream.
- No python3 in el7.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 26 2014 Eric Smith <spacewar@gmail.com> 0.8.1-1
- Update to latest upstream.

* Tue Aug 13 2013 Eric Smith <spacewar@gmail.com> 0.6-5
- Add Requires of python{,3}-pycparser.

* Thu Jul 25 2013 Eric Smith <spacewar@gmail.com> 0.6-4
- Fix broken conditionals in spec (missing question marks), needed for el6.

* Tue Jul 23 2013 Eric Smith <spacewar@gmail.com> 0.6-3
- Add Python3 support.

* Mon Jul 22 2013 Eric Smith <spacewar@gmail.com> 0.6-2
- Better URL, and use version macro in Source0.

* Sun Jul 21 2013 Eric Smith <spacewar@gmail.com> 0.6-1
- initial version
