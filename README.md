## stackX
###### X for Extended
> A light-weight stack from the data structures which is primarily used to store a collection of objects. Individual items can be added and stored in a stack using a push operation. Objects can be retrieved using a pop operation, which removes an item from the stack.

### Usage

##### Install the packge using,
```python
pip install stackx
```


##### Import it to your application by,
```python
from stackx import stack
```


##### Check whether stack is working or not by pinging it.
```python
stack.ping()
```
```python
'pong!'
```

##### Create your stack
```python
stack = stack(max_size=5, reset_on_full=True)
```

##### Push
```python
stack.push(10)
```

##### Pop
```python
stack.pop()
```

##### Check if the stack is full
```python
stack.full()
```
```python
False
```

##### Show all elements in the stack
```python
stack.show_all()
```
##### Reset
```python
stack.reset()
```

