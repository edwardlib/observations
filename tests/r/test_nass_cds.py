from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nass_cds import nass_cds


def test_nass_cds():
  """Test module nass_cds.py by downloading
   nass_cds.csv and testing shape of
   extracted data has 26217 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nass_cds(test_path)
  try:
    assert x_train.shape == (26217, 15)
  except:
    shutil.rmtree(test_path)
    raise()
