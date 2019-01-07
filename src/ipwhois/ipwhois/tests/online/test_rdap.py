import json
import io
from os import path
import logging
from ipwhois.tests import TestCommon
from ipwhois.exceptions import (HTTPLookupError, HTTPRateLimitError)
from ipwhois.rdap import (RDAP, Net)

LOG_FORMAT = ('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] '
              '[%(funcName)s()] %(message)s')
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
log = logging.getLogger(__name__)


class TestRDAP(TestCommon):

    def test_lookup(self):

        data_dir = path.abspath(path.join(path.dirname(__file__), '..'))

        with io.open(str(data_dir) + '/rdap.json', 'r') as data_file:
            data = json.load(data_file)

        for key, val in data.items():

            log.debug('Testing: {0}'.format(key))
            net = Net(key)
            obj = RDAP(net)

            try:

                self.assertIsInstance(obj.lookup(asn_data=val['asn_data'],
                                                 depth=1), dict)

            except (HTTPLookupError, HTTPRateLimitError):

                pass

            except AssertionError as e:

                raise e

            except Exception as e:

                self.fail('Unexpected exception raised: {0}'.format(e))

        for key, val in data.items():

            log.debug('Testing bootstrap and raw: {0}'.format(key))
            net = Net(key)
            obj = RDAP(net)

            try:

                self.assertIsInstance(obj.lookup(asn_data=val['asn_data'],
                                                 depth=3,
                                                 bootstrap=True,
                                                 inc_raw=True), dict)

            except (HTTPLookupError, HTTPRateLimitError):

                pass

            except AssertionError as e:

                raise e

            except Exception as e:

                self.fail('Unexpected exception raised: {0}'.format(e))
