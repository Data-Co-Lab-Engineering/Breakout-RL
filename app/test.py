import gym
from gym.wrappers import Monitor
from app.utils import show_video
import numpy as np



# Init the environment and the monitor
env = gym.make("Breakout-v0")
env = Monitor(env, "video", force="True")
env.reset()

for i in range(3000):
	action = np.random.randint(1, 4)
	observation, reward, terminal, info = env.step(action)
	np.invert(_["ale.lives"]).astype(np.float32)
	if terminal:
		print("Terminal state")
		env.reset()



show_video()
