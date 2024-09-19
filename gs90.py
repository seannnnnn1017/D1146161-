import Jetson.GPIO as GPIO
import time

# 設置 GPIO 針腳編號模式
GPIO.setmode(GPIO.BOARD)

# 定義 PWM 使用的 GPIO 針腳，這裡假設使用的是 33 針腳 (根據你的硬體情況修改)
pwm_pin = 33
GPIO.setup(pwm_pin, GPIO.OUT)

# 設定 PWM 頻率 (SG90 通常使用 50Hz)
pwm = GPIO.PWM(pwm_pin, 50)

# 啟動 PWM，初始占空比設為 0
pwm.start(0)

# 定義轉動到90度的脈寬（1.5ms 對應大約 7.5% 的占空比）
def set_angle(angle):
    duty = (0.05 * angle) + 2.5  # 計算對應角度的占空比
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # 保持脈衝一段時間，讓馬達有時間移動到位
    pwm.ChangeDutyCycle(0)  # 停止信號以防止持續抖動

try:
    # 讓舵機轉到 90 度
    set_angle(90)
finally:
    # 清理資源
    pwm.stop()
    GPIO.cleanup()
