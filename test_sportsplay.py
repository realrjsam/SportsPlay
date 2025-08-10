
from main import filter_by_name, filter_by_salary

SAMPLE = [
    {"player":"Patrick Mahomes","team":"KC","years":"10","salary":"45"},
    {"player":"Jalen Hurts","team":"PHI","years":"5","salary":"51"},
    {"player":"Micah Parsons","team":"DAL","years":"4","salary":"32"},
    {"player":"C.J. Stroud","team":"HOU","years":"4","salary":"36"},
]

def assert_equal(actual, expected, msg):
    if actual != expected:
        raise AssertionError(f"{msg}: expected {expected}, got {actual}")

def assert_true(condition, msg):
    if not condition:
        raise AssertionError(msg)

def run_tests():
    print("Running tests...")
    
    # name filter tests
    r = filter_by_name(SAMPLE, "Hurts")
    assert_equal(len(r), 1, "name filter should return 1 for 'Hurts'")
    assert_equal(r[0]["team"], "PHI", "Hurts team should be PHI")

    r = filter_by_name(SAMPLE, "a")  # many names contain 'a'
    assert_true(len(r) >= 2, f"name filter should return multiple when broad, got {len(r)}")

    # salary filter tests
    r = filter_by_salary(SAMPLE, 40)
    names = {c["player"] for c in r}
    expected_names = {"Jalen Hurts", "Patrick Mahomes"}
    assert_true(expected_names.issubset(names), f"salary >40 should include Hurts & Mahomes, got {names}")

    r = filter_by_salary(SAMPLE, 60)
    assert_equal(len(r), 0, "salary >60 should return none")

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
