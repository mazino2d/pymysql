### Example

```python
>>> from pzsql import core
>>> x  =  core.Executor("iotplatform")
>>> x.excute("select * from gps", func = lambda x: print(x))
{'id': 'd0_0', 'timestamp': 1591483446, 'status': 0, 'latitude': 209, 'longtitude': 185}
{'id': 'd0_0', 'timestamp': 1591483450, 'status': 1, 'latitude': 183, 'longtitude': 193}
{'id': 'd0_0', 'timestamp': 1591483483, 'status': 0, 'latitude': 290, 'longtitude': 107}
```

### Author

Khoi Dang Do @ Zalo Group
