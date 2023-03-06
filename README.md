# streamlit-endpoint-patch
Since `streamlit 1.18.0`, original endpoint names were migrated to new ones under `_stcore` (e.g. `_stcore/stream`) and this breaks some systems, espeically those behind reverse proxies or arrangements with forwarding rules that you cannot change in a heartbeat.

This repo contains a very dirty monkey patch that forces [streamlit](https://github.com/streamlit/streamlit) to use the old endpoints of `/stream` (and friends like `/health`).

⚠️This is an unofficial patch and not approved by Streamlit developers. In the long run you should work to get the new endpoints working, and use this temporary solution at your own risk!⚠️

Last tested with `streamlit 1.19.0`.

### Install
```
pip install streamlit-endpoint-patch
```

### Usage
2 methods.

#### Method 1 (through pypi):
1. Install package once
```
pip install streamlit-endpoint-patch
```

2. Execute the following in your virtualenv/pyenv/whatever
```
streamlit-endpoint-patch
```

#### Method 2 (copy-paste):

1. Copy `streamlit_endpoint_patch/endpoint_coersion.py` to where you see fit
2. Activate virtualenv if you have one
3. Execute the following in your virtualenv/pyenv/whatever
```bash
python streamlit_endpoint_patch/endpoint_coersion.py  # or wherever you put the .py
```

## Reverting to original streamlit
```bash
pip install streamlit=<your version>
```