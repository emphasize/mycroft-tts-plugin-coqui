# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests

from mycroft.tts import TTSValidator
from mycroft.tts.remote_tts import RemoteTTS


class CoquiRemoteTTSPlugin(RemoteTTS):

    def __init__(self, lang, config):
        super(CoquiRemoteTTSPlugin, self).__init__(lang, config, config.get('url'),
                                                   '/api/tts', CoquiTTSValidator(self))
        self.speaker_idx = self.config.get("speaker_id", "")
        self.style_wav = self.config.get("style_wav", "")

    # RemoteTTS is splitting sentences up. Overwrite, let coqui do its job
    @staticmethod
    def __get_phrases(sentence):
        return sentence

    def build_request_params(self, sentence):
        params = dict()
        params['text'] = sentence.encode('utf-8')
        params['speaker_id'] = self.speaker_idx
        params['style_wav'] = self.style_wav
        return params


class CoquiTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(CoquiTTSValidator, self).__init__(tts)

    def validate_lang(self):
        pass

    def validate_connection(self):
        try:
            resp = requests.get(self.tts.url + "/health", verify=False)
            if resp.status_code == 200:
                return True
        except Exception:
            raise Exception(
                'CoquiTTS server could not be verified. Check your connection '
                'to the server: ' + self.tts.url)

    def get_tts_class(self):
        return CoquiRemoteTTSPlugin
