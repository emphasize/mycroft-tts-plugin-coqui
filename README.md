# mycroft-tts-plugin-coqui

This TTS service requires a running instance of [Mycroft](https://github.com/MycroftAI/mycroft-core)

Furthermore a running Coqui TTS server built from [this source](https://github.com/emphasize/TTS). # The original source code does not provide the api needed


Configuration parameters (only the url is mandatory, other are defaulted as in the following) :

```json
"tts": {
    "module": "coqui_remote",
    "coqui_remote": {
        "url": "insert_your_server_url_here",  # without api endpoint
        "speaker_idx": 2,                      # if multispeaker; optional, default ""
        "style_wav": ""                        # optional, default ""
    }
}
```

##### Installation

`mycroft-pip install mycroft-tts-plugin-coqui`

##### LICENSE :

Apache-2.0