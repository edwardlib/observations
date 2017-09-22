from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snow_gr import snow_gr


def test_snow_gr():
  """Test module snow_gr.py by downloading
   snow_gr.csv and testing shape of
   extracted data has 119 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snow_gr(test_path)
  try:
    assert x_train.shape == (119, 15)
  except:
    shutil.rmtree(test_path)
    raise()
