from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cushny_peebles_n import cushny_peebles_n


def test_cushny_peebles_n():
  """Test module cushny_peebles_n.py by downloading
   cushny_peebles_n.csv and testing shape of
   extracted data has 11 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cushny_peebles_n(test_path)
  try:
    assert x_train.shape == (11, 4)
  except:
    shutil.rmtree(test_path)
    raise()
