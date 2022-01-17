import os
from datetime import datetime

from exercise import linker


def test_purge_cache():
    links_cache = {
        'old': {
            'time': datetime(1900, 1, 1)
        },
        'new': {
            'time': datetime.utcnow()
        },
    }
    linker.purge_cache(links_cache)
    assert 'old' not in links_cache
    assert 'new' in links_cache


def test_save_cache(tmpdir):
    path = os.path.join(tmpdir, 'cache.yml')
    links_cache = {
        'old': {
            'time': datetime(1900, 1, 1)
        },
        'new': {
            'time': datetime.utcnow()
        },
    }
    linker.save_cache(links_cache, path)
    loaded_cache = linker.load_cache(path)
    assert loaded_cache == links_cache
