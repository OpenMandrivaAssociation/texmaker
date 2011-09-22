Name:            texmaker
Version:         3.1
Release:         %mkrel 1
Epoch:           1
Summary:         A QT-based LATEX editor
License:         GPL
Group:           Publishing
URL:             http://www.xm1math.net/texmaker/
Source0:         http://www.xm1math.net/texmaker/%name-%version.tar.bz2
Patch0:		 texmaker-3.1-hunspell.patch
Requires:        aspell
BuildRequires:   desktop-file-utils
BuildRequires:   qt4-devel >= 4.6.1
BuildRequires:   libpoppler-qt4-devel 
BuildRequires:   hunspell-devel
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Texmaker is a free LaTeX editor that integrates many tools needed to develop
documents with LaTeX, in just one application.

It includes the following features:
- an unicode editor to write your LaTeX source files 
  (syntax highlighting, undo-redo, search-replace, ...)
- the principal LaTex tags can be inserted directly with the "LaTeX", 
  "Math" and "Greek" menus 
- 370 mathematical symbols can be inserted in just one click 
- wizards to generate code ('Quick document', 'Quick letter', tabular,
  tabbing and array environments) 
- LaTeX-related programs can be launched via the "Tools" menu 
- the standard Bibtex entry types can be inserted in the ".bib" file
  with the "Bibliography" menu 
- a "structure view" of the document for easier navigation of a document 
  (by clicking on an item in the "Structure" frame, you can jump directly 
  to the corresponding part of your document 
- extensive LaTeX documentation 
- in the "Messages / Log File" frame, you can see information about processes 
  and the logfile after a LaTeX compilation 
- the "Next Latex Error" and "Previous Latex Error" commands let you reach the
  LaTeX errors detected by Kile in the log file 
- by clicking on the number of a line in the log file, the cursor jumps to the 
  corresponding line in the editor 

%prep
%setup -q
%patch0 -p1 -b .system

%build
export QTDIR=%{qt4dir}
%{qt4dir}/bin/qmake texmaker.pro
%{make}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%_bindir
INSTALL_ROOT=%{buildroot} make install

# icons
mkdir -p %{buildroot}%_miconsdir
cp utilities/texmaker16x16.png %{buildroot}%_miconsdir/%name.png
mkdir -p %{buildroot}%_iconsdir/hicolor/16x16/apps
cp utilities/texmaker16x16.png %{buildroot}%_iconsdir/hicolor/16x16/apps/%name.png
cp utilities/texmaker32x32.png %{buildroot}%_iconsdir/%name.png
mkdir -p %{buildroot}%_iconsdir/hicolor/32x32/apps
cp utilities/texmaker32x32.png %{buildroot}%_iconsdir/hicolor/32x32/apps/%name.png
mkdir -p %{buildroot}%_liconsdir
cp utilities/texmaker48x48.png %{buildroot}%_liconsdir/%name.png
mkdir -p %{buildroot}%_iconsdir/hicolor/48x48/apps
cp utilities/texmaker48x48.png %{buildroot}%_iconsdir/hicolor/48x48/apps/%name.png
mkdir -p %{buildroot}%_iconsdir/hicolor/scalable/apps
cp utilities/texmaker.svg %{buildroot}%_iconsdir/hicolor/scalable/apps/%name.svg

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%doc utilities/AUTHORS utilities/CHANGELOG.txt
%_bindir/%name
%_datadir/%name
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/*/apps/*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
