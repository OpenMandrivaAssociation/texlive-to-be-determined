Name:		texlive-to-be-determined
Version:	64882
Release:	2
Summary:	Highlight text passages that need further work
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/to-be-determined
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/to-be-determined.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/to-be-determined.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/to-be-determined.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a single command \tbd which highlights
the pieces of text that need to be rewritten later. You can
hide them all with a single package option hide, or just make
them disappear entirely with the option off.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/to-be-determined
%{_texmfdistdir}/tex/latex/to-be-determined
%doc %{_texmfdistdir}/doc/latex/to-be-determined

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
