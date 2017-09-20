from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bfi_dictionary import bfi_dictionary


def test_bfi_dictionary():
  """Test module bfi_dictionary.py by downloading
   bfi_dictionary.csv and testing shape of
   extracted data has 28 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bfi_dictionary(test_path)
  try:
    assert x_train.shape == (28, 7)
  except:
    shutil.rmtree(test_path)
    raise()
