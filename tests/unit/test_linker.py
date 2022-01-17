#!/usr/bin/env python
"""Tests for `exercise` package."""

from datetime import datetime, timedelta

import mock
import pytest

from exercise import linker

SAMPLE_LINKS = [
    'https://awesome.web', 'ftp://awesome.data', '#awesome', '/internallink',
    '', None
]

LINKS_CACHE = SAMPLE_LINKS[0:-2]
SAMPLE_CACHE = {'anyweb.can.do': {'links': LINKS_CACHE}}
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
    assert set(links) == set(SAMPLE_LINKS[0:-2])


@mock.patch('exercise.linker._get_html')
@mock.patch('exercise.linker._get_all_links')
def test_get_links_fills_cache(mock_links, mock_html):
    mock_links.return_value = SAMPLE_LINKS
    cache = dict()
    links = linker.get_links('anyweb.can.do', cache=cache)
    data = cache['anyweb.can.do']
    assert data['links'] == links
    assert datetime.utcnow() - data['time'] < timedelta(milliseconds=100)


def test_get_links_using_cache():
    links = linker.get_links('anyweb.can.do', cache=SAMPLE_CACHE)
    assert set(links) == set(LINKS_CACHE)


@mock.patch('exercise.linker._get_html')
@mock.patch('exercise.linker._get_all_links')
@pytest.mark.parametrize(('filter', 'expected'), SAMPLE_TYPES)
def test_get_links_filtered(mock_links, mock_html, filter, expected):
    mock_links.return_value = SAMPLE_LINKS
    links = linker.get_links('anyweb.can.do', link_type=filter)
    assert links == expected


@pytest.mark.parametrize(('filter', 'expected'), SAMPLE_TYPES)
def test_get_links_filtered_cache(filter, expected):
    links = linker.get_links('anyweb.can.do',
                             cache=SAMPLE_CACHE,
                             link_type=filter)
    assert links == expected


@mock.patch('exercise.linker.get_links')
def test_get_ftp(mock_links):
    linker.get_ftp_links('anyweb.can.do')
    mock_links.assert_called_once_with(
        'anyweb.can.do',
        cache=None,
        link_type='ftp',
    )


@mock.patch('exercise.linker.get_links')
def test_get_http(mock_links):
    linker.get_http_links('anyweb.can.do')
    mock_links.assert_called_once_with(
        'anyweb.can.do',
        cache=None,
        link_type='http',
    )
