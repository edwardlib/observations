from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ceosal2 import ceosal2


def test_ceosal2():
  """Test module ceosal2.py by downloading
   ceosal2.csv and testing shape of
   extracted data has 177 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ceosal2(test_path)
  try:
    assert x_train.shape == (177, 15)
  except:
    shutil.rmtree(test_path)
    raise()
