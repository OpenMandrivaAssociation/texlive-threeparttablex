# revision 19460
# category Package
# catalog-ctan /macros/latex/contrib/threeparttablex
# catalog-date 2010-07-14 16:29:05 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-threeparttablex
Version:	0.2
Release:	1
Summary:	Notes in longtables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/threeparttablex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttablex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttablex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the functionality of the threeparttable
package to tables created using the longtable package.

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
%{_texmfdistdir}/tex/latex/threeparttablex/threeparttablex.sty
%doc %{_texmfdistdir}/doc/latex/threeparttablex/README
%doc %{_texmfdistdir}/doc/latex/threeparttablex/threeparttablex.pdf
%doc %{_texmfdistdir}/doc/latex/threeparttablex/threeparttablex.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
