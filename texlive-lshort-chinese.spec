%global tl_name lshort-chinese
%global tl_revision 73160

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.05
Release:	%{tl_revision}.1
Summary:	Introduction to LaTeX, in Chinese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/chinese
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-chinese.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-chinese.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A Chinese edition of the not so short introduction to LaTeX2e, with
additional information of typesetting Chinese language.

