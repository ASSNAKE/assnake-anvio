import os, assnake

import assnake_anvio.result
from assnake.utils import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))

snake_module = assnake.SnakeModule(
    name = 'assnake-anvio', 
    install_dir = this_dir,
    results = [
        assnake_anvio.result
    ],

    snakefiles = [],
    invocation_commands = []
)
