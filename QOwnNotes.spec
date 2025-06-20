%global debug_package %{nil}

%global appname QOwnNotes
%global url1    https://github.com/pbek
 
Name:           qownnotes
Version:        25.6.0
Release:        1
Summary:        QOwnNotes is a plain-text file notepad and todo-list manager with markdown support and ownCloud / Nextcloud integration.
License:        MIT and BSD and GPLv2 and GPLv3+ and LGPLv2+ and ASL 2.0
URL:            https://www.qownnotes.org

Source0:        https://github.com/pbek/QOwnNotes/releases/download/v%{version}/qownnotes-%{version}.tar.xz
#Source0:        https://download.tuxfamily.org/qownnotes/src/%{name}-%{version}.tar.xz

BuildRequires:  qmake-qt6
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WebSockets)
#BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6Xml)
#BuildRequires:  cmake(Qt6XmlPatterns)
BuildRequires:  pkgconfig(appstream-glib)
 
Requires:       hicolor-icon-theme
Recommends:     %{name}-translations = %{version}-%{release}

%patchlist
#qownnotes-24.8.4-compile.patch
 
%description
QOwnNotes is the open source notepad with markdown support and todo list manager
for GNU/Linux, Mac OS X and Windows, that works together with the default notes
application of ownCloud and Nextcloud.
 
You are able to write down your thoughts with QOwnNotes and edit or search for
them later from your mobile device, like with CloudNotes or the
ownCloud/Nextcloud web-service.
 
The notes are stored as plain text files and are synced with
ownCloud's/Nextcloud's file sync functionality. Of course other software, like
Syncthing or Dropbox can be used too.
 
I like the concept of having notes accessible in plain text files, like it is
done in the ownCloud/Nextcloud notes apps, to gain a maximum of freedom, but I
was not able to find a decent desktop note taking tool or a text editor, that
handles them well. Out of this need QOwnNotes was born.
 
 
%package        translations
Summary:        Translations files for %{name}
BuildArch:      noarch
 
Requires:       %{name} = %{version}-%{release}
 
%description    translations
Translations files for %{name}.
 
 
%prep
%autosetup -n %{name}-%{version} -p1
 
%build
# Build translations
# * https://github.com/pbek/QOwnNotes/issues/1744
#lrelease-qt5 src/%{name}.pro
 
qmake-qt6 \
    PREFIX=%{buildroot}%{_prefix} \
    
%make_build
 
 
%install
%make_install
 
%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
#{_metainfodir}/*.xml
 
%files translations
%{_datadir}/qt6/translations/%{appname}_*
