from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_acc_deaths import us_acc_deaths


def test_us_acc_deaths():
  """Test module us_acc_deaths.py by downloading
   us_acc_deaths.csv and testing shape of
   extracted data has 72 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_acc_deaths(test_path)
  try:
    assert x_train.shape == (72, 2)
  except:
    shutil.rmtree(test_path)
    raise()
