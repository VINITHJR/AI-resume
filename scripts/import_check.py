import sys
import os
import streamlit as st

# ensure workspace root is on sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

st.title("Dependency and Module Import Checker")

# Check for sklearn instead of rank_bm25
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np
    st.success('sklearn OK')
except ImportError:
    st.error('sklearn not available')

# Check for keyword_utils
try:
    import keyword_utils
    st.success('keyword_utils OK')
except ImportError as e:
    st.error(f'keyword_utils import error: {e}')

# Check for other essential packages
try:
    import google.generativeai as genai
    st.success('google-generativeai OK')
except ImportError:
    st.warning('google-generativeai not available')

try:
    import streamlit
    st.success('streamlit OK')
except ImportError:
    st.error('streamlit not available')

st.info('Import check completed!')
