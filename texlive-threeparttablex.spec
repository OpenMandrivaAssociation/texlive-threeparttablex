# revision 19460
# category Package
# catalog-ctan /macros/latex/contrib/threeparttablex
# catalog-date 2010-07-14 16:29:05 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-threeparttablex
Version:	0.2
Release:	3
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 756837
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719733
- texlive-threeparttablex
- texlive-threeparttablex
- texlive-threeparttablex

