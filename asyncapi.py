
from flask import Flask, jsonify,redirect
import asyncio
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/asyncapi')

async def intro():
    await asyncio.sleep(1)
    return ("Welcom To Async API")

async def hello():
    await asyncio.sleep(1) 
    return ("Developer name : " + os.environ.get('DEVELOPER_NAME'))


@app.route('/asyncapi',methods=['GET'])
async def async_view():
    res=await intro()
    result = await hello()
    return jsonify(res,result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3080)
