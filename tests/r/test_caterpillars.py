from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.caterpillars import caterpillars


def test_caterpillars():
  """Test module caterpillars.py by downloading
   caterpillars.csv and testing shape of
   extracted data has 267 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = caterpillars(test_path)
  try:
    assert x_train.shape == (267, 18)
  except:
    shutil.rmtree(test_path)
    raise()
