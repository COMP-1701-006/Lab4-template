import pytest
import io

def test_add_ingredient(import_ingredients):
    out = import_ingredients.add_ingredient("flour", "200")
    assert out is not None
    assert "200" in out
    assert "flour" in out

def test_area(import_cooking_time):
    assert import_cooking_time.area(6) == pytest.approx(28.274333882308138)
    assert import_cooking_time.area(10) == pytest.approx(78.53981633974483)

def test_cake_time(import_cooking_time):
    assert import_cooking_time.cake_time(350, 6) == 20
    assert import_cooking_time.cake_time(350, 10) == 45
    assert import_cooking_time.cake_time(400, 11.5) == 55
    assert import_cooking_time.cake_time(400, 8.5) == 30

def test_prompts(import_cooking_time, monkeypatch, capsys):
    inputs = io.StringIO("350\n9\n")
    monkeypatch.setattr("sys.stdin", inputs)
    import_cooking_time.main()
    out, _ = capsys.readouterr()
    assert "300" in out
    assert "450" in out
    assert "6" in out
    assert "12" in out

@pytest.fixture
def import_ingredients(monkeypatch):
    try:
        inputs = io.StringIO("flour\n200\n")
        monkeypatch.setattr("sys.stdin", inputs)
        import ingredients
        return ingredients
    except ImportError as e:
        assert False, "ingredients.py not found, check your file paths"

@pytest.fixture
def import_cooking_time(monkeypatch):
    try:
        inputs = io.StringIO("350\n9\n")
        monkeypatch.setattr("sys.stdin", inputs)
        import cooking_time
        return cooking_time
    except ImportError as e:
        assert False, "cooking_time.py not found, check your file paths"