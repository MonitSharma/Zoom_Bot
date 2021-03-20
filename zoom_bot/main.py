import subprocess
import time
import pyautogui
import pandas as pd
from datetime import datetime


def sign_in(meeting_id, pwd):
    subprocess.call(["C:\\Users\\Monit Sharma\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"])

    time.sleep(2)

    # clicking the button

    join_button = pyautogui.locateCenterOnScreen('joint.PNG')
    pyautogui.moveTo(join_button)
    pyautogui.click()


    # the meeting id
    meeting_id_btn = pyautogui.locateCenterOnScreen('img2.PNG')
    pyautogui.moveTo(meeting_id_btn)
    #pyautogui.click()
    pyautogui.write(meeting_id)
    time.sleep(2)



    # hit the join button
    joint_button = pyautogui.locateCenterOnScreen('join2.PNG')
    pyautogui.moveTo(joint_button)
    pyautogui.click()
    time.sleep(2)



    # pwd and enter
    password_btn = pyautogui.locateCenterOnScreen('img3.PNG')
    pyautogui.moveTo(password_btn)
    #pyautogui.click()
    pyautogui.write(pwd)
    pyautogui.press('enter')


#sign_in('793 5637 0762', 'UTl1Z2lDV293NXQyUVBPaExHM3c0UT09')
df = pd.read_csv('timing.csv')

while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

        row = df.loc[df['timings'] == now]
        m_id = str(row.iloc[0,1])
        m_pwd = str(row.iloc[0,2])

        sign_in(m_id, m_pwd)
        time.sleep(40)
        print('signed in')
