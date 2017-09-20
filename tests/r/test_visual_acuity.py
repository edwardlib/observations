from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.visual_acuity import visual_acuity


def test_visual_acuity():
  """Test module visual_acuity.py by downloading
   visual_acuity.csv and testing shape of
   extracted data has 32 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = visual_acuity(test_path)
  try:
    assert x_train.shape == (32, 4)
  except:
    shutil.rmtree(test_path)
    raise()
