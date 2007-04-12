%define name texmaker
%define version 1.12
%define release %mkrel 2
%define qtdir %_prefix/lib/qt3

Summary: A LATEX editor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Publishing
Url: http://www.xm1math.net/texmaker/index.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: qt3-devel
BuildRequires: kdelibs-devel

%description
Texmaker is a program, that integrates many tools needed 
to develop documents with LaTeX, in just one application. 

It have thoses features:
- an editor to write your LaTeX source files 
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
#export LD_LIBRARY_PATH=%qtdir/lib:$LD_LIBRARY_PATH
#export PATH=%qtdir/bin:$PATH
export QTDIR=%qtdir
%qtdir/bin/qmake -makefile -unix "LIBS +=-lm $QTDIR/%{_lib}/libqt-mt.so.3" texmaker.pro

export CFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS=$RPM_OPT_FLAGS

%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT{%_miconsdir,%_iconsdir,%_liconsdir}
mkdir -p $RPM_BUILD_ROOT%_datadir/applnk/Office
cp -v utilities/texmaker.desktop $RPM_BUILD_ROOT%_datadir/applnk/Office/texmaker.desktop
cp -v texmaker $RPM_BUILD_ROOT%_bindir/texmaker
cp -v utilities/texmaker16x16.png $RPM_BUILD_ROOT%_miconsdir/%name.png
cp -v utilities/texmaker32x32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
cp -v utilities/texmaker48x48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png

# menu of course
mkdir -p $RPM_BUILD_ROOT/%_menudir
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/%{name}"\
title="Texmaker"\
longtitle="A power latex editor"\
needs="kde"\
section="Office/Wordprocessors"\
icon="%{name}.png"
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc utilities/latexhelp.html utilities/usermanual.html utilities/AUTHORS utilities/COPYING utilities/*.gif utilities/doc*
%_bindir/%name
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%_menudir/%name
%_datadir/applnk/Office/%name.desktop

