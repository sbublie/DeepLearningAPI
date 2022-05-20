# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PredictionResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, prediction=None):  # noqa: E501
        """PredictionResult - a model defined in OpenAPI

        :param prediction: The prediction of this PredictionResult.  # noqa: E501
        :type prediction: int
        """
        self.openapi_types = {
            'prediction': int
        }

        self.attribute_map = {
            'prediction': 'prediction'
        }

        self._prediction = prediction

    @classmethod
    def from_dict(cls, dikt) -> 'PredictionResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PredictionResult of this PredictionResult.  # noqa: E501
        :rtype: PredictionResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def prediction(self):
        """Gets the prediction of this PredictionResult.


        :return: The prediction of this PredictionResult.
        :rtype: int
        """
        return self._prediction

    @prediction.setter
    def prediction(self, prediction):
        """Sets the prediction of this PredictionResult.


        :param prediction: The prediction of this PredictionResult.
        :type prediction: int
        """

        self._prediction = prediction
