from environment.uncertainty import StochasticBlockages


def test_blockage_probability_bounds():
    model = StochasticBlockages(0.5)

    for _ in range(100):
        result = model.is_blocked()
        assert result in [True, False]
