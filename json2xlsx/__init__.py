# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__VERSION__ = __version__

import sys, os
import json
import xlsxwriter
import types

import unittest

def resolve_format(formats, format):
    if isinstance(format, dict):
        return format

    elif isinstance(format, str) or isinstance(format, unicode):
        return resolve_format(formats, formats[format])

    elif isinstance(format, list):
        result = dict()
        for sub_format in format:
            result.update(resolve_format(formats, sub_format))

        return  result

    else:
        raise TypeError("can not handle format for %s ('%s')" % (type(format), repr(format)))


def write(filename, data):

    format_definitions = {}
    if 'formats' in data:
        format_definitions = data['formats']

    wb = xlsxwriter.Workbook(filename)
    cell_formats = {}

    for ws_data in data['worksheets']:

        ws = wb.add_worksheet(ws_data['name'])
        if 'columns' in ws_data:
            for column in ws_data['columns']:
                print repr(column)
                ws.set_column(column['x'], column['x'], column['width'])
            
        if 'rows' in ws_data:
            for row in ws_data['rows']:
                ws.set_row(column['y'], column['height'])
            
        if 'cells' in ws_data:
            for cell in ws_data['cells']:

                cell_format = None
                if u'format' in cell:
                    format = cell['format']

                    format = resolve_format(format_definitions, format)
                    format_hash = repr(format)
                    if not format_hash in cell_formats:
                        cell_format = wb.add_format(format);
                        cell_formats[format_hash] = cell_format
                    else:
                        cell_format = cell_formats[format_hash]

                ws.write(cell['y'], cell['x'], cell['value'], cell_format)

    wb.close()
    return True


class TestWriteXLSXFile(unittest.TestCase):
    """
    Unit tests

    """

    def test_write_xlsx_file(self):
        """Test writing an XLXS File."""
        
        test_data = {
            'worksheets': [
                {
                    'name': 'sheet1',
                    'cells': [
                        {'x': 0, 'y': 0, 'value': 12},
                        {'x': 1, 'y': 0, 'value': 12},
                        {'x': 2, 'y': 0, 'value': '=A1+B1'},
                    ]
                }
            ]
        }

        got = write('test.xlsx', test_data)
        self.assertTrue(got)


    def test_resolve_format1(self):
        """Test resolve_format."""

        got = resolve_format({'bold': {'bold': True }}, 'bold')
        self.assertEqual(got, {'bold': True})


    def test_resolve_format_error(self):
        """Test resolve_format."""

        self.assertRaises(TypeError, resolve_format, False)

    


if __name__ == '__main__':
    unittest.main()


