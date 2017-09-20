from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.possum_div import possum_div


def test_possum_div():
  """Test module possum_div.py by downloading
   possum_div.csv and testing shape of
   extracted data has 151 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = possum_div(test_path)
  try:
    assert x_train.shape == (151, 9)
  except:
    shutil.rmtree(test_path)
    raise()
