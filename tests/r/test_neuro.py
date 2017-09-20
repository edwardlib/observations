from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.neuro import neuro


def test_neuro():
  """Test module neuro.py by downloading
   neuro.csv and testing shape of
   extracted data has 469 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = neuro(test_path)
  try:
    assert x_train.shape == (469, 6)
  except:
    shutil.rmtree(test_path)
    raise()
