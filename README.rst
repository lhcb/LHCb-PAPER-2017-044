LHCb-PAPER-2017-044 supplementary material
==========================================

This repository contains supplementary material for LHCb-PAPER-2017-044_, a
publication_ of a search for CP violation in charm baryon decays.

The repository is a Python package containing an implementation of a weighting
function that is used in the analysis, and is provided so that others may
weight their data in a similar manner, for comparison to the publised results.

The package can be installed with the pip_ command::

    $ pip install git+https://github.com/lhcb/LHCb-PAPER-2017-044.git

The correctness of the installation can be verified by running the test suite::

    $ python -m lhcb_paper_2017_044.tests

Once installed, the weighting function can be obtained by using the
``weighting_function`` method in the ``lhcb_paper_2017_044`` module::

    >>> import lhcb_paper_2017_044
    >>> clf = lhcb_paper_2017_044.weighting_function()
    >>> clf.predict_weights(...)

Documentation on the method is given in the implementation_.

In the publication, the weights are used to align the kinematic spectrum of pππ
data with that of pKK data. For comparison with other results, external pππ
data can be given as input to the ``clf.predict_weights`` method, and the
return value can then be used to weight the external data. Additional
information on the role of the weighting function, and the motivation for
providing it, is given in LHCb-PAPER-2017-044_.

Dataset
-------

The data provided here represents a subsample of the data used in the analysis,
specifically the data taken at a centre-of-mass energy of 8 TeV and with
the LHCb dipole magnet in the 'down' polarity. In the analysis, two classifiers
are trained per subsample, but ``weighting_function`` returns one
*representative* classifier. The exact weights used in the analysis are also
provided, for comparison, as the ``kinematic_weight`` column::

    >>> import lhcb_paper_2017_044
    >>> ppipi, pKK = lhcb_paper_2017_044.data()
    >>> ppipi.kinematic_weight.head()
    0    1.313518
    1    0.913545
    2    0.026368
    3    0.005139
    4    1.204687
    Name: kinematic_weight, dtype: float64

Issues
------

If you have any questions on the usage or interpretation of the package, please
`open an issue`_.

.. _LHCb-PAPER-2017-044: https://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2017-044.html
.. _publication: https://arxiv.org/abs/1712.07051
.. _pip: https://packaging.python.org/tutorials/installing-packages/
.. _implementation: lhcb_paper_2017_044/__init__.py
.. _open an issue: https://github.com/lhcb/LHCb-PAPER-2017-044/issues
