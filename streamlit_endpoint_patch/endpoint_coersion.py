# This patch forcibly reverts the new `_stcore/stream` (and friends) endpoints to the
# original `/stream` (and friends) endpoints, so that reverse proxy environments will
# continue to work without config overhaul (i.e. corporate bureaucracy overload).
import os
import shutil

def main():
    # Check that target streamlit exists
    try:
        import streamlit as st
    except ImportError as e:
        raise Exception('Must have streamlit installed') from e
    assert st.__version__ >= '1.18.0', 'Streamlit version must be >=1.18.0'

    replace_pairs = [
        ('_stcore/script-health-check', 'script-health-check'),
        ('_stcore/stream', 'stream'),
        ('_stcore/metrics', 'metrics'),
        ('_stcore/message', 'message'),
        ('_stcore/health', 'health'),
        ('_stcore/allowed-message-origins', 'allowed-message-origins'),
        ('_stcore/upload_file', 'upload_file'),
    ]

    # Replace _stcore endpoint names wherever they are found..
    from streamlit.web.server import routes
    from streamlit.web.server import server
    from streamlit.web.server import stats_request_handler
    from streamlit.web.server import upload_file_request_handler
    python_targets = [
        routes,
        server,
        stats_request_handler,
        upload_file_request_handler
    ]

    for python_file in python_targets:
        replace_str_in_file(python_file.__file__, replace_pairs)
    
    js_targets = [
        os.path.join(
            os.path.dirname(st.__file__),
            'static/static/js/main.1d359564.js'
        )
    ]

    for js_file in js_targets:
        replace_str_in_file(js_file, replace_pairs)
    
    print('All done')

def replace_str_in_file(filepath, find_replace_pairs):
    # Backup first
    bk_filepath = f'{filepath}.bk'
    if not os.path.isfile(bk_filepath):
        shutil.copy2(filepath, bk_filepath)

    with open(filepath, 'r') as f:
        py_code = f.read()
    
    for find, replace in find_replace_pairs:
        py_code = py_code.replace(find, replace)
    
    with open(filepath, 'w') as f:
        f.write(py_code)
    

if __name__ == '__main__':
    main()