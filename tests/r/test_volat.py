from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.volat import volat


def test_volat():
  """Test module volat.py by downloading
   volat.csv and testing shape of
   extracted data has 558 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = volat(test_path)
  try:
    assert x_train.shape == (558, 17)
  except:
    shutil.rmtree(test_path)
    raise()
