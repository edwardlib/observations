from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gag_urine import gag_urine


def test_gag_urine():
  """Test module gag_urine.py by downloading
   gag_urine.csv and testing shape of
   extracted data has 314 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gag_urine(test_path)
  try:
    assert x_train.shape == (314, 2)
  except:
    shutil.rmtree(test_path)
    raise()
