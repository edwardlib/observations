from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cushny_peebles import cushny_peebles


def test_cushny_peebles():
  """Test module cushny_peebles.py by downloading
   cushny_peebles.csv and testing shape of
   extracted data has 11 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cushny_peebles(test_path)
  try:
    assert x_train.shape == (11, 4)
  except:
    shutil.rmtree(test_path)
    raise()
