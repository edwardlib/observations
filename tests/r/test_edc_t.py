from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.edc_t import edc_t


def test_edc_t():
  """Test module edc_t.py by downloading
   edc_t.csv and testing shape of
   extracted data has 5788 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = edc_t(test_path)
  try:
    assert x_train.shape == (5788, 5)
  except:
    shutil.rmtree(test_path)
    raise()
