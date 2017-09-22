from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.doctor_aus import doctor_aus


def test_doctor_aus():
  """Test module doctor_aus.py by downloading
   doctor_aus.csv and testing shape of
   extracted data has 5190 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = doctor_aus(test_path)
  try:
    assert x_train.shape == (5190, 15)
  except:
    shutil.rmtree(test_path)
    raise()
