import unittest

import hep_ml.reweight
import numpy as np
import pandas as pd

import lhcb_paper_2017_044


class LHCbPAPER2017044TestCase(unittest.TestCase):
    """Test cases for the lhcb_paper_2017_044 module."""
    def test_data(self):
        """The data should be loaded as a pandas.DataFrame."""
        a, b = lhcb_paper_2017_044.data()
        for data in [a, b]:
            self.assertEqual(type(data), pd.DataFrame)

    def test_data_contents(self):
        """The data should contain the relevant columns and not be empty."""
        ppipi, pKK = lhcb_paper_2017_044.data()
        columns = ['training_weight', 'Lc_PT', 'Lc_ETA', 'Lc_p_PT', 'Lc_p_ETA']

        self.assertEqual(list(ppipi.columns), columns + ['kinematic_weight'])
        self.assertGreater(len(ppipi), 0)

        self.assertEqual(list(pKK.columns), columns)
        self.assertGreater(len(pKK), 0)

    def test_weighting_function(self):
        """The weighting function should return a `GBReweighter` object."""
        clf = lhcb_paper_2017_044.weighting_function()
        self.assertEqual(type(clf), hep_ml.reweight.GBReweighter)

    def test_weighting_function_predict_weights(self):
        """The weighting function should predict weights."""
        clf = lhcb_paper_2017_044.weighting_function()

        # This could equally be a 2D numpy array or a pandas DataFrame
        data = [
            [2500, 3, 1000, 2.5],
            [5000, 3.8, 3400, 3]
        ]
        weights = clf.predict_weights(data)

        expected = np.array([0.95024977,  0.86829971])
        self.assertTrue(np.allclose(weights, expected))


if __name__ == '__main__':
    unittest.main()
