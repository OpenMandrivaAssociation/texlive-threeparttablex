# revision 31276
# category Package
# catalog-ctan /macros/latex/contrib/threeparttablex
# catalog-date 2013-07-23 11:01:18 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-threeparttablex
Version:	0.3
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

%description
The package provides the functionality of the threeparttable
package to tables created using the longtable package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/threeparttablex/threeparttablex.sty
%doc %{_texmfdistdir}/doc/latex/threeparttablex/README
%doc %{_texmfdistdir}/doc/latex/threeparttablex/threeparttablex.pdf
%doc %{_texmfdistdir}/doc/latex/threeparttablex/threeparttablex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
