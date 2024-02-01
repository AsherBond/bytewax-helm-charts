# ./simple.py
import bytewax.operators as op
from bytewax.testing import TestingSource
from bytewax.dataflow import Dataflow
from bytewax.connectors.stdio import StdOutSink
import time

def slow_inc(x):
    time.sleep(5)
    return x + 1

flow = Dataflow("simple")

inp = op.input("inp1", flow, TestingSource(range(99999999)))
out = op.map("slow", inp, slow_inc)
op.output("out", out, StdOutSink())




