import gym
from .hit_target import HitTargetEnv


gym.register('HitTargetEnv-v0', HitTargetEnv, max_episode_steps=1000)
