%define name 	texmaker
%define version 1.5
%define release %mkrel 1

%define qtdir	%_prefix/lib/qt4

Summary: 	A QT-based LATEX editor
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Epoch:		1
Source0: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		Publishing
Url: 		http://www.xm1math.net/texmaker/index.html
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	qt4-devel
Requires:	aspell

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

%build
export QTDIR=%qtdir
%qtdir/bin/qmake %name.pro
perl -pi -e "s|-O2|$RPM_OPT_FLAGS||g" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
install -m 755 %name %buildroot/%_bindir

# icons
mkdir -p %buildroot/%_miconsdir
cp utilities/texmaker16x16.png $RPM_BUILD_ROOT/%_miconsdir/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/16x16/apps
cp utilities/texmaker16x16.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/16x16/apps/%name.png
cp utilities/texmaker32x32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/32x32/apps
cp utilities/texmaker32x32.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/32x32/apps/%name.png
mkdir -p %buildroot/%_liconsdir
cp utilities/texmaker48x48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/48x48/apps
cp utilities/texmaker48x48.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/48x48/apps/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/scalable/apps
cp utilities/texmaker.svg $RPM_BUILD_ROOT/%_iconsdir/hicolor/scalable/apps/%name.svg

# menu
mkdir -p %buildroot/%_datadir/applications
cp utilities/texmaker.desktop %buildroot/%_datadir/applications

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc utilities/*.html utilities/*.css utilities/AUTHORS utilities/*.gif utilities/*.png
%_bindir/%name
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/applications/%name.desktop

