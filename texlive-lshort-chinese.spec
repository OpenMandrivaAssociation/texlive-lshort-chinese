# revision 15878
# category Package
# catalog-ctan /info/lshort/chinese
# catalog-date 2008-07-16 16:26:02 +0200
# catalog-license gpl
# catalog-version 4.20
Name:		texlive-lshort-chinese
Version:	4.20
Release:	1
Summary:	Introduction to LaTeX, in Chinese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/chinese
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-chinese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-chinese.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A translation to Chinese of the not so short introduction to
LaTeX2e, presented by the Chinese TeX Society CTeX. The
processed output is created by use of XeTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/README
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/lshort-zh-cn.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/fancyhea.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/lshort-a5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/lshort-base.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/lshort.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/lshort.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/myclass.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/test.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/typeset.tex
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/usefulmacros.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/zhfont.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/zhmath.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/zhspacing.sty
%doc %{_texmfdistdir}/doc/latex/lshort-chinese/src/zhulem.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
