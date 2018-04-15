#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http:#www.gnu.org/licenses/.
#

import unittest

import scipy.constants as scc

from smile.algorithms.tdoa import *

# Test scenarios contains following information
# - Anchors' coordinates in 2D
# - True tag position in 2D
# - True differences in distances between tag and Anchors no. 2 and 3 relative to distance between tag and Anchor no.1


def generate_scenario_data(mobile_position):
    coordinates = np.asarray(((0, 0),  # Anchor 1
                              (10, 0),  # Anchor 2
                              (10, 10)))  # Anchor 3

    distances = np.asarray((np.abs(np.linalg.norm(mobile_position - coordinates[0, :])),
                            np.abs(np.linalg.norm(mobile_position - coordinates[1, :])),
                            np.abs(np.linalg.norm(mobile_position - coordinates[2, :]))))

    distances -= distances[0]

    return coordinates, distances, mobile_position


def scenario_1():
    return generate_scenario_data((6, 4))


def scenario_2():
    return generate_scenario_data((5, 5))


def scenario_3():
    return generate_scenario_data((7, 6))


def scenario_4():
    return generate_scenario_data((8, 2))


class TestDoanVesely(unittest.TestCase):
    def test_scenario_1(self):
        coordinates, distances, true_mobile_position = scenario_1()
        position = doan_vesely(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)

    def test_scenario_2(self):
        coordinates, distances, true_mobile_position = scenario_2()
        position = doan_vesely(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)

    def test_scenario_3(self):
        coordinates, distances, true_mobile_position = scenario_3()
        position = doan_vesely(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)

    def test_scenario_4(self):
        coordinates, distances, true_mobile_position = scenario_4()
        position = doan_vesely(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)


class TestFang(unittest.TestCase):
    def test_scenario_1(self):
        coordinates, distances, true_mobile_position = scenario_1()
        position = fang(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)

    # Scenario no. 2 doesn't apply to Fang algorithm

    def test_scenario_3(self):
        coordinates, distances, true_mobile_position = scenario_3()
        position = fang(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)

    def test_scenario_4(self):
        coordinates, distances, true_mobile_position = scenario_4()
        position = fang(coordinates, distances)
        np.testing.assert_almost_equal(position, true_mobile_position, decimal=7)


if __name__ == '__main__':
    unittest.main()
