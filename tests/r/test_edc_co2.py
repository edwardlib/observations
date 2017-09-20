from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.edc_co2 import edc_co2


def test_edc_co2():
  """Test module edc_co2.py by downloading
   edc_co2.csv and testing shape of
   extracted data has 1096 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = edc_co2(test_path)
  try:
    assert x_train.shape == (1096, 2)
  except:
    shutil.rmtree(test_path)
    raise()
