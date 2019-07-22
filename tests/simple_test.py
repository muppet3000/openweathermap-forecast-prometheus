import pytest

def test_error_missing_config():
    with pytest.raises(IOError):
        import main