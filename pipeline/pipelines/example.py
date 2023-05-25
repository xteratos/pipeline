import json
from kfp.v2 import compiler
from kfp.v2 import dsl
from kfp.v2.dsl import component

# A simple component that prints and returns a greeting string
@component
def hello_world(message: str) -> str:
    greeting_str = f'Hello, {message}'
    print(greeting_str)
    return greeting_str

# A simple pipeline that contains a single hello_world task
@dsl.pipeline(
    name='hello-world-scheduled-pipeline')
def hello_world_scheduled_pipeline(greet_name: str):
    hello_world_task = hello_world(greet_name)

# Compile the pipeline and generate a JSON file
compiler.Compiler().compile(pipeline_func=hello_world_scheduled_pipeline,
                            package_path='hello_world_scheduled_pipeline.json')