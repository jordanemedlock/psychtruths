# -*- coding: utf-8 -*-

###############################################################################
#
# GetHistoricalUpdates
# Returns impression and engagement data on company shares for a given company page.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetHistoricalUpdates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetHistoricalUpdates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetHistoricalUpdates, self).__init__(temboo_session, '/Library/LinkedIn/Companies/GetHistoricalUpdates')


    def new_input_set(self):
        return GetHistoricalUpdatesInputSet()

    def _make_result_set(self, result, path):
        return GetHistoricalUpdatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetHistoricalUpdatesChoreographyExecution(session, exec_id, path)

class GetHistoricalUpdatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetHistoricalUpdates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the Client ID).)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process (AKA the OAuth User Secret).)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process (AKA the OAuth User Token).)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('AccessToken', value)
    def set_CompanyID(self, value):
        """
        Set the value of the CompanyID input for this Choreo. ((required, integer) A LinkedIn assigned ID associated with the company.)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('CompanyID', value)
    def set_EndTimestamp(self, value):
        """
        Set the value of the EndTimestamp input for this Choreo. ((optional, date) The starting timestamp of when the stats search should begin (milliseconds since epoch). The current time will be used if a timestamp is not provided.)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('EndTimestamp', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the Client Secret).)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('SecretKey', value)
    def set_StartTimestamp(self, value):
        """
        Set the value of the StartTimestamp input for this Choreo. ((required, date) The starting timestamp of when the stats search should begin (milliseconds since epoch). The current time will be used if a timestamp is not provided.)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('StartTimestamp', value)
    def set_TimeGranularity(self, value):
        """
        Set the value of the TimeGranularity input for this Choreo. ((required, string) Granularity of statistics. Valid values are: day, month.)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('TimeGranularity', value)
    def set_UpdateKey(self, value):
        """
        Set the value of the UpdateKey input for this Choreo. ((optional, string) Optionally provide an update key value to return statistics for a specific company update.)
        """
        super(GetHistoricalUpdatesInputSet, self)._set_input('UpdateKey', value)

class GetHistoricalUpdatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetHistoricalUpdates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class GetHistoricalUpdatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetHistoricalUpdatesResultSet(response, path)
