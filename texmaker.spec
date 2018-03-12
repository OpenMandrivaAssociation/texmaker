%define debug_package %{nil}

Name:            texmaker
Version:         5.0.2
Release:         1
Epoch:           1
Summary:         A QT-based LATEX editor
License:         GPLv2+
Group:           Publishing
URL:             http://www.xm1math.net/texmaker/
Source0:         http://www.xm1math.net/texmaker/%{name}-%{version}.tar.bz2
Requires:        aspell
Requires:	 texlive-collection-latex
BuildRequires:   desktop-file-utils
BuildRequires:   hunspell-devel
BuildRequires:	 cmake(ECM)
BuildRequires:	 cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Network) cmake(Qt5PrintSupport) cmake(Qt5Script) cmake(Qt5Widgets) cmake(Qt5Xml)

%description
Texmaker is a free LaTeX editor that integrates many tools needed to develop
documents with LaTeX, in just one application.

It includes the following features:
- an Unicode editor to write your LaTeX source files 
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
  and the log file after a LaTeX compilation 
- the "Next Latex Error" and "Previous Latex Error" commands let you reach the
  LaTeX errors detected by Kile in the log file 
- by clicking on the number of a line in the log file, the cursor jumps to the 
  corresponding line in the editor 

%prep
%setup -q

%build
%{qmake_qt5} texmaker.pro
%{make}

%install
INSTALL_ROOT=%{buildroot} make install

# icons
for size in 16 22 32 48 64 128
do
    dir="%{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/"
    install -d -m755 $dir
    ln -s "../../../../texmaker/texmaker${size}x${size}.png" "%{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png"
done
install -d -m755 %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
ln -s ../../../../texmaker/texmaker.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -d -m755 %{buildroot}%{_miconsdir}/
ln -s ../../texmaker/texmaker16x16.png %{buildroot}%{_miconsdir}/%{name}.png
ln -s ../texmaker/texmaker32x32.png %{buildroot}%{_iconsdir}/%{name}.png
install -d -m755 %{buildroot}%{_liconsdir}/
ln -s ../../texmaker/texmaker48x48.png %{buildroot}%{_liconsdir}/%{name}.png

install -d -m 755 %{buildroot}%{_docdir}/%{name}/
mv -f %{buildroot}%{_datadir}/texmaker/*.txt %{buildroot}%{_datadir}/texmaker/AUTHORS %{buildroot}%{_datadir}/texmaker/COPYING %{buildroot}%{_docdir}/%{name}/

%find_lang %{name} --with-qt --all-name
%define langfile %{name}.lang

%files %{?langfile:-f %{langfile}}
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.aff
%{_datadir}/%{name}/*.dic
%{_datadir}/%{name}/*.tms
%{_datadir}/%{name}/texmaker.svg
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

