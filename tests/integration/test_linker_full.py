"""Tests for `exercise` package."""

import pytest

from exercise import linker

LINKS_TO_CHECK = [
    ('https://github.com', [
        '#home-community',
        'https://www.facebook.com/GitHub',
    ]),
    ('https://www.esmvaltool.org/gallery.html', [
        'https://docs.esmvaltool.org/en/latest/recipes/recipe_perfmetrics.html',
        './gallery2.html',
        '#top',
    ]),
    ("https://help.ceda.ac.uk/article/280-ftp", [
        'http://archive.ceda.ac.uk',
        'ftp://ftp.ceda.ac.uk/',
        'ftp://anon-ftp.ceda.ac.uk',
    ])
]


@pytest.mark.parametrize(('url', 'expected'), LINKS_TO_CHECK)
def test_get_links(url, expected):
    links = linker.get_links(url)
    print(links)
    for link_expected in expected:
        assert link_expected in links


@pytest.mark.parametrize(('url', 'expected'), LINKS_TO_CHECK)
def test_get_ftp(url, expected):
    links = linker.get_ftp_links(url)
    for link_expected in expected:
        if link_expected.startswith('ftp'):
            assert link_expected in links
        else:
            assert link_expected not in links


@pytest.mark.parametrize(('url', 'expected'), LINKS_TO_CHECK)
def test_get_http(url, expected):
    links = linker.get_http_links(url)
    for link_expected in expected:
        if link_expected.startswith('http'):
            assert link_expected in links
        else:
            assert link_expected not in links
