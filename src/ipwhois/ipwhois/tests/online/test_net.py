import logging
from ipwhois.tests import TestCommon
from ipwhois.exceptions import (ASNLookupError, ASNRegistryError,
                                BlacklistError, WhoisLookupError,
                                HTTPLookupError, HostLookupError)
from ipwhois.net import Net

LOG_FORMAT = ('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] '
              '[%(funcName)s()] %(message)s')
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
log = logging.getLogger(__name__)


class TestNet(TestCommon):

    def test_lookup_asn(self):
        # TODO: keep until deprecated lookup is removed, for coverage
        net = Net('74.125.225.229')
        try:
            self.assertIsInstance(net.lookup_asn(), tuple)
        except HTTPLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

    def test_get_asn_dns(self):
        result = Net('74.125.225.229')
        try:
            self.assertIsInstance(result.get_asn_dns(), list)
        except ASNLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        result.dns_zone = 'a'
        self.assertRaises(ASNLookupError, result.get_asn_dns)

    def test_get_asn_verbose_dns(self):
        result = Net('74.125.225.229')
        try:
            self.assertIsInstance(result.get_asn_verbose_dns(asn='15169'), str)
        except ASNLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        self.assertRaises(ASNLookupError, result.get_asn_verbose_dns, **dict(
            asn='a'
        ))

    def test_get_asn_whois(self):
        result = Net('74.125.225.229')
        try:
            self.assertIsInstance(result.get_asn_whois(), str)
        except ASNLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

    def test_get_asn_http(self):
        result = Net('74.125.225.229')
        try:
            self.assertIsInstance(result.get_asn_http(), dict)
        except ASNLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

    def test_get_whois(self):
        result = Net('74.125.225.229')
        try:
            self.assertIsInstance(result.get_whois(), str)
        except WhoisLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        self.assertRaises(WhoisLookupError, result.get_whois, **dict(
            retry_count=0, server='arin.net'))

        self.assertRaises(BlacklistError, result.get_whois, **dict(
            server='whois.arin.net', extra_blacklist=['whois.arin.net']))

        result = Net(address='74.125.225.229', timeout=0)
        self.assertRaises(WhoisLookupError, result.get_whois, **dict(
            retry_count=1))

    def test_get_asn_origin_whois(self):
        # IP doesn't matter here
        result = Net('74.125.225.229')

        try:
            self.assertIsInstance(result.get_asn_origin_whois(
                asn='AS15169'), str)
        except WhoisLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        self.assertRaises(WhoisLookupError, result.get_asn_origin_whois,
                          **dict(asn='AS15169', retry_count=0,
                                 server='radb.net'))

        # IP doesn't matter here
        result = Net(address='74.125.225.229', timeout=0)
        self.assertRaises(WhoisLookupError, result.get_asn_origin_whois,
                          **dict(asn='AS15169', retry_count=1))

    def test_get_http_json(self):
        from ipwhois.rdap import RIR_RDAP
        result = Net('74.125.225.229')
        try:
            self.assertIsInstance(result.get_http_json(
                RIR_RDAP['arin']['ip_url'].format('74.125.225.229')), dict)
        except HTTPLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        self.assertRaises(HTTPLookupError, result.get_http_json, **dict(
            url='http://255.255.255.255', retry_count=1))

        result = Net(address='74.125.225.229', timeout=0)
        url = RIR_RDAP['arin']['ip_url'].format('74.125.225.229')
        self.assertRaises(HTTPLookupError, result.get_http_json, **dict(
            url=url, retry_count=0))

    def test_get_host(self):
        ips = [
            '74.125.225.229',  # ARIN
            '2001:4860:4860::8888'
        ]

        for ip in ips:
            result = Net(ip)
            try:
                self.assertIsInstance(result.get_host(0), tuple)
            except HostLookupError:
                pass
            except AssertionError as e:
                raise e
            except Exception as e:
                self.fail('Unexpected exception raised: {0}'.format(e))

        result = Net('74.125.225.229', 0)
        self.assertRaises(HostLookupError, result.get_host, **dict(
            retry_count=1))

    def test_get_http_raw(self):
        from ipwhois.nir import NIR_WHOIS

        # GET
        result = Net('133.1.2.5')
        try:
            self.assertIsInstance(result.get_http_raw(
                NIR_WHOIS['jpnic']['url'].format('133.1.2.5')), str)
        except HTTPLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        # POST
        result = Net('115.1.2.3')
        try:
            self.assertIsInstance(result.get_http_raw(
                url=NIR_WHOIS['krnic']['url'].format('115.1.2.3'),
                request_type=NIR_WHOIS['krnic']['request_type'],
                form_data={
                    NIR_WHOIS['krnic']['form_data_ip_field']: '115.1.2.3'
                }
            ), str)
        except HTTPLookupError:
            pass
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail('Unexpected exception raised: {0}'.format(e))

        self.assertRaises(HTTPLookupError, result.get_http_raw, **dict(
            url='http://255.255.255.255', retry_count=1))

        result = Net(address='133.1.2.5', timeout=0)
        url = NIR_WHOIS['jpnic']['url'].format('133.1.2.5')
        self.assertRaises(HTTPLookupError, result.get_http_raw, **dict(
            url=url, retry_count=0))
