
from flask import Flask, jsonify,redirect
import asyncio

app = Flask(__name__)
app.route('/')
def index():
    return redirect('/asyncapi')

async def async_task():
    await asyncio.sleep(1)
    return {'status': 'success'}

    

@app.route('/asyncapi', methods=['GET'])
async def async_view():
    result = await async_task()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
