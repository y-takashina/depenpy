import numpy as np
from pytest import raises, fail

from depynd.information import mutual_information, conditional_mutual_information

X = np.random.multivariate_normal(np.zeros(2), np.eye(2), 10)
x = np.random.normal(0, 1, 10)
y = np.random.normal(0, 1, 20)


class TestMi:
    def test_k(self):
        try:
            mutual_information(X, X, k=1)
            mutual_information(X, X, k=9)
        except:
            fail()
        with raises(AssertionError):
            mutual_information(X, X, k=0)
        with raises(AssertionError):
            mutual_information(X, X, k=10)
        with raises(AssertionError):
            mutual_information(X, X, k=0.1)
        with raises(AssertionError):
            mutual_information(X, X, k=[1])

    def test_length(self):
        with raises(AssertionError):
            mutual_information(x, y)

    def test_dimension(self):
        try:
            mutual_information(x, x)
            mutual_information(x, X)
            mutual_information(X, x)
            mutual_information(X, X)
        except:
            fail()
        assert 0 == mutual_information(x, np.empty([10, 0]))


class TestCmi:
    def test_length(self):
        with raises(AssertionError):
            conditional_mutual_information(x, x, y)
        with raises(AssertionError):
            conditional_mutual_information(x, y, x)
        with raises(AssertionError):
            conditional_mutual_information(y, x, x)

    def test_dimension(self):
        try:
            conditional_mutual_information(X, x, x)
            conditional_mutual_information(x, X, x)
            conditional_mutual_information(x, x, X)
            conditional_mutual_information(X, X, x)
            conditional_mutual_information(x, X, X)
            conditional_mutual_information(X, x, X)
            conditional_mutual_information(X, X, X)
        except:
            fail()
        assert 0 == conditional_mutual_information(np.empty([10, 0]), x, x)
        assert 0 == conditional_mutual_information(x, np.empty([10, 0]), x)
        assert mutual_information(x, x) == conditional_mutual_information(x, x, np.empty([10, 0]))
