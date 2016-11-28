# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from msrest.serialization import Model


class Trigger(Model):
    """A condition to be satisfied for an action to be executed.

    :param lifetime_percentage: Percentage of lifetime as which to trigger.
     Value should be between 1 and 99.
    :type lifetime_percentage: int
    :param days_before_expiry: Days before expiry.
    :type days_before_expiry: int
    """ 

    _validation = {
        'lifetime_percentage': {'maximum': 99, 'minimum': 1},
    }

    _attribute_map = {
        'lifetime_percentage': {'key': 'lifetime_percentage', 'type': 'int'},
        'days_before_expiry': {'key': 'days_before_expiry', 'type': 'int'},
    }

    def __init__(self, lifetime_percentage=None, days_before_expiry=None):
        self.lifetime_percentage = lifetime_percentage
        self.days_before_expiry = days_before_expiry