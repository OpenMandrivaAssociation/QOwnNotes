%global appname QOwnNotes
%global url1    https://github.com/pbek
 
Name:           qownnotes
Version:        20.5.13
Release:        1
Summary:        QOwnNotes is a plain-text file notepad and todo-list manager with markdown support and ownCloud / Nextcloud integration.
 
# The entire source code is MIT except bundled libs:
# BSD:          qdarkstyle
#               qkeysequencewidget
#               qmarkdowntextedit
#               singleapplication
#               simplecrypt
# MIT:          piwiktracker
#               md4c
# GPLv2         versionnumber
# GPLv3+        qttoolbareditor
# LGPLv2+       fakevim
# ASL 2.0       diff_match_patch
License:        MIT and BSD and GPLv2 and GPLv3+ and LGPLv2+ and ASL 2.0
URL:            https://www.qownnotes.org

Source0:        https://download.tuxfamily.org/qownnotes/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(appstream-glib)
 
Requires:       hicolor-icon-theme
Recommends:     %{name}-translations = %{version}-%{release}
 
Provides:       bundled(fakevim) = 0.0.1
Provides:       bundled(md4c) = 0.4.2~git%{md4c_shortcommit}
Provides:       bundled(qhotkey) = 1.3.0~git%{qhotkey_commit}
Provides:       bundled(qkeysequencewidget) = 1.0.1
Provides:       bundled(qmarkdowntextedit) = 2019.4.0~git%{qmarkdowntextedit_shortcommit}
Provides:       bundled(qt-piwik-tracker) = 0~git%{piwiktracker_shortcommit}
Provides:       bundled(qt-toolbar-editor) = 0~git%{qttoolbareditor_shortcommit}
Provides:       bundled(qtcsv) = 1.2.2

 
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
%autosetup -n %{name}-%{version}
 
 
%build
# Build translations
# * https://github.com/pbek/QOwnNotes/issues/1744
lrelease-qt5 src/%{name}.pro
 
%qmake_qt5 \
    PREFIX=%{buildroot}%{_prefix} \
    
%make_build -C
 
 
%install
%make_install -C
install -m 0644 -Dp obs/%{name}.appdata.xml %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
%find_lang %{name} --with-qt

 
 
%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml
 
%files -f %{appname}.lang translations
%{_datadir}/qt5/translations/%{appname}_ceb.qm
%{_datadir}/qt5/translations/%{appname}_fil.qm
%{_datadir}/qt5/translations/%{appname}_hil.qm
