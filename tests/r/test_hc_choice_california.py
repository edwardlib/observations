from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hc_choice_california import hc_choice_california


def test_hc_choice_california():
  """Test module hc_choice_california.py by downloading
   hc_choice_california.csv and testing shape of
   extracted data has 250 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hc_choice_california(test_path)
  try:
    assert x_train.shape == (250, 18)
  except:
    shutil.rmtree(test_path)
    raise()
