Summary:	Open ERP - free ERP and CRM software (server)
Summary(pl.UTF-8):	Open ERP - darmowe oprogramowanie ERP i CRM (serwer)
Name:		openerp-server
Version:	5.0.12
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.openerp.com/download/stable/source/%{name}-%{version}.tar.gz
# Source0-md5:	40444cb067d146ab04956913f11d57ff
URL:		http://www.openerp.com/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-psycopg2
BuildRequires:	python-ReportLab
BuildRequires:	python-pychart
BuildRequires:	python-pydot
BuildRequires:	python-lxml
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-psycopg2
Requires:	python-ReportLab
Requires:	python-pychart
Requires:	python-pydot
Requires:	python-mx-DateTime
Requires:	python-lxml
Requires:	python-pytz
Requires:	python-PIL
Requires:	python-vobject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open ERP is a complete ERP and CRM. The main features are accounting
(analytic and financial), stock management, sales and purchases
management, tasks automation, marketing campaigns, help desk, POS,
etc. Technical features include a distributed server, flexible
workflows, an object database, a dynamic GUI, customizable reports,
and SOAP and XML-RPC interfaces.

%description -l pl.UTF-8
Open ERP to pełny ERP i CRM. Główne możliwości to rozliczenia
(analityczne i finansowe), zarządzanie magazynem, zarządzanie
sprzedażą i zakupami, automatyzacja zadań, kampanie reklamowe, help
desk, POS itp. Techniczne możliwości obejmują serwer rozproszony,
elastyczne przepływy prac, obiektową bazę danych, dynamiczne GUI,
konfigurowalne raporty oraz interfejsy SOAP i XML-RPC.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{Changelog,INSTALL}
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{name}
%{_mandir}/man?/*
