"""Module config. Initialize configparser."""
import configparser

config = configparser.ConfigParser()
config.read('praw.ini')
