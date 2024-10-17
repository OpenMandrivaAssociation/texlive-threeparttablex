Name:		texlive-threeparttablex
Version:	34206
Release:	2
Summary:	Notes in longtables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/threeparttablex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttablex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/threeparttablex.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
