from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.transp_eq import transp_eq


def test_transp_eq():
  """Test module transp_eq.py by downloading
   transp_eq.csv and testing shape of
   extracted data has 25 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = transp_eq(test_path)
  try:
    assert x_train.shape == (25, 5)
  except:
    shutil.rmtree(test_path)
    raise()
