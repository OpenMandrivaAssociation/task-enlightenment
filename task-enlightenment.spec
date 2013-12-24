Summary:	Metapackage for the Enlightenment
Name:		task-enlightenment
Version:	0.18
Release:	2
Epoch:		1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.rosalinux.com
Requires:	%{name}-minimal = %{EVRD}
Requires:	e_modules
Requires:	emprint
Requires:	enjoy
Requires:	ephoto
Requires:	terminology
# prefered apps
# Suggests:	lxdm
Obsoletes:	task-e17 < 1:0.18
Provides:	task-e18 = %{EVRD}
Provides:	task-e17 = %{EVRD}
BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
all Enlightenment applications and libraries.

%files

#----------------------------------------------------------------------------

%package minimal
Summary:	Metapackage minimal for the Enlightenment
License:	BSD
Group:		Graphical desktop/Enlightenment
Requires:	eet
Requires:	evas
Requires:	ecore
Requires:	embryo
Requires:	edje
Requires:	efreet
Requires:	eldbus
Requires:	eeze
Requires:	expedite
Requires:	evas_generic_loaders
Requires:	emotion
Requires:	ethumb
Requires:	elementary
Requires:	e
Obsoletes:	e_dbus < 1.8.0
Obsoletes:	editje < 0.9.3-1
Obsoletes:	edje_viewer < 1.1.0-1
Obsoletes:	enki < 0.6.0-1
Obsoletes:	enlil < 0.6.1
Obsoletes:	exalt < 0.9-2
Obsoletes:	task-e17-minimal < 1:0.18
Provides:	task-e18-minimal = %{EVRD}
Provides:	task-e17-minimal = %{EVRD}
BuildArch:	noarch

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal set of Enlightenment applications and libraries.

%files minimal

#----------------------------------------------------------------------------

%prep

%build

%install

