Name     : usrbinjava
Version  : 1.3
Release  : 7
URL      : https://github.com/clearlinux/usrbinjava/archive/v1.3.tar.gz
Source0  : https://github.com/clearlinux/usrbinjava/archive/v1.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: usrbinjava-bin = %{version}-%{release}
Requires: usrbinjava-license = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the usrbinjava package.
Group: Binaries
Requires: usrbinjava-license = %{version}-%{release}
Provides: openjdk-bin

%description bin
bin components for the usrbinjava package.


%package license
Summary: license components for the usrbinjava package.
Group: Default

%description license
license components for the usrbinjava package.


%prep
%setup -q -n usrbinjava-1.3
cd %{_builddir}/usrbinjava-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573233720
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1573233720
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/usrbinjava
cp %{_builddir}/usrbinjava-1.3/COPYING.Apache-2.0 %{buildroot}/usr/share/package-licenses/usrbinjava/2b8b815229aa8a61e483fb4ba0588b8b6c491890
%make_install
## install_append content
ln -s /usr/bin/java %{buildroot}/usr/bin/appletviewer
ln -s /usr/bin/java %{buildroot}/usr/bin/extcheck
ln -s /usr/bin/java %{buildroot}/usr/bin/idlj
ln -s /usr/bin/java %{buildroot}/usr/bin/jaotc
ln -s /usr/bin/java %{buildroot}/usr/bin/jar
ln -s /usr/bin/java %{buildroot}/usr/bin/jarsigner
ln -s /usr/bin/java %{buildroot}/usr/bin/java-rmi.cgi
ln -s /usr/bin/java %{buildroot}/usr/bin/javac
ln -s /usr/bin/java %{buildroot}/usr/bin/javadoc
ln -s /usr/bin/java %{buildroot}/usr/bin/javah
ln -s /usr/bin/java %{buildroot}/usr/bin/javap
ln -s /usr/bin/java %{buildroot}/usr/bin/jcmd
ln -s /usr/bin/java %{buildroot}/usr/bin/jconsole
ln -s /usr/bin/java %{buildroot}/usr/bin/jdb
ln -s /usr/bin/java %{buildroot}/usr/bin/jdeprscan
ln -s /usr/bin/java %{buildroot}/usr/bin/jdeps
ln -s /usr/bin/java %{buildroot}/usr/bin/jfr
ln -s /usr/bin/java %{buildroot}/usr/bin/jhat
ln -s /usr/bin/java %{buildroot}/usr/bin/jhsdb
ln -s /usr/bin/java %{buildroot}/usr/bin/jimage
ln -s /usr/bin/java %{buildroot}/usr/bin/jinfo
ln -s /usr/bin/java %{buildroot}/usr/bin/jjs
ln -s /usr/bin/java %{buildroot}/usr/bin/jlink
ln -s /usr/bin/java %{buildroot}/usr/bin/jmap
ln -s /usr/bin/java %{buildroot}/usr/bin/jmod
ln -s /usr/bin/java %{buildroot}/usr/bin/jps
ln -s /usr/bin/java %{buildroot}/usr/bin/jrunscript
ln -s /usr/bin/java %{buildroot}/usr/bin/jsadebugd
ln -s /usr/bin/java %{buildroot}/usr/bin/jshell
ln -s /usr/bin/java %{buildroot}/usr/bin/jstack
ln -s /usr/bin/java %{buildroot}/usr/bin/jstat
ln -s /usr/bin/java %{buildroot}/usr/bin/jstatd
ln -s /usr/bin/java %{buildroot}/usr/bin/keytool
ln -s /usr/bin/java %{buildroot}/usr/bin/native2ascii
ln -s /usr/bin/java %{buildroot}/usr/bin/orbd
ln -s /usr/bin/java %{buildroot}/usr/bin/pack200
ln -s /usr/bin/java %{buildroot}/usr/bin/policytool
ln -s /usr/bin/java %{buildroot}/usr/bin/rmic
ln -s /usr/bin/java %{buildroot}/usr/bin/rmid
ln -s /usr/bin/java %{buildroot}/usr/bin/rmiregistry
ln -s /usr/bin/java %{buildroot}/usr/bin/schemagen
ln -s /usr/bin/java %{buildroot}/usr/bin/serialver
ln -s /usr/bin/java %{buildroot}/usr/bin/servertool
ln -s /usr/bin/java %{buildroot}/usr/bin/tnameserv
ln -s /usr/bin/java %{buildroot}/usr/bin/unpack200
ln -s /usr/bin/java %{buildroot}/usr/bin/wsgen
ln -s /usr/bin/java %{buildroot}/usr/bin/wsimport
ln -s /usr/bin/java %{buildroot}/usr/bin/xjc
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/appletviewer
/usr/bin/extcheck
/usr/bin/idlj
/usr/bin/jaotc
/usr/bin/jar
/usr/bin/jarsigner
/usr/bin/java
/usr/bin/java-rmi.cgi
/usr/bin/javac
/usr/bin/javadoc
/usr/bin/javah
/usr/bin/javap
/usr/bin/jcmd
/usr/bin/jconsole
/usr/bin/jdb
/usr/bin/jdeprscan
/usr/bin/jdeps
/usr/bin/jfr
/usr/bin/jhat
/usr/bin/jhsdb
/usr/bin/jimage
/usr/bin/jinfo
/usr/bin/jjs
/usr/bin/jlink
/usr/bin/jmap
/usr/bin/jmod
/usr/bin/jps
/usr/bin/jrunscript
/usr/bin/jsadebugd
/usr/bin/jshell
/usr/bin/jstack
/usr/bin/jstat
/usr/bin/jstatd
/usr/bin/keytool
/usr/bin/native2ascii
/usr/bin/orbd
/usr/bin/pack200
/usr/bin/policytool
/usr/bin/rmic
/usr/bin/rmid
/usr/bin/rmiregistry
/usr/bin/schemagen
/usr/bin/serialver
/usr/bin/servertool
/usr/bin/tnameserv
/usr/bin/unpack200
/usr/bin/wsgen
/usr/bin/wsimport
/usr/bin/xjc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/usrbinjava/2b8b815229aa8a61e483fb4ba0588b8b6c491890
