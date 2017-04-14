#!/usr/bin/env python3
import perf

runner = perf.Runner()
runner.timeit("sorted(list(range(1000)), key=lambda x: x)",
              stmt="sorted(s, key=f)",
              setup="f = lambda x: x; s = list(range(1000))")
