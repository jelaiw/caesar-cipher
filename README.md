![build workflow](https://github.com/jelaiw/caesar-cipher/actions/workflows/build.yml/badge.svg)
## Overview
A Streamlit app for playing with Caesar ciphers.

## Run the App
Deployed at https://caesar.streamlit.app, with a big TY to Streamlit Community Cloud!

## Demos
Basic flow.

![Demo of basic flow](/assets/caesar-rot3-demo.gif)

## Developers
Set up something like the following:
1. Install Pipenv.
   * See https://docs.streamlit.io/library/get-started/installation#install-pipenv.
2. `pipenv shell` to activate virtual environment.
3. `pipenv install` to install dependencies from Pipfile to virtual environment.
4. `streamlit run app.py`

NOTE: _Streamlit's install docs no longer prescribe Pipenv (above link anchor is gone too), but leaving above instructions intact as it still works to quickly get me started on GitHub Codespaces_.

Run unit tests like this:
```sh
$ pytest
================================================================== test session starts ===================================================================
platform linux -- Python 3.12.1, pytest-9.0.1, pluggy-1.6.0
rootdir: /workspaces/caesar-cipher
plugins: anyio-4.11.0
collected 18 items                                                                                                                                       

test_caesar.py .............                                                                                                                       [ 72%]
test_textutil.py .....                                                                                                                             [100%]

=================================================================== 18 passed in 0.03s ===================================================================
```

## References
1. *"Streamlit: The fastest way to build and share data apps"*. Streamlit. https://streamlit.io/.
1. *"Community Cloud: Deploy, manage, and share your apps with the world, directly from Streamlit -- all for free"*. Streamlit. https://streamlit.io/cloud.
