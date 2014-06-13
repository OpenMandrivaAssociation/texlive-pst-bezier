# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-bezier
# catalog-date 2009-02-01 17:37:35 +0100
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-pst-bezier
Version:	0.01
Release:	7
Summary:	Draw Bezier curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bezier
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bezier.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bezier.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bezier.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a macro \psbcurve for drawing a Bezier
curve. Provision is made for full control of over all the
control points of the curve.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-bezier/pst-bezier.pro
%{_texmfdistdir}/tex/generic/pst-bezier/pst-bezier.tex
%{_texmfdistdir}/tex/latex/pst-bezier/pst-bezier.sty
%doc %{_texmfdistdir}/doc/generic/pst-bezier/Changes
%doc %{_texmfdistdir}/doc/generic/pst-bezier/README
%doc %{_texmfdistdir}/doc/generic/pst-bezier/pst-bezier-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-bezier/pst-bezier-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-bezier/pst-bezier-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-bezier/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.01-2
+ Revision: 755222
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.01-1
+ Revision: 719335
- texlive-pst-bezier
- texlive-pst-bezier
- texlive-pst-bezier
- texlive-pst-bezier

