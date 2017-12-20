# coding: utf-8
from __future__ import absolute_import, division, print_function
import os

import hep_ml.reweight
import pandas as pd

# Path to gzipped-compressed CSV files containing the input data
PPIPI_DATA_PATH = 'data/LcToppipi.csv.gz'
PKK_DATA_PATH = 'data/LcTopKK.csv.gz'
# Column name in the input data used as a weight to the GBDT training
TRAINING_WEIGHT = 'training_weight'
# Column name in the input data used in the analysis itself (i.e. the
# 'original' weights, which this module can generate a representative sample
# of)
KINEMATIC_WEIGHT = 'kinematic_weight'


def data():
    """Return pandas.DataFrame objects for the pππ and pKK input data."""
    # The directory that *this* file is in, the file you're looking at
    thisfile_dir, _ = os.path.split(__file__)
    ppipi_path = os.path.join(thisfile_dir, PPIPI_DATA_PATH)
    pKK_path = os.path.join(thisfile_dir, PKK_DATA_PATH)

    read_opts = dict(index_col=False, encoding='utf-8', compression='gzip')
    ppipi = pd.read_csv(ppipi_path, **read_opts)
    pKK = pd.read_csv(pKK_path, **read_opts)

    return ppipi, pKK


def weighting_function():
    r"""Return the pππ weighting function.

    The weighting function is a classifier of type `GBReweighter`, as defined
    in the hep_ml package. Weights can be obtained from it using the
    `predict_weights` method. This takes an array of input vectors, each
    containing, in order:

    1. the transverse momentum of the Λc+;
    2. the pseudorapidity of the Λc+;
    3. the transverse momentum of the proton from the Λc+; and
    4. the transverse momentum of the proton form the Λc+.

    Momentum should be specified in MeV/c. The input vectors can be a list of
    lists (regular Python lists, that is), a two-dimensional numpy array, or a
    pandas DataFrame object.

    The weights return by `predict_weights` are applied to the pππ candidates.

    Example
    =======

    ```python
    from lhcb_paper_2017_044 import weighting_function

    clf = weighting_function()
    clf.predict_weights([
        [2500, 3, 1000, 2.5],
        [5000, 3.8, 3400, 3],
    ])
    # Returns array([ 1.01120624,  0.77987936])
    ```
    """
    original, target = data()
    # We're re-generating weights, so discard those used in the analysis
    original.pop(KINEMATIC_WEIGHT)
    original_weight = original.pop(TRAINING_WEIGHT)
    target_weight = target.pop(TRAINING_WEIGHT)
    assert (original.columns == target.columns).all(), 'Mismatched columns'

    nfeatures = original.columns.size
    gb_args = dict(max_leaf_nodes=nfeatures, subsample=1.0,
                   random_state=23475)
    gbr_args = dict(n_estimators=300, learning_rate=0.025, max_depth=2)

    reweighter = hep_ml.reweight.GBReweighter(gb_args=gb_args, **gbr_args)
    reweighter.fit(
        original=original, target=target,
        original_weight=original_weight, target_weight=target_weight
    )

    return reweighter
