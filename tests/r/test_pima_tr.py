from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pima_tr import pima_tr


def test_pima_tr():
  """Test module pima_tr.py by downloading
   pima_tr.csv and testing shape of
   extracted data has 200 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pima_tr(test_path)
  try:
    assert x_train.shape == (200, 8)
  except:
    shutil.rmtree(test_path)
    raise()
