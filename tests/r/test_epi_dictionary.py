from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.epi_dictionary import epi_dictionary


def test_epi_dictionary():
  """Test module epi_dictionary.py by downloading
   epi_dictionary.csv and testing shape of
   extracted data has 57 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = epi_dictionary(test_path)
  try:
    assert x_train.shape == (57, 1)
  except:
    shutil.rmtree(test_path)
    raise()
