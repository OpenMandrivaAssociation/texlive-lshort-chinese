Name:		texlive-lshort-chinese
Version:	67025
Release:	1
Summary:	Introduction to LaTeX, in Chinese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/chinese
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-chinese.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-chinese.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A translation to Chinese of the not so short introduction to
LaTeX2e, presented by the Chinese TeX Society CTeX. The
processed output is created by use of XeTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-chinese

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
