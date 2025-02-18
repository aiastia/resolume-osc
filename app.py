from flask import Flask, render_template, request, jsonify
from pythonosc import udp_client

app = Flask(__name__)

# 配置 Resolume 的 IP 和 OSC 端口
resolume_ip = "127.0.0.1"  # 如果 Resolume 运行在同一台机器上，使用 localhost
resolume_port = 7000       # 默认 OSC 端口

# 创建 OSC 客户端
try:
    client = udp_client.SimpleUDPClient(resolume_ip, resolume_port)
    print(f"OSC 客户端已创建，目标地址：{resolume_ip}:{resolume_port}")
except Exception as e:
    print(f"创建 OSC 客户端时出错：{e}")
    exit()

# 发送 OSC 消息函数
def send_osc_message(address, value):
    try:
        client.send_message(address, value)
        print(f"已发送消息：地址={address}, 值={value}")
        return True, f"已发送消息：地址={address}, 值={value}"
    except Exception as e:
        print(f"发送 OSC 消息时出错：{e}")
        return False, f"发送 OSC 消息时出错：{e}"

# 渲染首页
@app.route('/')
def index():
    return render_template('index.html')

# 定义接口：通过 POST 方式发送 OSC 消息
@app.route('/send', methods=['POST'])
def send():
    data = request.json
    address = data.get('address')
    value = data.get('value')
    if address is None or value is None:
        return jsonify({'success': False, 'message': '缺少 address 或 value 参数'}), 400
    success, message_text = send_osc_message(address, value)
    return jsonify({'success': success, 'message': message_text})

if __name__ == '__main__':
    # 监听所有网卡地址
    app.run(host="0.0.0.0", debug=True)
