from main import filter_by_name, filter_by_salary

SAMPLE = [
    {"player":"Patrick Mahomes","team":"KC","years":10,"salary":45.0},
    {"player":"Jalen Hurts","team":"PHI","years":5,"salary":51.0},
    {"player":"Micah Parsons","team":"DAL","years":4,"salary":30.0},
    {"player":"C.J. Stroud","team":"HOU","years":4,"salary":36.0},
]

def assert_equal(a, b, msg):
    if a != b:
        raise AssertionError(msg)

def run_tests():
    # name filter
    r = filter_by_name(SAMPLE, "Hurts")
    assert_equal(len(r), 1, "name filter should return 1")
    assert_equal(r[0]["team"], "PHI", "Hurts team should be PHI")

    r = filter_by_name(SAMPLE, "a")  # many names contain 'a'
    assert_equal(len(r) >= 2, "name filter should return multiple when broad")

    # salary filter
    r = filter_by_salary(SAMPLE, 40)
    names = {c["player"] for c in r}
    assert_equal({"Jalen Hurts","Patrick Mahomes"}.issubset(names), "salary >40 should include Hurts & Mahomes")

    r = filter_by_salary(SAMPLE, 60)
    assert_equal(len(r), 0, "salary >60 should return none")

    print("All tests passed")

if __name__ == "__main__":
    run_tests()