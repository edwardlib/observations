from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mhtdata import mhtdata


def test_mhtdata():
  """Test module mhtdata.py by downloading
   mhtdata.csv and testing shape of
   extracted data has 159312 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mhtdata(test_path)
  try:
    assert x_train.shape == (159312, 8)
  except:
    shutil.rmtree(test_path)
    raise()
