from genesis.core.genesis import generate_map
from genesis.core.vis import chunk

def test_chunk():
    noise = generate_map(100) 
    chunks = [c for c in chunk(noise, (0,0, 10, 10))]
    assert len(chunks) == 100
