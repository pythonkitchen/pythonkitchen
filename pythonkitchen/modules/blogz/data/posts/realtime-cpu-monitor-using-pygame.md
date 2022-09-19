title: Realtime CPU monitor using PyGame
slug: realtime-cpu-monitor-using-pygame
pub: Thu, 26 Nov 2020 14:26:01 +0000

Here's a realtime CPU monitor using PyGame:


```python
'''
Author: https://github.com/Abdur-rahmaanJ
Instructions: 
    pip install psutil hooman==0.3.6
'''

from hooman import Hooman
import psutil
import pygame

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)

bg_col = (255, 255, 255)


loop_var = 0
time_unit = 0
graph_data = []


hapi.stroke_size(3)
hapi.stroke(hapi.color['black'])

while hapi.is_running:
    loop_var += 1
    hapi.background(bg_col)

    if loop_var % 10 == 0:
        time_unit += 1
        graph_data.append([round(time_unit), round(psutil.cpu_percent())])
        #print(graph_data)

    if graph_data:
        range_data = list(zip(*graph_data ))
        max_time =  round(max(range_data[0]))
        max_cycle =  round(max(range_data[1]))
    else:
        max_time = 100
        max_cycle = 100

    hapi.linechart(
        30,
        30,
        400,
        300,
        {
            "data": graph_data,
            "mouse_line": True,
            "range_y": [0, max_cycle],
            "range_x": [0, max_time],
        },
    )

    hapi.event_loop()
    hapi.flip_display()

pygame.quit()


```


output:
![](https://www.pythonkitchen.com/wp-content/uploads/2020/11/pygame_hooman_spu-cyles.png)
