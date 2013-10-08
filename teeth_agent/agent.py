"""
Copyright 2013 Rackspace, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from teeth_agent.client import TeethClient
from teeth_agent.logging import get_logger
log = get_logger()


class StandbyAgent(TeethClient):
    """
    Agent to perform standbye operations.
    """

    def __init__(self, addrs):
        super(StandbyAgent, self).__init__(addrs)
        self._addHandler('v1', 'prepare_image', self.prepare_image)
        log.msg('Starting agent', addrs=addrs)

    def prepare_image(self, message):
        """Prepare an Image."""

        if 'image_id' not in message.params:
            raise Exception('missing required parameter "image_id" in call to prepare_image')

        image_id = message.params['image_id']

        log.msg('Preparing image', image_id=image_id)
        return {'image_id': image_id, 'status': 'PREPARED'}
