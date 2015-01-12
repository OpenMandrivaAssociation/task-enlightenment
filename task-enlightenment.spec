Summary:	Metapackage for the Enlightenment
Name:		task-enlightenment
Version:	0.19
Release:	7
Epoch:		1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.rosalinux.com
Requires:	%{name}-minimal = %{EVRD}
Requires:	e_modules
Requires:	econnman
# Seems to be useless for now
#Requires:	emote
Requires:	emprint
Requires:	enjoy
Requires:	enventor
Requires:	ephoto
Requires:	epour
Requires:	python-efl
Requires:	rage
Requires:	terminology
# prefered apps
# Suggests:	lxdm
Obsoletes:	task-e17 < 1:0.18
Provides:	task-e19 = %{EVRD}
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
Requires:	e
Requires:	ecore
Requires:	edje
Requires:	eet
Requires:	eeze
Requires:	efreet
Requires:	eldbus
Requires:	elementary
Requires:	elua
Requires:	embryo
Requires:	emotion
Requires:	emotion_generic_players
Requires:	ethumb
Requires:	evas
Requires:	evas_generic_loaders
Requires:	expedite
Obsoletes:	e_dbus < 1.8.0
Obsoletes:	editje < 0.9.3-1
Obsoletes:	edje_viewer < 1.1.0-1
Obsoletes:	enki < 0.6.0-1
Obsoletes:	enlil < 0.6.1
Obsoletes:	exalt < 0.9-2
Obsoletes:	%{_lib}exalt1 < 0.9-2
Obsoletes:	%{_lib}exalt-devel < 0.9-2
Obsoletes:	task-e17-minimal < 1:0.18
Provides:	task-e19-minimal = %{EVRD}
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

