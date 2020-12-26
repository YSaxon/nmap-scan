import pytest

from nmap_scan.Exceptions.LogicException import LogicException
from nmap_scan.Exceptions.NmapConfigurationException import NmapConfigurationException
from nmap_scan.Exceptions.NmapExecutionException import NmapExecutionException
from nmap_scan.Exceptions.NmapNotInstalledException import NmapNotInstalledException
from nmap_scan.Exceptions.NmapPasswordRequiredException import NmapPasswordRequiredException
from nmap_scan.Exceptions.NmapScanMethodUnknownException import NmapScanMethodUnknownException
from nmap_scan.Exceptions.NmapXMLParserException import NmapXMLParserException


@pytest.mark.parametrize(("exception"), [
    LogicException,
    NmapExecutionException,
    NmapNotInstalledException,
    NmapPasswordRequiredException,
    NmapScanMethodUnknownException,
    NmapXMLParserException,
    NmapConfigurationException
])
def test_error_on_missing_required_param(exception):
    with pytest.raises(exception) as excinfo:
        raise exception()
