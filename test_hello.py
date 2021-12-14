from click.testing import CliRunner
from hello import marco


def test_marco():
    assert "Polo" == marco("Marco")

def test_not_marco():
    assert "No!" == marco("Bobo")

