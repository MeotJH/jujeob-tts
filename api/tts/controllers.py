from http import HTTPStatus

from flask import request
from flask_restx import Resource, fields

from api import tts_api as api
from api.tts import services
from util.logging_util import logger

voice_field = fields.String(required=True, title='목소리 타겟 텍스트', description="해당 문자가 TTS로 변환됨", example='Hello World')
binary_field = fields.String(required=True, title='tts 목소리 바이너리 데이터', description="TTS 바이너리로 변환된")
tts_text_field = fields.String(required=True, title='tts 텍스트 데이터', description="TTS 바이너리로 변환된")

tts_request_model = api.model('TTSRequestModel', {
    'voice': voice_field}
                              )

users_response_model = api.model('TTSResponseModel', {
    'voice': binary_field,
    'text' : tts_text_field,
}
                                 )


@api.route('/', strict_slashes=False)
class TTS(Resource):
    @api.doc(params={'voice': 'Hello World'})
    @api.marshal_with(users_response_model, envelope='data')
    def get(self):
        voice = request.args.get('voice')

        if not voice:
            return {'voice': 'voice is required'}, HTTPStatus.BAD_REQUEST
        jujeob = services.get_jujeob(voice)
        return {'voice': jujeob['voice'], 'text': jujeob['text']}, HTTPStatus.OK



