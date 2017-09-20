from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chain import chain


def test_chain():
  """Test module chain.py by downloading
   chain.csv and testing shape of
   extracted data has 532 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chain(test_path)
  try:
    assert x_train.shape == (532, 7)
  except:
    shutil.rmtree(test_path)
    raise()
