# -*- coding: utf-8 -*-

from opinel.utils.fs import *
from opinel.utils.console import configPrintException

class TestOpinelFsClass:
    """
    Test opinel.fs
    """

    def cmp(self, a, b):
        """
        Implement cmp() for Python3 tests
        """
        return (a > b) - (a < b)

    def test_CustomJSONEncoder(self):
        pass

    def test_load_data(self):
        test = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/protocols.json')
        load_data(test, local_file=True)
        load_data(test, 'protocols', local_file=True)
        load_data('protocols.json', 'protocols')
        load_data('ip-ranges.json', 'prefixes')
        load_data('tests/data/protocols.json', 'protocols', local_file=True)
        test = load_data('protocols.json', 'protocols')
        assert type(test) == dict
        assert test['1'] == 'ICMP'
        test = load_data('tests/data/protocols.json', 'protocols', True)
        assert type(test) == dict
        assert test['-2'] == 'TEST'


    def test_read_default_args(self):
        pass


    def test_read_ip_ranges(self):
        read_ip_ranges('ip-ranges.json', local_file=False)
        read_ip_ranges('tests/data/ip-ranges-1.json', local_file=True)
        read_ip_ranges('tests/data/ip-ranges-1.json', local_file=True, ip_only=True)
        successful_read_ip_ranges_runs = True
        test_cases = [
         {'filename': 'tests/data/ip-ranges-1.json',
            'local_file': True,
            'conditions': [],'ip_only': False,
            'results': 'tests/results/read_ip_ranges/ip-ranges-1a.json'
            },
         {'filename': 'tests/data/ip-ranges-1.json',
            'local_file': True,
            'conditions': [],'ip_only': True,
            'results': 'tests/results/read_ip_ranges/ip-ranges-1b.json'
            },
         {'filename': 'tests/data/ip-ranges-1.json',
            'local_file': True,
            'conditions': [
                         [
                          'field_a', 'equal', 'a1']],
            'ip_only': True,
            'results': 'tests/results/read_ip_ranges/ip-ranges-1c.json'
            },
         {'filename': 'ip-ranges.json',
            'local_file': False,
            'conditions': [
                         [
                          'ip_prefix', 'equal', '23.20.0.0/14']],
            'ip_only': False,
            'results': 'tests/results/read_ip_ranges/ip-ranges-a.json'
            }]
        for test_case in test_cases:
            results = test_case.pop('results')
            test_results = read_ip_ranges(**test_case)
            known_results = load_data(results, local_file=True)
            if self.cmp(test_results, known_results) != 0:
                successful_read_ip_ranges_runs = False

        assert successful_read_ip_ranges_runs

    def test_save_blob_as_json(self):
        configPrintException(True)
        date = datetime.datetime.now()
        save_blob_as_json('tmp1.json', {'foo': 'bar','date': date}, True, False)
        save_blob_as_json('tmp1.json', {'foo': 'bar'}, True, True)
        save_blob_as_json('/root/tmp1.json', {'foo': 'bar'}, True, True)

    def test_save_ip_ranges(self):
        if os.path.isfile('ip-ranges-default.json'):
            os.remove('ip-ranges-default.json')
        save_ip_ranges('default', {'a': 'b'}, False, False)
        save_ip_ranges('default', {'a': 'b'}, True, True)