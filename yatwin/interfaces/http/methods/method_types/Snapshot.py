from .BaseMethod import BaseMethod
from ... import parameters
import cv2
import numpy
import os

"""
Imports:
    .BaseMethod.BaseMethod
    ...parameters
    cv2
    numpy
    os

Contains:
    <Snapshot>
"""

class Snapshot(BaseMethod):
    """
    Inherits from <BaseMethod>

    Provides methods to interact with the snapshot
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises super
        """

        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Disable super().__call__
        """

        return

    def get(self, *args, **kwargs):
        """
        Wrapper for BaseMethod.get

        Returns the data as bytes
        """

        resp = super().get(*args, **kwargs)

        return resp.parse_bytes()

    def download_snapshot(self, file_out='snapshot.jpg', res=0): # Missing http=
        """
        Downloads the snapshot to file_out

        :param res - The resolution parameter value
        """

        local_dir = os.getcwd()

        path = local_dir + '\\' + file_out

        params = \
        {
            parameters.RES.identifier: res,
        }

        resp = self.get(**params)

        with open(path, 'wb') as file:
            file.write(resp)

        return path

    def view_snapshot(self, res=0):
        """
        Views the snapshot using cv2.imshow

        :param res - The resolution parameter value
        """

        params = \
        {
            parameters.RES.identifier: res,
        }

        resp = self.get(**params)

        image = cv2.imdecode(numpy.fromstring(resp, dtype=numpy.uint8), cv2.IMREAD_COLOR)

        cv2.imshow('snapshot', image)
