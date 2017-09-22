from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mode_choice import mode_choice


def test_mode_choice():
  """Test module mode_choice.py by downloading
   mode_choice.csv and testing shape of
   extracted data has 840 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mode_choice(test_path)
  try:
    assert x_train.shape == (840, 7)
  except:
    shutil.rmtree(test_path)
    raise()
