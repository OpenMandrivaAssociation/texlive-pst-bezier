# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-bezier
# catalog-date 2009-02-01 17:37:35 +0100
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-pst-bezier
Version:	0.01
Release:	1
Summary:	Draw Bezier curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bezier
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bezier.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bezier.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bezier.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a macro \psbcurve for drawing a Bezier
curve. Provision is made for full control of over all the
control points of the curve.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
