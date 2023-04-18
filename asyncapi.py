
from flask import Flask, jsonify,redirect
import asyncio

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/asyncapi')

async def hello():
    await asyncio.sleep(1) 
    return ("Hello!,Welocme to ASync API")


@app.route('/asyncapi',methods=['GET'])
async def async_view():
    result = await hello()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3080)
