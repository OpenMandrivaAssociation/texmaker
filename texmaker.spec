Name:            texmaker
Version:         3.5
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
BuildRequires:   qt4-devel >= 4.7
BuildRequires:   pkgconfig(poppler-qt4) 
BuildRequires:   hunspell-devel

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
%{qmake_qt4} texmaker.pro
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

%if %{mdvver} >= 201200
%find_lang %{name} --with-qt --all-name
%define langfile %{name}.lang
%endif

%files %{?langfile:-f %{langfile}}
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.aff
%{_datadir}/%{name}/*.dic
%{_datadir}/%{name}/*.css
%{_datadir}/%{name}/*.js
%{_datadir}/%{name}/texmaker.svg
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%if %{mdvver} <= 201100
%{_datadir}/%{name}/*.qm
%endif


%changelog
* Mon Jul 23 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:3.4.1-1
+ Revision: 810617
- update to 3.4.1

* Fri May 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:3.3.4-1
+ Revision: 800749
- update to 3.3.4

* Mon Apr 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:3.3.3-1
+ Revision: 790019
- update to 3.3.3

* Sun Mar 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:3.3.2-1
+ Revision: 784106
- new version 3.3.2

* Fri Mar 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:3.3.1-1
+ Revision: 781868
- new version 3.3.1

* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:3.2.2-1
+ Revision: 770445
- update to 3.2.2
- specfile cleanup

* Thu Sep 22 2011 Lev Givon <lev@mandriva.org> 1:3.1-1
+ Revision: 700968
- Update to 3.1.

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1:3.0.1-2
+ Revision: 655747
- rebuild for new hunspell

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1:3.0.1-1
+ Revision: 654124
- New version 3.0.1
- add gentoo patch to use system hunspell
- extra en_US dic is not needed, because it defaults to shipped en_GB dict.

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 1:2.2.1-2
+ Revision: 643884
- rebuild to obsolete old packages

* Mon Jan 31 2011 Funda Wang <fwang@mandriva.org> 1:2.2.1-1
+ Revision: 634341
- update to new version 2.2.1

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 1:2.2-1
+ Revision: 633846
- update to new version 2.2

* Wed Oct 27 2010 Lev Givon <lev@mandriva.org> 1:2.1-1mdv2011.0
+ Revision: 589626
- Update to 2.1.

* Tue Aug 31 2010 Lev Givon <lev@mandriva.org> 1:2.0-1mdv2011.0
+ Revision: 574861
- Update to 2.0.
  Update en_US dictionary.

* Fri Feb 19 2010 Lev Givon <lev@mandriva.org> 1:1.9.9-2mdv2010.1
+ Revision: 508359
- Add en_US dictionary (#40598).

* Tue Feb 02 2010 Funda Wang <fwang@mandriva.org> 1:1.9.9-1mdv2010.1
+ Revision: 499566
- New version 1.9.9

* Tue Jun 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.9.2-1mdv2010.0
+ Revision: 391090
- update to new version 1.9.2

* Sun May 24 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.9.1-1mdv2010.0
+ Revision: 379198
- update to new version 1.9.1

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.9-1mdv2010.0
+ Revision: 378397
- Update to new version 1.9

* Wed Nov 05 2008 David Walluck <walluck@mandriva.org> 1:1.8-1mdv2009.1
+ Revision: 300031
- 1.8

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:1.7.1-2mdv2009.0
+ Revision: 269424
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 1:1.7.1-1mdv2009.0
+ Revision: 200675
- New version 1.7.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 25 2007 Funda Wang <fwang@mandriva.org> 1:1.6-2mdv2008.0
+ Revision: 71117
- BR desktop-file-utils
- fix invalid desktop file

* Thu Jun 21 2007 David Walluck <walluck@mandriva.org> 1:1.6-1mdv2008.0
+ Revision: 42159
- 1.6
- use full source URL

* Thu May 10 2007 Austin Acton <austin@mandriva.org> 1:1.5-2mdv2008.0
+ Revision: 26094
- install docs where it can find them

* Wed May 09 2007 Austin Acton <austin@mandriva.org> 1:1.5-1mdv2008.0
+ Revision: 25770
- requires aspell
- epoch 1
- new version
- use qt4, drop KDE dependency
- force build flags
- XDG menu, FD.o icons (cookies!!)


* Mon Jun 26 2006 Pascal Terjan <pterjan@mandriva.org> 1.12-2mdv2007.0
- fix qtdir and path to the lib on x86_64
- mkrel

* Thu Apr 28 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.12-1mdk
- 1.12

* Wed Jun 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.1-3mdk
- rebuild

* Wed Feb 11 2004 David Baudens <baudens@mandrakesoft.com> 1.0.1-2mdk
- Fix menu

* Tue Aug 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Sun Jul 20 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-3mdk
- fix menu section (David Coe <david.coe@dsl.pipex.com>)

* Sat Jul 19 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-2mdk
- buildrequires kdelibs-devel

* Fri Jul 18 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-1mdk
- 1st mdk contrib (Thanks to war[sheep] to notify me this tools)

