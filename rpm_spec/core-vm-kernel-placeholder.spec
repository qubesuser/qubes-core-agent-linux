# We don't install kernel pkg in VM, but some other pkgs depends on it.
# Done as separate subpackage because yum allows multiple versions of kernel
# pkg installed simultaneusly - and of course we don't want multiple versions
# of qubes-core-vm
Name:       qubes-core-vm-kernel-placeholder
Summary:    Placeholder for kernel package as it is managed by Dom0
Version:	1.0
Release:	3%{dist}
Vendor:		Invisible Things Lab
License:	GPL
Group:		Qubes
URL:		http://www.qubes-os.org
#  template released with 1.0-rc1 have kernel-debug installed by mistake. This
#  line is required to smooth upgrade.
Obsoletes:  kernel-debug
#  this driver require exact kernel-drm-nouveau version; as isn't needed in VM,
#  just remove it
Obsoletes:  xorg-x11-drv-nouveau
Provides:   xorg-x11-drv-nouveau
#  choose the oldest Qubes-supported VM kernel
Provides:   kernel = 3.7.4
Provides:   kernel-modules-extra
# for xl2tpd
Provides: kmod(l2tp_ppp.ko)

%description
Placeholder for kernel package as it is managed by Dom0.

%install

mkdir -p $RPM_BUILD_ROOT/lib/modules

%files
%if %{fedora} > 18
%dir /lib/modules
%endif
