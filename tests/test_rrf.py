from retrieval.rrf import ReciprocalRankFusion


def test_rrf_empty():

    rrf = ReciprocalRankFusion()

    results = rrf.fuse([], [])

    assert results == []
