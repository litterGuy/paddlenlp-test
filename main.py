import time
import traceback

from flask import Flask, request
from paddlenlp import Taskflow

from resp import JSONResponse, ErrorResponse

# 情感分析
schema = ['情感倾向[正向，负向]']
senta = Taskflow("sentiment_analysis", model="bilstm", schema=schema)

# 省市提取
province_city_schema = ['省份', '城市']
areaExtra = Taskflow('information_extraction', schema=province_city_schema)

app = Flask(__name__)


# 省市提取
def area_extraction(text):
    try:
        starttime = time.time()
        result = areaExtra(text)
        endtime = time.time()
        return {
            'result': result,
            'diff': endtime - starttime
        }
    except Exception as e:
        traceback.print_exc()


# 情感分析
def senta_extra(text):
    try:
        starttime = time.time()
        result = senta(text)
        endtime = time.time()
        return {
            'result': result,
            'diff': endtime - starttime
        }
    except Exception as e:
        traceback.print_exc()


@app.route('/nlphandle', methods=['POST'])
def nlphandle():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return ErrorResponse(1, 'Content-Type not supported!')
    json = request.json
    text = json['text']
    if text:
        try:
            starttime = time.time()
            area_res = area_extraction(text)
            senta_res = senta_extra(text)
            endtime = time.time()
            return JSONResponse({
                'senta': senta_res,
                'area': area_res,
                'diff': endtime - starttime
            })
        except BaseException as err:
            return ErrorResponse(1, str(err))
    else:
        return ErrorResponse(1, 'param is null')


if __name__ == '__main__':
    app.run()
