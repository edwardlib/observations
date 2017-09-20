from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ceosal1 import ceosal1


def test_ceosal1():
  """Test module ceosal1.py by downloading
   ceosal1.csv and testing shape of
   extracted data has 209 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ceosal1(test_path)
  try:
    assert x_train.shape == (209, 12)
  except:
    shutil.rmtree(test_path)
    raise()
