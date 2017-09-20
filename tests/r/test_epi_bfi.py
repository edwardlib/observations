from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.epi_bfi import epi_bfi


def test_epi_bfi():
  """Test module epi_bfi.py by downloading
   epi_bfi.csv and testing shape of
   extracted data has 231 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = epi_bfi(test_path)
  try:
    assert x_train.shape == (231, 13)
  except:
    shutil.rmtree(test_path)
    raise()
