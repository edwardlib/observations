from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.flight_response import flight_response


def test_flight_response():
  """Test module flight_response.py by downloading
   flight_response.csv and testing shape of
   extracted data has 464 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = flight_response(test_path)
  try:
    assert x_train.shape == (464, 7)
  except:
    shutil.rmtree(test_path)
    raise()
