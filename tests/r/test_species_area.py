from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.species_area import species_area


def test_species_area():
  """Test module species_area.py by downloading
   species_area.csv and testing shape of
   extracted data has 14 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = species_area(test_path)
  try:
    assert x_train.shape == (14, 5)
  except:
    shutil.rmtree(test_path)
    raise()
