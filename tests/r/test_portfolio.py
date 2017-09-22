from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.portfolio import portfolio


def test_portfolio():
  """Test module portfolio.py by downloading
   portfolio.csv and testing shape of
   extracted data has 100 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = portfolio(test_path)
  try:
    assert x_train.shape == (100, 2)
  except:
    shutil.rmtree(test_path)
    raise()
