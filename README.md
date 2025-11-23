![build workflow](https://github.com/jelaiw/caesar-cipher/actions/workflows/build.yml/badge.svg)
## Overview
A Streamlit app for playing with Caesar ciphers.

## Run the App
Deployed at https://caesar.streamlit.app, with a big TY to Streamlit Community Cloud!

## Demos
Basic flow.

![Demo of basic flow](/assets/caesar-rot3-demo.gif)

## Developers
Perform one-time setup with pipenv for development.
1. Install pipenv.
   * See https://docs.streamlit.io/library/get-started/installation#install-pipenv.
2. `pipenv shell` to activate virtual environment.
3. `pipenv install` to install dependencies from Pipfile to virtual environment.
4. `streamlit run app.py`

NOTE: See workaround for GitHub Codespaces in configuration at `.streamlit/config.toml`.

## References
1. *"Streamlit: The fastest way to build and share data apps"*. Streamlit. https://streamlit.io/.
1. *"Community Cloud: Deploy, manage, and share your apps with the world, directly from Streamlit -- all for free"*. Streamlit. https://streamlit.io/cloud.
