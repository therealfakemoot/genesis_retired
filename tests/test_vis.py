from genesis.core.genesis import generate_map
from genesis.core.vis import chunk

def test_chunk_len():
    noise = generate_map(100) 
    chunks = [c for c in chunk(noise, (0,0, 10, 10))]
    assert len(chunks) == 100

def test_chunk_shape():
    noise = generate_map(100) 
    c = chunk(noise, (0,0, 10, 10)).next()
    assert c.shape == (10,10)
