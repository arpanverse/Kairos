from sentence_transformers import SentenceTransformer
import pytest

@pytest.fixture(scope='session')
def sentence_transformer():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    yield model
    model.__del__()