from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.somerville import somerville


def test_somerville():
  """Test module somerville.py by downloading
   somerville.csv and testing shape of
   extracted data has 659 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = somerville(test_path)
  try:
    assert x_train.shape == (659, 8)
  except:
    shutil.rmtree(test_path)
    raise()
