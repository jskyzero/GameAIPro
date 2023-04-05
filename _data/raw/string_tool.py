# -*- coding: utf-8 -*-
"""

usage:
    python3 _data/raw/string_tool.py
"""

if __name__ == "__main__":
    src = """
17.【寻路架构的优化】
18.【选择搜索空间的呈现形式】
19.【创建高阶导航网格】
20.【MMO寻路预计算】
21.【编队运动技术】
22.【预规划碰撞回避】
23.【群体寻路】
24.【高效群体寻路】
26.【动画驱动的移动规划】
26.【战术点选择】
27.【NavMesh上的战术寻路】
28.【管理NPC攻击】
29.【分层AI设计】
30.【神经网络】
31.【目标记录】
32.【潜行游戏感知】
33.【聪明的询问环境】
34.【知识系统】
35.【社交动态系统】
36.【带来生活气息】
37.【托词与愚弄】
38.【AI架构】
39.【AI控制载具】
40.【PID控制器】
41.【热视觉确定最优路径】
42.【橡皮筋系统】
43.【社交模拟架构】
44.【控制动物行为】
45.【GPGPU】
46.【虚拟音效】
47.【第三人称摄像机】
48.【N-Gram技术】




"""
    for str in src.split('\n'):
      if '【' in str:
        result = str[str.find('【')+1:str.find('】')]
        print(result.strip())