from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.caschool import caschool


def test_caschool():
  """Test module caschool.py by downloading
   caschool.csv and testing shape of
   extracted data has 420 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = caschool(test_path)
  try:
    assert x_train.shape == (420, 17)
  except:
    shutil.rmtree(test_path)
    raise()
