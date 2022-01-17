#!/usr/bin/env python
"""Tests for `exercise` package."""

import mock
import pytest

from exercise import linker

SAMPLE_LINKS = [
    'https://awesome.web', 'ftp://awesome.data', '#awesome', '/internallink',
    '', None
]

SAMPLE_TYPES = [
    ('http', ['https://awesome.web']),
    ('https', ['https://awesome.web']),
    ('ftp', ['ftp://awesome.data']),
    ('#', ['#awesome']),
    ('unkwnown', []),
]


@mock.patch('exercise.linker._get_html')
@mock.patch('exercise.linker._get_all_links')
def test_get_links(mock_links, mock_html):
    mock_links.return_value = SAMPLE_LINKS
    links = linker.get_links('anyweb.can.do')
    assert (set(links) & set(SAMPLE_LINKS)) == set(SAMPLE_LINKS[0:-2])


@mock.patch('exercise.linker._get_html')
@mock.patch('exercise.linker._get_all_links')
@pytest.mark.parametrize(('filter', 'expected'), SAMPLE_TYPES)
def test_get_links_filtered(mock_links, mock_html, filter, expected):
    mock_links.return_value = SAMPLE_LINKS
    links = linker.get_links('anyweb.can.do', link_type=filter)
    print(links)
    print(expected)
    assert links == expected


@mock.patch('exercise.linker.get_links')
def test_get_ftp(mock_links):
    linker.get_ftp_links('anyweb.can.do')
    mock_links.assert_called_once_with(
        'anyweb.can.do',
        link_type='ftp',
    )


@mock.patch('exercise.linker.get_links')
def test_get_http(mock_links):
    linker.get_http_links('anyweb.can.do')
    mock_links.assert_called_once_with(
        'anyweb.can.do',
        link_type='http',
    )
